# ACDC Data Mining Project

Customer segmentation for Amazing Creative Desk Coworking (ACDC).

Data Mining, Nova IMS, 2026/2027.

[Exploratory analysis and feature engineering notebook](notebooks/GroupXX_EDA_Code.ipynb)

The notebook includes documented data cleaning, distributions and relationships, comparisons within plans and account types, service-use patterns, recorded membership trends, and sensitivity to the flagged revenue pattern. Engineered features cover last-period plan utilization and the number of reported services used. Economic comparisons use observed nonnegative revenue, with coverage and exclusions reported explicitly.

## Files

- `notebooks/`: project analysis notebooks.
- `data/raw/`: original dataset, stored locally and ignored by Git.
- `requirements.txt`: Python dependencies.

## Setup

```bash
python -m pip install -r requirements.txt
python -m jupyterlab
```

Place `acdc_dataset.csv` in `data/raw/` before running the analysis.

Open `notebooks/GroupXX_EDA_Code.ipynb` in JupyterLab. Its relative data path assumes that the kernel working directory is `notebooks/`. Restart the kernel, run all cells and save the notebook to retain visible outputs.

The 66 code cells were executed successfully in the existing `ProjetoDM` environment with Python 3.12.15, pandas 3.0.6 and Matplotlib 3.11.2. Integration checks confirmed member retention, revenue coverage, undefined utilization cases and the use of all nine original service flags. A fresh dependency installation has not yet been verified. Matplotlib 3.10 or newer is required for the boxplot orientation argument.
