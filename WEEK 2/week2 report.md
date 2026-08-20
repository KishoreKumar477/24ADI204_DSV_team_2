# Data Representation & Preprocessing Report

### 1. Dataset Overview
*   **Source Dataset:** [Blastchar/Telco-Customer-Churn](https://colab.research.google.com/drive/1WNTwbYnSTDmPtC1mLN_3RLO3940W6L38?usp=sharing)
*   **Initial Shape:** 7,043 rows and 21 columns.
*   **Objective:** Predict customer churn (binary classification: `Yes` or `No`).
*   **Initial Data Types:** 18 `object` (categorical/text), 2 `int64`, and 1 `float64`.

### 2. Data Cleaning & Transformation
*   **Handling Missing/Anomalous Data:** The `TotalCharges` column contained empty spaces for 11 index positions. These were handled by forward-filling values from the previous rows, and the column was subsequently converted to a `float` datatype. 
*   **Irrelevant Features:** The `customerID` column was dropped as it holds no predictive value.
*   **Categorical Encoding:** `LabelEncoder` was applied to transform text-based categorical features into numerical formats.
*   **Feature Scaling:** `MinMaxScaler` was applied to the numerical features (`tenure`, `MonthlyCharges`, and `TotalCharges`) to normalize their distributions between 0 and 1.

### 3. Feature Categorization & Selection
The features were initially split into logical groups for visualization:
*   **Numerical Features:** `tenure`, `MonthlyCharges`, `TotalCharges`
*   **Categorical Features:** `gender`, `SeniorCitizen`, `Partner`, `Dependents`, `PhoneService`, `MultipleLines`, `InternetService`, `OnlineSecurity`, `OnlineBackup`, `DeviceProtection`, `TechSupport`, `StreamingTV`, `StreamingMovies`, `Contract`, `PaperlessBilling`, `PaymentMethod`.

**Feature Selection Process:**
*   `SelectKBest` was used to evaluate feature importance. 
*   **Chi-Squared (Chi2)** was used for categorical feature selection.
*   **ANOVA (f_classif)** was used for numerical feature selection.
*   **Features Dropped:** Based on the statistical scores, the following features were deemed less impactful and removed from the final dataset: `PhoneService`, `gender`, `StreamingTV`, `StreamingMovies`, `MultipleLines`, and `InternetService`.

### 4. Target Variable & Data Balancing
*   **Initial Imbalance:** The target variable (`Churn`) was significantly imbalanced, with a mean of 0.27 (meaning ~27% of the dataset represented churned customers, while ~73% were retained).
*   **Balancing Technique:** **SMOTE** (Synthetic Minority Over-sampling Technique) was applied with a `sampling_strategy=1` to generate synthetic samples for the minority class.
*   **Final Data Distribution:** After applying SMOTE, the target classes were perfectly balanced, resulting in **5,174** instances of non-churned (0) customers and **5,174** instances of churned (1) customers.

*[Colab Notebook Link](https://colab.research.google.com/drive/1WNTwbYnSTDmPtC1mLN_3RLO3940W6L38#scrollTo=QaCWhv7-bXpO)

