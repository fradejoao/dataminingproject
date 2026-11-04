# ACDC Data Mining Project

Customer segmentation for Amazing Creative Desk Coworking (ACDC).

Data Mining, Nova IMS, 2026/2027.

[Exploratory analysis and feature engineering notebook](notebooks/Group21_EDA_Code.ipynb)

## Intermediate submission

The final submission files are in `delivery/`:

- [Group21_EDA_Code.ipynb](delivery/Group21_EDA_Code.ipynb)
- [Group21_EDA_Slides.pdf](delivery/Group21_EDA_Slides.pdf)

The [editable presentation](slides/Group21_EDA_Slides.pptx) is kept separately. The PDF contains the cover and five content slides. The 4 November core-delivery check reran the original 68 notebook code cells in a clean kernel, independently reproduced the numerical slide claims from the raw CSV, and inspected all six rendered slides. The presentation's sensitivity-chart rounding was aligned with the notebook table. A detailed local review record is retained in `.local/`, which is ignored by Git.

The notebook now includes both optional intermediate bonuses: multidimensional anomaly detection and a local interactive EDA dashboard. The existing PDF/PPTX retain the core presentation; [suggested bonus slide wording](slides/BONUS_SLIDE_NOTE.md), the [anomaly figure](slides/assets/Group21_Bonus_Anomalies.png) and a [dashboard screenshot](slides/assets/Group21_Dashboard.png) are supplied for the group to integrate within the five content slides.

The notebook includes the ACDC business context, documented data cleaning, distributions and relationships, comparisons within plans and account types, service-use patterns, recorded membership trends, and sensitivity to the flagged revenue pattern. Engineered features cover last-period plan utilization and the number of reported services used. Economic comparisons use observed nonnegative revenue, with coverage and exclusions reported explicitly. The closing sections assess candidate features and redundancy, state provisional profile hypotheses, and explain limitations to address before clustering.

## Optional anomaly bonus

The bonus uses Isolation Forest on log-transformed nonnegative revenue, utilization and service variety. It scores 14,318 members and flags 144 at a chosen 1% review budget. Of these, 66 also have the existing zero-revenue/recency-999 pattern. The analysis includes member profiles, a two-panel plot, example cases, threshold sensitivity and a second random seed. Flags are exploratory: all 15,450 members remain in the main dataset. This is an extension of the course's data-quality workflow; Isolation Forest goes beyond the Lab 06 IQR/manual examples. See the notebook for the method reference and limitations.

## Optional interactive dashboard bonus

The [Streamlit app](dashboard/app.py) lets users filter by current plan, account type and review cohort; explore revenue and utilization distributions; compare service-use proportions and plan summaries; find individual member IDs; and download the selected records. Indicators report their available sample sizes. Revenue summaries use observed nonnegative values, undefined ratios remain missing, and service percentages use all members in the selected group. Anomaly flags retain the notebook's original scoring scope, rather than being refitted after a filter.

Run all notebook cells first. The final dashboard section exports all 15,450 prepared members to the local, Git-ignored `data/processed/acdc_dashboard.csv`. This preserves the existing cleaning decisions and nullable anomaly flags. Regenerate it after updating the data or analysis. Then run these commands from the repository root:

```bash
python -m pip install -r requirements-dashboard.txt
python -m streamlit run dashboard/app.py
```

Open the local address printed by Streamlit, normally `http://localhost:8501`. The dataset stays local; the dashboard is not deployed to a public website. For a short demonstration, select Private Office, compare its revenue/utilization coverage, reset the filters, select Anomaly Review Candidates, then search a member ID in the second tab. Clearing all plans shows an empty-selection message.

Dashboard dependencies are pinned to the tested Streamlit 1.58.0 and Plotly 6.7.0. Data/interaction tests cover the full sample, plan/account intersections, service denominators, anomaly coverage, reset/empty selections, member lookup and revenue scale. To rerun them after exporting data:

```bash
python -m pip install pytest
python -m pytest tests/test_dashboard.py -q
```

## Files

- `notebooks/`: project analysis notebooks.
- `dashboard/`: interactive app and descriptive-data helpers.
- `slides/`: editable presentation.
- `delivery/`: final notebook and PDF for submission.
- `data/raw/`: original dataset, stored locally and ignored by Git.
- `requirements.txt`: Python dependencies.

## Setup

```bash
python -m pip install -r requirements.txt
python -m jupyterlab
```

Place `acdc_dataset.csv` in `data/raw/` before running the analysis.

Open `notebooks/Group21_EDA_Code.ipynb` in JupyterLab. Its relative data path assumes that the kernel working directory is `notebooks/`. Restart the kernel, run all cells and save the notebook to retain visible outputs.

All 76 code cells, including both bonuses, were executed successfully in a new virtual environment installed from the updated `requirements.txt` on 4 November 2026: Python 3.14.6, pandas 3.1.0, NumPy 2.5.4, scikit-learn 1.9.0 and Matplotlib 3.11.2. Outputs are saved in both notebook copies. Checks confirmed preservation of the main dataset and original analytical results, feature calculations, anomaly eligibility, score direction, profile summaries, threshold sensitivity and fixed-seed reproducibility. The dashboard export preserves every member and keeps 1,132 unscored anomaly flags missing. Matplotlib 3.10 or newer is required for the boxplot orientation argument. The tested scikit-learn version is pinned to support reproducing the anomaly results.

Group 21: João Frade (20260557), Alfredo Soudo (20260591), and Maria Coutinho (20260657). Profile hypotheses are provisional and do not represent fitted clusters.
