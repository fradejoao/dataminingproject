# ACDC — Data Mining Project 2026/2027

Customer segmentation for Amazing Creative Desk Coworking (ACDC), developed for the Data Mining course at Nova IMS.

The project studies customer value and usage behaviour, then develops and evaluates a segmentation that supports business decisions.

## Current stage

Planning and initial data reconnaissance for **Deliverable 1: Exploratory Data Analysis**, due **4 November 2026** according to the supplied project guidelines. The final submission time and discussion arrangements should be checked on Moodle.

The project notebook and slides will be developed next. This repository is a starting structure, not a completed submission.

- [Work plan and deliverable checklist](docs/PLANO_ENTREGA_1.md)
- [Course materials and methods covered](docs/MAPA_MATERIAIS.md)
- [Initial dataset audit](docs/AUDITORIA_INICIAL.md)
- [AI assistance log](docs/AI_USAGE.md)

## Repository structure

```text
data/raw/          Original CSV, stored locally and ignored by Git
data/processed/    Derived datasets, stored locally and ignored by Git
docs/              Planning, sources, decisions and assistance log
notebooks/         Project analysis notebooks
```

## Local setup

Use Python and a virtual environment. The initial dependency list follows the tools used in class; an executed project notebook and tested version information will be added as the analysis develops.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m jupyterlab
```

Place the supplied `acdc_dataset.csv` in `data/raw/`. It is semicolon-delimited. From a notebook in `notebooks/`, the intended import is:

```python
import pandas as pd

df_raw = pd.read_csv("../data/raw/acdc_dataset.csv", sep=";")
df = df_raw.copy()
```

The original CSV, teaching PDFs and teaching notebooks are not distributed in this public repository. The course materials remain available through the [instructor's repository](https://github.com/anacaleiro/Data-Mining-26-27).

## Submission names

The guidelines specify submission filenames, not a mandatory GitHub repository name. Replace `XX` with the actual Moodle group number:

- `GroupXX_EDA_Code.ipynb`
- `GroupXX_EDA_Slides.pdf`

Contributors, group number, analyses and final conclusions will be recorded as the group develops and reviews the work.
