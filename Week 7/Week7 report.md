# Dimensionality Reduction & Feature Selection Report: Telco Churn

This report covers the feature selection process, Principal Component Analysis (PCA) configuration, and variance breakdown directly corresponding to your Colab workspace pipeline.

---

## 1. Feature Selection

Feature selection was implemented using univariate statistical tests against the target variable (`Churn`) to remove non-informative features prior to dimensionality reduction and modeling.

### Categorical Feature Selection ($\chi^2$ Test)
* **Method:** `SelectKBest(score_func=chi2, k='all')`
* **Features Dropped:** `PhoneService`, `gender`, `StreamingTV`, `StreamingMovies`, `MultipleLines`, `InternetService`.
* **Rationale:** Low relative chi-square scores indicated minimal statistical dependency with customer churn compared to top indicators like `Contract` and `OnlineSecurity`.

### Numerical Feature Selection (ANOVA F-Test)
* **Method:** `SelectKBest(score_func=f_classif, k='all')`
* **Features Evaluated:** `tenure`, `MonthlyCharges`, `TotalCharges` (all demonstrated statistically significant F-scores and were retained).

---

## 2. Principal Component Analysis (PCA)

PCA was executed on the normalized 13-feature subset (`SeniorCitizen`, `Partner`, `Dependents`, `tenure`, `OnlineSecurity`, `OnlineBackup`, `DeviceProtection`, `TechSupport`, `Contract`, `PaperlessBilling`, `PaymentMethod`, `MonthlyCharges`, `TotalCharges`).

### Explained Variance Breakdown

| Principal Component | Variance Explained | Cumulative Variance |
|:---:|:---:|:---:|
| **PC1** | 30.64% | 30.64% |
| **PC2** | 17.03% | 47.67% |
| **PC3** | 11.01% | 58.68% |
| **PC4** | 10.57% | 69.25% |
| **PC5** | 8.75% | 78.00% |
| **PC6** | 6.75% | 84.75% |
| **PC7** | 4.63% | 89.37% |
| **PC8** | 4.23% | 93.60% |
| **PC9** | 2.54% | **96.15%** |
| **PC10** | 1.65% | 97.79% |
| **PC11** | 1.47% | 99.27% |
| **PC12** | 0.65% | 99.92% |
| **PC13** | 0.08% | 100.00% |

---

## 3. Dimensionality Reduction Summary

* **Original Feature Space:** 13 features
* **Components Required for $\ge$95% Variance:** 9 components (capturing **96.15%** of total variance)
* **Dimensionality Compression Ratio:** **30.8%** reduction ($13 \rightarrow 9$ dimensions)
* **Top 2 Components Coverage:** PC1 and PC2 jointly capture **47.67%** of the dataset variance in 2D space.