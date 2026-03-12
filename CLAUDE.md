# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

A machine learning project to predict credit card payment default using the [UCI Default of Credit Card Clients dataset](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients) (30,000 rows, 23 features, binary target). Currently in Phase 0 (EDA). The project goal is to build a well-evaluated baseline model while developing good ML engineering habits.

## Environment setup

Python 3.9 with a `.venv` virtual environment. Activate with:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the notebook

```bash
jupyter lab notebooks/eda.ipynb
```

The notebook kernel uses the `.venv` interpreter. In VS Code, select the `.venv` Python interpreter for the notebook kernel.

## Dataset

Loaded via `ucimlrepo` (dataset ID 350) — no local raw file needed, it fetches from the UCI ML repository at runtime. The target column is `DEFAULT` (1 = defaulted, 0 = did not default).

Feature groups used throughout the project:
- **Basic info**: `LIMIT_BAL`, `SEX`, `EDUCATION`, `MARRIAGE`, `AGE`
- **Repayment status** (monthly): `PAY_0`, `PAY_2`–`PAY_6`
- **Bill statement amounts** (monthly): `BILL_AMT1`–`BILL_AMT6`
- **Previous payment amounts** (monthly): `PAY_AMT1`–`PAY_AMT6`

Original UCI column names (`X1`–`X23`, `Y`) are renamed to descriptive names at the start of the notebook. All new notebook cells should use the renamed column names.

## Project structure

- `notebooks/eda.ipynb` — primary working notebook (EDA and modelling)
- `data/raw/` — for any raw data files saved locally
- `data/processed/` — for cleaned/transformed data
- `src/` — Python modules (currently empty; utility functions will go here as the project progresses)
- `project_log.md` — session-by-session record of decisions and progress
