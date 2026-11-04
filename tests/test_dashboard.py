"""Run the notebook export first, then: python -m pytest tests/test_dashboard.py."""

import pandas as pd
import pytest
from streamlit.testing.v1 import AppTest

from dashboard.data import (
    ROOT, SNAPSHOT_PATH, PLAN_ORDER, filter_members, load_snapshot, service_rates, summary_metrics,
)

pytestmark = pytest.mark.skipif(not SNAPSHOT_PATH.exists(), reason="Run the notebook to export dashboard data first.")


def test_notebook_counts_and_filtered_denominators():
    frame = load_snapshot()
    before = frame.copy(deep=True)
    metrics = summary_metrics(frame)
    assert metrics["members"] == 15450
    assert metrics["revenue_n"] == 14328
    assert metrics["median_revenue"] == 859.22
    assert metrics["utilization_n"] == 15440
    assert metrics["median_utilization_pct"] == 51.75
    assert metrics["zero_999"] == 1296
    assert metrics["anomaly_flagged"] == 144
    private = filter_members(frame, ["private_office"])
    assert summary_metrics(private)["members"] == 664
    assert summary_metrics(private)["revenue_n"] == 591
    assert summary_metrics(private)["median_revenue"] == 20000.08
    assert summary_metrics(private)["median_utilization_pct"] == 14.79
    rates = service_rates(private).set_index("Service")["Members (%)"]
    assert round(rates["Mail Handling"], 1) == 76.5
    assert round(rates["Day Passes"], 1) == 5.3
    flagged = filter_members(frame, PLAN_ORDER, cohort="Anomaly review candidates")
    assert len(flagged) == 144 and flagged["zero_999"].sum() == 66
    assert len(filter_members(frame, PLAN_ORDER, cohort="Not scored for anomalies")) == 1132
    assert filter_members(frame, []).empty
    assert pd.isna(summary_metrics(filter_members(frame, []))["median_revenue"])
    pd.testing.assert_frame_equal(frame, before)


def test_app_filters_reset_empty_selection_and_anomaly_coverage():
    app = AppTest.from_file(str(ROOT / "dashboard/app.py"), default_timeout=30).run()
    assert not app.exception
    assert app.metric[0].value == "15,450"
    assert app.metric[1].value == "859.22 €"
    app.multiselect(key="plans").set_value(["private_office"]).run()
    assert not app.exception
    assert app.metric[0].value == "664"
    assert app.metric[1].value == "20,000.08 €"
    app.selectbox(key="account").set_value("Team").run()
    assert not app.exception
    frame = load_snapshot()
    expected = frame.loc[(frame["plan_tier"] == "private_office") & frame["is_team_account"]]
    assert app.metric[0].value == f"{len(expected):,}"
    app.button[0].click().run()
    assert app.metric[0].value == "15,450"
    app.selectbox(key="cohort").set_value("Anomaly review candidates").run()
    assert not app.exception
    assert app.metric[0].value == "144"
    app.selectbox(key="cohort").set_value("Not scored for anomalies").run()
    assert not app.exception
    assert app.metric[0].value == "1,132"
    app.multiselect(key="plans").set_value([]).run()
    assert not app.exception
    assert not app.metric
    assert any("No members match" in element.value for element in app.info)


def test_member_lookup_and_revenue_scale():
    app = AppTest.from_file(str(ROOT / "dashboard/app.py"), default_timeout=30).run()
    app.text_input(key="member_search").set_value("cw005743").run()
    assert not app.exception
    rows = app.dataframe[1].value
    assert len(rows) == 1 and rows.iloc[0]["member_id"] == "CW005743"
    assert rows.iloc[0]["lifetime_value"] == 878005
    assert app.metric[0].value == "15,450"  # ID search affects only the member table.
    app.toggle(key="revenue_log").set_value(False).run()
    assert not app.exception
    assert app.metric[1].value == "859.22 €"
    app.text_input(key="member_search").set_value("not-a-member").run()
    assert not app.exception
    assert app.dataframe[1].value.empty
