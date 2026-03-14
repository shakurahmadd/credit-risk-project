# Credit Default Predictor

Predicts whether a credit card customer will default on their payment next month.
                                                                                            
**[Live Demo](https://credit-risk-project.onrender.com)**  

---                                                                                                                                           

### Overview

The project was built using the [UCI Default of Credit Card Clients dataset](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients), which contains data on 30,000 Taiwanese credit card holders with 23 features, including credit limit, repayment history, and bill/payment amounts. The target is binary: whether the customer defaulted in the following month.

---

### Approach:

EDA highlighted a 78/22 class imbalance and showed that repayment status features were the strongest predictors of default. Bill and payment amount features were heavily right-skewed with extreme outliers, so a Yeo-Johnson power transform was applied before scaling.

Three models were compared against a dummy baseline: Decision Trees, Random Forest, and XGBoost. The primary metric used was recall, since failing to identify a defaulter carries a higher cost than a false positive. Random Forest performed best and was therefore taken forward for hyperparameter tuning. `class_weight="balanced"` was used throughout to account for class imbalance.

Feature importance analysis highlighted several low-contribution features, which were removed with no impact on performance.

---

### Final Model Results

|Metric | Score |
|-------|-------|
| Recall | 0.61 |
|Precision | 0.51 | 
|F1 | 0.55|

---

### Tech Stack
Python · pandas · scikit-learn · XGBoost · Flask · Bootstrap 5 · Render

---

## Run Locally 

```bash
git clone https://github.com/shakurahmadd/credit-risk-project.git
cd credit-risk-project
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python src/app.py
```
Visit http://localhost:5000

---