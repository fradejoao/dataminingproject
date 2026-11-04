# ACDC Data Mining Project

Customer segmentation for Amazing Creative Desk Coworking (ACDC).

Data Mining, Nova IMS, 2026/2027.

[Exploratory analysis and feature engineering notebook](notebooks/Group21_EDA_Code.ipynb)

## Intermediate submission

The final submission files are in `delivery/`:

- [Group21_EDA_Code.ipynb](delivery/Group21_EDA_Code.ipynb)
- [Group21_EDA_Slides.pdf](delivery/Group21_EDA_Slides.pdf)

The [editable presentation](slides/Group21_EDA_Slides.pptx) is kept separately. The PDF contains the cover and five content slides. The 4 November final check reran all 68 notebook code cells in a clean kernel, independently reproduced the numerical slide claims from the raw CSV, and inspected all six rendered slides. The presentation's sensitivity-chart rounding was aligned with the notebook table. A detailed local review record is retained in `.local/`, which is ignored by Git.

The notebook includes the ACDC business context, documented data cleaning, distributions and relationships, comparisons within plans and account types, service-use patterns, recorded membership trends, and sensitivity to the flagged revenue pattern. Engineered features cover last-period plan utilization and the number of reported services used. Economic comparisons use observed nonnegative revenue, with coverage and exclusions reported explicitly. The closing sections assess candidate features and redundancy, state provisional profile hypotheses, and explain limitations to address before clustering.

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

All 68 code cells were executed successfully in a new virtual environment installed from `requirements.txt` on 2 November 2026, using Python 3.14.6, pandas 3.1.0 and Matplotlib 3.11.2. Outputs are saved in the notebook. Checks confirmed member retention, revenue coverage, feature calculations, pairwise sample sizes, independently calculated rank correlations and the numerical claims in the conclusions. The original 66 cells retain the same text results. Matplotlib 3.10 or newer is required for the boxplot orientation argument.

Group 21: João Frade (20260557), Alfredo Soudo (20260591), and Maria Coutinho (20260657). Profile hypotheses are provisional and do not represent fitted clusters.
