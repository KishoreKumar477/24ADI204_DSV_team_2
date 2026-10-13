# EDA Deep Dive: Univariate and Bivariate Analysis

## 1. Introduction
Exploratory Data Analysis (EDA) is used to understand the structure, patterns, distributions, and relationships present in a dataset. In this project, EDA was performed on the Telco Customer Churn dataset using Python visualization libraries.

---

## 2. Data Preparation
The `TotalCharges` column was converted from text to numeric format using Pandas. Invalid or empty values were converted to `NaN`, and the corresponding rows were removed before performing the analysis.

---

## 3. Univariate Analysis
Univariate analysis studies one variable at a time.

The following visualizations were created:
* **Histograms** for Tenure, Monthly Charges, and Total Charges to understand their distributions.
* **Boxplots** for the same numerical variables to observe their spread and potential outliers.
* **Bar charts** for Gender, Partner status, Dependents status, and Churn to understand the distribution of categorical variables.

These plots provide a simple view of the frequency, range, and distribution of individual features.

---

## 4. Bivariate Analysis
Bivariate analysis examines the relationship between two variables.

The project used:
* **Scatter plot** of Tenure vs Monthly Charges
* **Scatter plot** of Tenure vs Total Charges
* **Scatter plot** of Monthly Charges vs Total Charges
* **Boxplots** of numerical variables grouped by Churn
* **Countplots** for:
  * Gender vs Churn
  * Internet Service vs Churn
  * Contract Type vs Churn

The scatterplots were colored according to the Churn status, making it easier to visually compare customers who churned and those who did not.

---

## 5. Correlation Analysis
A correlation heatmap was created for numerical features using Pandas and Seaborn. It helps identify the strength and direction of relationships between numerical variables such as:
* Tenure
* Monthly Charges
* Total Charges

---

## 6. Tools Used
* **Python**
* **Pandas** — data loading and preprocessing
* **NumPy** — numerical operations
* **Matplotlib** — plotting
* **Seaborn** — statistical visualizations

---

## 7. Conclusion
EDA provided a clear understanding of the Telco Customer Churn dataset. Univariate analysis helped examine individual feature distributions, while bivariate analysis helped explore relationships between customer characteristics and churn. Histograms, boxplots, countplots, scatterplots, and a correlation heatmap were used to visualize the data and identify useful patterns for further analysis and machine-learning tasks.