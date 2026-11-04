# Bonus additions for the existing five content slides

The notebook now includes both optional intermediate bonuses. The current PDF and PPTX still contain the previously reviewed core presentation. Integrate these short additions into existing content slides, keeping the five-slide limit. Slide 5 can include a compact callout; the data-quality slide is another suitable location for the anomaly summary.

Updated [notebook figures](assets/notebook/) use white backgrounds without grids and stronger colors, as requested by the instructor. Replace the relevant embedded plot images in the current slides; the PNG changes do not update the PPTX automatically.

## Suggested combined callout

**Optional bonuses: anomaly review + interactive EDA**

- Isolation Forest: **144 / 14,318** members flagged at a chosen 1% review budget; all members retained.
- Interactive dashboard: filters by plan, account type and review cohort; distributions, service comparisons and member drill-down.
- Available sample sizes remain visible; source code and launch instructions are in the project repository.

Screenshot: [Group21_Dashboard.png](assets/Group21_Dashboard.png). A small screenshot can accompany the dashboard bullet if space allows. Avoid making the plots unreadably small just to include a screenshot.

What to say: "We added a local interactive tool so stakeholders can explore the same prepared data themselves. Filters update the indicators, charts and tables, while revenue and utilization show their actual coverage. We can inspect flagged cases without deleting members."

For a live demonstration, run all notebook cells and start `python -m streamlit run dashboard/app.py` from the repository root after installing `requirements-dashboard.txt`. Select Private Office to illustrate different revenue/utilization patterns, reset, and select Anomaly Review Candidates. Do not present the local address as a publicly hosted link; cite the GitHub source and README for reproduction.

## Anomaly-only slide wording

**Bonus — Multidimensional anomaly review**

- Isolation Forest on value, utilization and service variety.
- **144 / 14,318 members flagged** using a chosen 1% review budget; **66** also have the zero-revenue/recency-999 pattern.
- **All members retained.** Flags are exploratory and sensitive to the random seed.

Optional visual: [Group21_Bonus_Anomalies.png](assets/Group21_Bonus_Anomalies.png). Use it only if it remains readable; the three short bullets can be sufficient for the existing slide, with the full plot available in the notebook.

## What to explain orally

We looked for unusual combinations across three dimensions, extending the earlier rules that checked individual values. The logarithm reduces revenue skew; no missing revenue or undefined utilization was filled for this exercise. The model scores 14,318 members while all 15,450 remain in the main dataset.

The flagged group has median revenue EUR 0, utilization 71.79% and five services, compared with EUR 892.14, 50.60% and one service among other scored members. These are separate medians, not a claim that every flagged person has that exact combination. Unusual high-value members can also be flagged.

The 1% cutoff is our review budget, not a discovered rate of errors. A second seed keeps 109 of the original 144 flags, so the exact shortlist changes. We retain members, inspect flags separately and propose sensitivity checks during later clustering. The exercise does not prove that any member should be removed.
