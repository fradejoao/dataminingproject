"""Read the notebook export and calculate descriptive summaries without cleaning again."""

from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_PATH = ROOT / "data/processed/acdc_dashboard.csv"
PLAN_ORDER = ["hot_desk", "flex", "dedicated_desk", "full_time", "private_office", "unknown"]
SERVICE_COLUMNS = [
    "uses_meeting_rooms", "uses_event_space", "uses_guest_passes", "uses_print",
    "uses_mail_handling", "uses_phone_booths", "uses_day_passes", "uses_storage",
    "uses_bike_locker",
]
REVIEW_COHORTS = [
    "All members", "Zero revenue / recency 999", "Anomaly review candidates",
    "Not scored for anomalies",
]
NUMERIC_COLUMNS = [
    "age", "avg_weekly_visits", "total_visits", "lifetime_value",
    "utilization_rate", "n_services_used", "anomaly_score",
]


def load_snapshot(path=SNAPSHOT_PATH):
    """Load the local notebook export, preserving undefined values and boolean flags."""
    boolean_columns = SERVICE_COLUMNS + ["is_team_account", "zero_999", "anomaly_flag"]
    frame = pd.read_csv(path, dtype={name: "boolean" for name in boolean_columns})
    required = set(NUMERIC_COLUMNS + boolean_columns + ["member_id", "plan_tier", "industry"])
    if not required.issubset(frame.columns):
        raise ValueError("The notebook export is incomplete. Run the dashboard export cell again.")
    if frame.empty or frame["member_id"].isna().any() or frame["member_id"].duplicated().any():
        raise ValueError("The notebook export must contain unique, nonmissing member IDs.")
    if frame[SERVICE_COLUMNS + ["is_team_account", "zero_999"]].isna().any().any():
        raise ValueError("Required descriptive flags are missing in the notebook export.")
    for column in NUMERIC_COLUMNS:
        frame[column] = pd.to_numeric(frame[column], errors="raise")
    if not frame["n_services_used"].eq(frame[SERVICE_COLUMNS].sum(axis=1)).all():
        raise ValueError("Service counts differ from the nine original flags. Regenerate the export.")
    if not frame["anomaly_flag"].notna().equals(frame["anomaly_score"].notna()):
        raise ValueError("Anomaly coverage is inconsistent. Regenerate the export.")
    return frame


def filter_members(frame, plans, account="All accounts", cohort="All members"):
    """Apply conjunctive filters; an empty plan selection deliberately selects no members."""
    mask = frame["plan_tier"].isin(plans)
    if account == "Individual":
        mask &= ~frame["is_team_account"]
    elif account == "Team":
        mask &= frame["is_team_account"]
    elif account != "All accounts":
        raise ValueError("Unknown account filter.")
    if cohort == "Zero revenue / recency 999":
        mask &= frame["zero_999"]
    elif cohort == "Anomaly review candidates":
        mask &= frame["anomaly_flag"].fillna(False)
    elif cohort == "Not scored for anomalies":
        mask &= frame["anomaly_score"].isna()
    elif cohort != "All members":
        raise ValueError("Unknown review filter.")
    return frame.loc[mask].copy()


def summary_metrics(frame):
    """Keep member counts, economic coverage and utilization coverage distinct."""
    revenue = frame.loc[frame["lifetime_value"] >= 0, "lifetime_value"]
    utilization = frame["utilization_rate"].dropna()
    return {
        "members": len(frame),
        "revenue_n": len(revenue),
        "median_revenue": np.round(revenue.median(), 2),
        "utilization_n": len(utilization),
        "median_utilization_pct": np.round(100 * utilization.median(), 2),
        "median_services": frame["n_services_used"].median(),
        "missing_revenue": int(frame["lifetime_value"].isna().sum()),
        "negative_revenue": int((frame["lifetime_value"] < 0).sum()),
        "zero_999": int(frame["zero_999"].sum()),
        "anomaly_scored": int(frame["anomaly_score"].notna().sum()),
        "anomaly_flagged": int(frame["anomaly_flag"].fillna(False).sum()),
    }


def service_rates(frame):
    """Each service percentage uses all selected members as its denominator."""
    return pd.DataFrame({
        "Service": [name.removeprefix("uses_").replace("_", " ").title() for name in SERVICE_COLUMNS],
        "Members (%)": frame[SERVICE_COLUMNS].mean().to_numpy(dtype=float) * 100,
    }).sort_values("Members (%)")


def plan_summary(frame):
    """Separate medians by plan, with the number of observations for each measure."""
    view = frame.assign(
        economic_revenue=frame["lifetime_value"].where(frame["lifetime_value"] >= 0),
        utilization_pct=100 * frame["utilization_rate"],
    )
    result = view.groupby("plan_tier").agg(
        members=("member_id", "size"),
        revenue_observations=("economic_revenue", "count"),
        median_revenue_eur=("economic_revenue", "median"),
        utilization_observations=("utilization_pct", "count"),
        median_utilization_pct=("utilization_pct", "median"),
        median_services=("n_services_used", "median"),
    )
    return result.reindex([p for p in PLAN_ORDER if p in result.index]).round(2)
