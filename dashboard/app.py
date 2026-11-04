"""Run from the repository with: python -m streamlit run dashboard/app.py."""

from pathlib import Path
import sys

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from dashboard.data import (
    PLAN_ORDER, REVIEW_COHORTS, SERVICE_COLUMNS, SNAPSHOT_PATH,
    filter_members, load_snapshot, plan_summary, service_rates, summary_metrics,
)

st.set_page_config(page_title="ACDC · Member Explorer", layout="wide")
st.title("ACDC Member Explorer")
st.caption("Group 21 · Explore economic value, workspace utilization and service needs")


@st.cache_data(show_spinner=False)
def read_data(path, modified_ns):
    # Include modification time in the cache key after a new notebook export.
    return load_snapshot(path)


def reset_filters():
    for key in ["plans", "account", "cohort", "member_search", "revenue_log"]:
        st.session_state.pop(key, None)


def show_number(value, suffix=""):
    return "Unavailable" if pd.isna(value) else f"{value:,.2f}{suffix}"


if not SNAPSHOT_PATH.exists():
    st.info("Prepare the dashboard data by running all cells in Group21_EDA_Code.ipynb first.")
    st.markdown("The final dashboard section exports the prepared data. See the repository README for setup.")
    st.stop()

try:
    data = read_data(str(SNAPSHOT_PATH), SNAPSHOT_PATH.stat().st_mtime_ns)
except (ValueError, KeyError, OSError) as error:
    st.error(f"The prepared dataset could not be opened: {error}")
    st.stop()

available_plans = [plan for plan in PLAN_ORDER if plan in data["plan_tier"].unique()]
st.sidebar.header("Explore a group")
plans = st.sidebar.multiselect(
    "Membership plans", available_plans, default=available_plans,
    format_func=lambda value: value.replace("_", " ").title(), key="plans",
)
account = st.sidebar.selectbox("Account type", ["All accounts", "Individual", "Team"], key="account")
cohort = st.sidebar.selectbox("Review cohort", REVIEW_COHORTS, key="cohort")
st.sidebar.button("Reset filters", on_click=reset_filters)
st.sidebar.caption("Filters select descriptive groups. They do not assign customer clusters.")

selected = filter_members(data, plans, account, cohort)
metrics = summary_metrics(selected)
st.subheader(f"{metrics['members']:,} members selected")
st.caption(f"{len(data):,} unique members available · filters apply to indicators, charts and tables")
if selected.empty:
    st.info("No members match these filters. Select at least one plan or reset the filters.")
    st.stop()

cards = st.columns(4)
cards[0].metric("Selected members", f"{metrics['members']:,}")
cards[0].caption(f"{100 * metrics['members'] / len(data):.1f}% of all members")
cards[1].metric("Median lifetime revenue", show_number(metrics["median_revenue"], " €"))
cards[1].caption(f"Observed nonnegative revenue: {metrics['revenue_n']:,} / {metrics['members']:,}")
cards[2].metric("Median plan utilization", show_number(metrics["median_utilization_pct"], "%"))
cards[2].caption(f"Defined ratios: {metrics['utilization_n']:,} / {metrics['members']:,}")
cards[3].metric("Median services used", f"{metrics['median_services']:g}")
cards[3].caption("Reported variety across nine services")

st.caption(
    f"Revenue missing: {metrics['missing_revenue']:,} · negative: {metrics['negative_revenue']:,} · "
    f"zero/999 pattern: {metrics['zero_999']:,} · anomaly review candidates: "
    f"{metrics['anomaly_flagged']:,} / {metrics['anomaly_scored']:,} scored members in this selection"
)

overview, details = st.tabs(["Distributions & services", "Compare plans & inspect members"])
with overview:
    left, right = st.columns(2)
    with left:
        st.subheader("Economic value")
        use_log = st.toggle("Compress the revenue scale", value=True, key="revenue_log")
        revenue = selected.loc[selected["lifetime_value"] >= 0, ["lifetime_value"]].copy()
        if revenue.empty:
            st.info("No observed nonnegative revenue is available for this selection.")
        else:
            revenue["Revenue"] = np.log1p(revenue["lifetime_value"]) if use_log else revenue["lifetime_value"]
            label = "log(1 + lifetime revenue in EUR)" if use_log else "Lifetime revenue (EUR)"
            chart = px.histogram(revenue, x="Revenue", nbins=35, color_discrete_sequence=["#536A60"])
            chart.update_layout(xaxis_title=label, yaxis_title="Members", height=320, margin=dict(t=15, b=45))
            st.plotly_chart(chart, width="stretch", key="revenue_chart")
            st.caption(f"n = {len(revenue):,}. Zeros and the full upper tail remain included.")
    with right:
        st.subheader("Plan utilization")
        utilization = selected[["utilization_rate"]].dropna().mul(100)
        if utilization.empty:
            st.info("No defined utilization ratios are available for this selection.")
        else:
            chart = px.histogram(utilization, x="utilization_rate", nbins=25, color_discrete_sequence=["#A18E6C"])
            chart.update_layout(xaxis_title="Last-period utilization (%)", yaxis_title="Members", height=320, margin=dict(t=15, b=45))
            st.plotly_chart(chart, width="stretch", key="utilization_chart")
            st.caption(f"n = {len(utilization):,}. Undefined ratios are excluded only from this chart.")

    st.subheader("Reported service needs")
    chart = px.bar(service_rates(selected), x="Members (%)", y="Service", orientation="h", color_discrete_sequence=["#536A60"])
    chart.update_layout(xaxis_range=[0, 100], height=360, margin=dict(t=10, b=30))
    st.plotly_chart(chart, width="stretch", key="services_chart")
    st.caption("Denominator: all selected members. Services can overlap; flags measure reported past use, not intensity.")

with details:
    st.subheader("Compare current membership plans")
    st.dataframe(plan_summary(selected), width="stretch")
    st.caption("Separate medians and available observation counts. The current plan may not describe the entire membership history.")
    st.subheader("Inspect selected members")
    query = st.text_input("Find a member by ID", placeholder="For example, CW005743", key="member_search").strip()
    member_rows = selected.loc[selected["member_id"].str.contains(query, case=False, regex=False)] if query else selected
    display = member_rows[[
        "member_id", "plan_tier", "is_team_account", "lifetime_value", "utilization_rate",
        "n_services_used", "zero_999", "anomaly_flag", "anomaly_score",
    ]].copy()
    display["utilization_rate"] *= 100
    display = display.rename(columns={"utilization_rate": "utilization_pct"})
    st.dataframe(display, hide_index=True, width="stretch", height=330)
    st.caption(f"{len(member_rows):,} matching members. ID search narrows this table and download only; other indicators keep the sidebar selection.")
    if len(member_rows) == 1:
        row = member_rows.iloc[0]
        services = [name.removeprefix("uses_").replace("_", " ") for name in SERVICE_COLUMNS if row[name]]
        st.markdown("**Services recorded for this member:** " + (", ".join(services) if services else "None reported"))
    st.download_button(
        "Download these members as CSV", member_rows.to_csv(index=False).encode("utf-8"),
        file_name="ACDC_selected_members.csv", mime="text/csv", key="download_members",
    )

st.divider()
st.caption(
    "Revenue covers the whole membership; utilization covers the last membership period; service flags describe past use. "
    "These are descriptive comparisons. Dates and recency remain unresolved, so current activity and churn are not inferred. "
    "Anomaly labels come from the notebook's full scoring sample and are not refitted after filtering; unscored members have blank flags."
)
