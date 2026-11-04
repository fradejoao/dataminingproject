# ACDC Data Mining Project

Customer segmentation for Amazing Creative Desk Coworking (ACDC).

Data Mining, Nova IMS, 2026/2027.

[Exploratory analysis and feature engineering notebook](notebooks/Group21_EDA_Code.ipynb)

## Intermediate submission

The final submission files are in `delivery/`:

- [Group21_EDA_Code.ipynb](delivery/Group21_EDA_Code.ipynb)
- [Group21_EDA_Slides.pdf](delivery/Group21_EDA_Slides.pdf)

The [editable presentation](slides/Group21_EDA_Slides.pptx) is kept separately. The PDF contains the cover and five content slides. The 4 November core-delivery check reran the original 68 notebook code cells in a clean kernel, independently reproduced the numerical slide claims from the raw CSV, and inspected all six rendered slides. The presentation's sensitivity-chart rounding was aligned with the notebook table. A detailed local review record is retained in `.local/`, which is ignored by Git.

The notebook now also includes an optional multidimensional anomaly bonus. The existing PDF/PPTX retain the core presentation; [suggested bonus slide wording](slides/BONUS_SLIDE_NOTE.md) and the [bonus figure](slides/assets/Group21_Bonus_Anomalies.png) are supplied for the group to integrate within the five content slides.

The notebook includes the ACDC business context, documented data cleaning, distributions and relationships, comparisons within plans and account types, service-use patterns, recorded membership trends, and sensitivity to the flagged revenue pattern. Engineered features cover last-period plan utilization and the number of reported services used. Economic comparisons use observed nonnegative revenue, with coverage and exclusions reported explicitly. The closing sections assess candidate features and redundancy, state provisional profile hypotheses, and explain limitations to address before clustering.

## Optional anomaly bonus

The bonus uses Isolation Forest on log-transformed nonnegative revenue, utilization and service variety. It scores 14,318 members and flags 144 at a chosen 1% review budget. Of these, 66 also have the existing zero-revenue/recency-999 pattern. The analysis includes member profiles, a two-panel plot, example cases, threshold sensitivity and a second random seed. Flags are exploratory: all 15,450 members remain in the main dataset. This is an extension of the course's data-quality workflow; Isolation Forest goes beyond the Lab 06 IQR/manual examples. See the notebook for the method reference and limitations.

## Files

- `notebooks/`: project analysis notebooks.
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

All 75 code cells, including the bonus, were executed successfully in a new virtual environment installed from the updated `requirements.txt` on 4 November 2026: Python 3.14.6, pandas 3.1.0, NumPy 2.5.4, scikit-learn 1.9.0 and Matplotlib 3.11.2. Outputs are saved in both notebook copies. Checks confirmed preservation of the main dataset and original analytical results, feature calculations, anomaly eligibility, score direction, profile summaries, threshold sensitivity and fixed-seed reproducibility. Matplotlib 3.10 or newer is required for the boxplot orientation argument. The tested scikit-learn version is pinned to support reproducing the anomaly results.

Group 21: João Frade (20260557), Alfredo Soudo (20260591), and Maria Coutinho (20260657). Profile hypotheses are provisional and do not represent fitted clusters.
