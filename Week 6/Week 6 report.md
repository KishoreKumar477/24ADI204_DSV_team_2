# Feature Engineering Report: Telco Customer Churn

Based on the pipeline executed in the notebook, this report documents the end-to-end preprocessing steps: categorical variable encoding, skewness remediation, normalization, and standardization.

---

## 1. Data Cleaning & Preparation

The raw dataset contains whitespace characters in numeric fields and unique identifier columns that need to be resolved prior to transformation.

* **ID Removal:** The `customerID` feature was dropped to prevent data leakage and noise.
* **Whitespace Treatment:** Rows containing blank spaces (`' '`) in the `TotalCharges` field were mapped to the preceding valid row's value and cast to `float64`.

```python
# Cleaning routine
l1 = [len(i.split()) for i in data['TotalCharges']]
l2 = [i for i in range(len(l1)) if l1[i] != 1]
for i in l2:
    data.loc[i, 'TotalCharges'] = data.loc[(i - 1), 'TotalCharges']

data['TotalCharges'] = data['TotalCharges'].astype(float)
data.drop(columns=['customerID'], inplace=True)
```

---

## 2. Categorical Variable Encoding

Categorical text features were mapped to discrete integers using Scikit-Learn's `LabelEncoder`.

### Encoded Dataset (First 5 Rows)

| Index | gender | SeniorCitizen | Partner | Dependents | tenure | PhoneService | MultipleLines | InternetService | OnlineSecurity | OnlineBackup | DeviceProtection | TechSupport | StreamingTV | StreamingMovies | Contract | PaperlessBilling | PaymentMethod | MonthlyCharges | TotalCharges | Churn |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **0** | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 29.85 | 29.85 | 0 |
| **1** | 1 | 0 | 0 | 0 | 34 | 1 | 0 | 0 | 2 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 3 | 56.95 | 1889.50 | 0 |
| **2** | 1 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 53.85 | 108.15 | 1 |
| **3** | 1 | 0 | 0 | 0 | 45 | 0 | 1 | 0 | 2 | 0 | 2 | 2 | 0 | 0 | 1 | 0 | 0 | 42.30 | 1840.75 | 0 |
| **4** | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 70.70 | 151.65 | 1 |

---

## 3. Fixing Skewness

To stabilize variance across continuous variables, a natural logarithmic transformation $\log(1 + x)$ was applied to `tenure`, `MonthlyCharges`, and `TotalCharges`.

### Skewness Metrics

| Feature | Skewness Before | Skewness After ($\log(1+x)$) | Delta / Shift |
|:---|:---:|:---:|:---|
| **tenure** | $0.2395$ | $-0.7784$ | Slight positive $\rightarrow$ Moderate negative |
| **MonthlyCharges** | $-0.2205$ | $-0.7190$ | Slight negative $\rightarrow$ Moderate negative |
| **TotalCharges** | $0.9596$ | $-0.7434$ | Substantial reduction of high positive skew ($+0.96 \rightarrow -0.74$) |

---

## 4. Normalization (MinMaxScaler)

Min-Max Scaling normalizes features into a fixed range of $[0, 1]$ according to the formula:

$$X_{\text{norm}} = \frac{X - X_{\min}}{X_{\max} - X_{\min}}$$

### Output Snapshot (First 5 Rows)

| Index | tenure | MonthlyCharges | TotalCharges |
|:---:|:---:|:---:|:---:|
| **0** | 0.161555 | 0.258016 | 0.072892 |
| **1** | 0.828664 | 0.602917 | 0.749358 |
| **2** | 0.256059 | 0.572840 | 0.280590 |
| **3** | 0.892362 | 0.443484 | 0.745063 |
| **4** | 0.256059 | 0.719396 | 0.335724 |

---

## 5. Scaling (StandardScaler)

Standardization centers numerical distributions around a mean of $0$ with unit standard deviation:

$$Z = \frac{X - \mu}{\sigma}$$

### Output Snapshot (First 5 Rows)

| Index | tenure | MonthlyCharges | TotalCharges |
|:---:|:---:|:---:|:---:|
| **0** | -2.028448 | -1.058533 | -2.273677 |
| **1** | 0.448730 | 0.027978 | 0.388137 |
| **2** | -1.677526 | -0.066772 | -1.456410 |
| **3** | 0.685260 | -0.474271 | 0.371239 |
| **4** | -1.677526 | 0.394908 | -1.239462 |