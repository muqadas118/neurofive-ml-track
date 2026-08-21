# Titanic Survival Prediction - Machine Learning Fundamentals

## Overview

This project is part of my Machine Learning Fundamentals Internship at Neurofive Solutions.

The goal of this project is to predict whether a passenger survived the Titanic disaster using Machine Learning. The project covers the complete beginner ML workflow including data exploration, data cleaning, visualization, feature encoding, model training, and evaluation.

## Dataset

* Dataset: Titanic - Machine Learning from Disaster
* Source: Kaggle
* Target Variable: `Survived`

  * 0 = Did Not Survive
  * 1 = Survived

## Tasks Performed

### Task 1: Exploratory Data Analysis (EDA)

* Loaded the dataset using Pandas
* Inspected dataset structure using:

  * `head()`
  * `info()`
  * `describe()`
* Identified numerical and categorical features
* Checked dataset dimensions and missing values

### Task 2: Data Cleaning & Visualization

* Handled missing values
* Removed the `Cabin` column due to a large number of missing values
* Created visualizations using Matplotlib and Seaborn:

  * Histogram
  * Boxplot
  * Bar Chart
  * Correlation Heatmap
* Detected outliers using a boxplot

### Task 3: Machine Learning Model

* Encoded categorical variables using `pd.get_dummies()`
* Split the dataset into training and testing sets using `train_test_split`
* Trained a Logistic Regression model
* Evaluated model performance using:

  * Accuracy Score
  * Confusion Matrix

## Model Performance

**Algorithm:** Logistic Regression

**Accuracy:** 80.45%

**Confusion Matrix:**

```text
[[89 16]
 [19 55]]
```

The model correctly classified most passengers and achieved over 80% accuracy on the test dataset.

## Task 4 – House Price Prediction using Linear Regression

* Used California Housing Dataset
* Selected important housing features
* Trained a Linear Regression model
* Evaluated performance using RMSE and R² Score
* Visualized Actual vs Predicted Prices

## Results:

RMSE: 0.81
R² Score: 0.499

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

## Learning Outcomes

Through this project, I learned:

* Data cleaning techniques
* Handling missing values
* Data visualization
* Feature encoding
* Classification using Logistic Regression
* Model evaluation using accuracy score and confusion matrix

## Task 8 – Ensemble Learning

For this task, I compared ensemble models with the earlier Logistic Regression model for customer churn prediction.

### Models Compared

| Model | Accuracy |
|---|---:|
| Logistic Regression | 72.57% |
| Random Forest | 75.41% |
| XGBoost | 79.32% |

### Feature Importance

Random Forest and XGBoost were also used to identify the most important churn-related features.

**Random Forest top features:**
1. Contract - Month-to-month
2. Tenure
3. TenureYears

**XGBoost top features:**
1. Contract - Month-to-month
2. InternetService - Fiber optic
3. OnlineSecurity - No

Both ensemble models identified month-to-month contracts as an important churn factor.

### How Random Forest and XGBoost Differ

Random Forest builds many decision trees independently and combines their predictions to reduce variance and improve stability. XGBoost builds trees sequentially, with each new tree focusing on errors made by previous trees. Because of this boosting approach, XGBoost can learn more complex patterns. In this task, XGBoost achieved the highest accuracy among the three models.

### Result

XGBoost performed best with an accuracy of **79.32%**, followed by Random Forest at **75.41%** and Logistic Regression at **72.57%**.

## Author

Muqadas Rehman

Machine Learning Fundamentals Intern
