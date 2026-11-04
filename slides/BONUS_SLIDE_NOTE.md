# Bonus addition for the existing five content slides

The notebook now includes the optional multidimensional anomaly analysis. The current PDF and PPTX still contain the previously reviewed core presentation. Integrate this short addition into an existing content slide, keeping the five-slide limit. Slide 5 can include it as a small final callout; the data-quality slide is another suitable location if it fits better.

## Suggested slide wording

**Bonus — Multidimensional anomaly review**

- Isolation Forest on value, utilization and service variety.
- **144 / 14,318 members flagged** using a chosen 1% review budget; **66** also have the zero-revenue/recency-999 pattern.
- **All members retained.** Flags are exploratory and sensitive to the random seed.

Optional visual: [Group21_Bonus_Anomalies.png](assets/Group21_Bonus_Anomalies.png). Use it only if it remains readable; the three short bullets can be sufficient for the existing slide, with the full plot available in the notebook.

## What to explain orally

We looked for unusual combinations across three dimensions, extending the earlier rules that checked individual values. The logarithm reduces revenue skew; no missing revenue or undefined utilization was filled for this exercise. The model scores 14,318 members while all 15,450 remain in the main dataset.

The flagged group has median revenue EUR 0, utilization 71.79% and five services, compared with EUR 892.14, 50.60% and one service among other scored members. These are separate medians, not a claim that every flagged person has that exact combination. Unusual high-value members can also be flagged.

The 1% cutoff is our review budget, not a discovered rate of errors. A second seed keeps 109 of the original 144 flags, so the exact shortlist changes. We retain members, inspect flags separately and propose sensitivity checks during later clustering. The exercise does not prove that any member should be removed.
