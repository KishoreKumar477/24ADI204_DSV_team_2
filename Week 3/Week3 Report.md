# Handling Missing Values and Outlier Detection

## 1. Introduction
Data cleaning is an important step in the Data Science process. In this project, the Telco Customer Churn dataset was cleaned by identifying missing values and detecting possible outliers. Python libraries such as Pandas, NumPy, Matplotlib, Seaborn, and Scikit-learn were used.

---

## 2. Dataset
The project uses the Telco Customer Churn dataset. The dataset contains customer-related information such as:
* Gender
* Tenure
* Monthly Charges
* Total Charges
* Internet Service
* Contract
* Payment Method

The original dataset was intentionally treated as an uncleaned dataset to demonstrate the data-cleaning process.

---

## 3. Handling Missing Values
First, missing values were identified using:
```python
data.isnull().sum()
```

The `TotalCharges` column was converted into numeric format. Invalid values were converted into missing values using `errors='coerce'`.

For numerical columns, median imputation was used:
* **MonthlyCharges** → median value
* **TotalCharges** → median value

For categorical columns, mode imputation was used:
* **Gender**
* **InternetService**
* **Contract**
* **PaymentMethod**

After imputation, the missing values were checked again to confirm that the dataset was cleaned.

---

## 4. Outlier Detection
Outliers were examined using boxplots for:
* Tenure
* Monthly Charges
* Total Charges

Boxplots help identify observations that are unusually far from the normal range.

The project also used Z-score standardization with `StandardScaler`. The numerical columns were standardized so that their values were centered around zero with a standard deviation of one:

$$Z = \frac{X - \mu}{\sigma}$$

A filtering condition was then applied to retain values between approximately $-3$ and $+3$, which is a common Z-score-based approach for identifying extreme observations.

---

## 5. Data Cleaning Workflow
The overall workflow was:

$$\text{Uncleaned Dataset} \rightarrow \text{Check Missing Values} \rightarrow \text{Convert Data Types} \rightarrow \text{Impute Missing Values} \rightarrow \text{Check Missing Values Again} \rightarrow \text{Visualize Outliers} \rightarrow \text{Z-score Detection} \rightarrow \text{Cleaned Dataset}$$

---

## 6. Tools Used
* **Python**
* **Pandas** — data loading and cleaning
* **NumPy** — numerical operations
* **Matplotlib** — visualization
* **Seaborn** — boxplots
* **Scikit-learn** — scaling and standardization

---

## 7. Conclusion
The Cleaning Sprint improved the quality of the Telco Customer Churn dataset by handling missing values and identifying potential outliers. Median imputation was used for numerical data and mode imputation for categorical data. Boxplots and Z-score-based filtering were used for outlier detection. The cleaned dataset can now be used for further analysis and machine-learning tasks such as customer churn prediction.