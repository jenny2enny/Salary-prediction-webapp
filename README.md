# Workers Salary Prediction Model

Welcome to the Workers Salary Prediction Model project! This repository contains a notebook and related materials to build, analyze, and visualize a machine learning model for predicting workers' salaries based on various features.

---

## Project Overview

The goal of this project is to create a robust and interpretable model to predict worker salaries using relevant features such as age, gender, education level, job title, and years of experience. The workflow includes data cleaning, exploratory data analysis (EDA), visualization, feature engineering, model building, and evaluation.

---

## Files

- **sal.ipynb** — Main Jupyter Notebook for the entire workflow; includes code, EDA, visualizations, and model training.

---

## Dataset

**Features:**
- Age
- Gender
- Education Level (`Bachelor's`, `Master's`, `PhD`)
- Job Title
- Years of Experience
- Salary (Target variable)

The dataset is expected in a CSV file named `Salary Data.csv`. The notebook reads and processes this file.

---

## Workflow Steps

1. **Import Libraries**
   - pandas, numpy, seaborn, scikit-learn, pickle, etc.

2. **Load Data**
   - Reads `Salary Data.csv` and displays the head of the dataset.

3. **Data Cleaning**
   - Drops missing values and duplicates.

4. **Exploratory Data Analysis (EDA)**
   - Statistical summary of numerical features.
   - Value counts for categorical features (Gender, Education Level, Job Title).
   - Visualization:
     - Barplot: Education Level vs Salary
     - Barplot: Gender vs Salary (with Education Level hue)
     - Scatterplot: Job Title vs Salary
     - Lineplot: Years of Experience vs Salary (with Education Level hue)
     - Lineplot: Age vs Salary

5. **Feature Engineering**
   - OneHotEncoder for categorical features.
   - Preprocessing pipeline with scikit-learn.

6. **Model Building**
   - Train-test split.
   - Linear Regression model.
   - Evaluation metrics: RMSE, MAE, R² score.

7. **Model Export**
   - Trained model is saved using pickle for later use.

---

## Visualization

Various plots are generated to analyze the relationship between salary and other features. These include:

- **Barplots** for categorical variables like Education Level and Gender.
- **Scatterplots** for Job Title vs Salary.
- **Lineplots** for Years of Experience and Age vs Salary.

---

## How to Run

1. Place `Salary Data.csv` in the same directory as the notebook.
2. Open `sal.ipynb` in Jupyter Notebook or JupyterLab.
3. Step through the notebook, executing cells sequentially.
4. Examine visualizations and model metrics.

---

## Requirements

- Python (recommended: 3.7+)
- Jupyter Notebook
- pandas, numpy, seaborn, scikit-learn, matplotlib, pickle

You can install dependencies using pip:

```bash
pip install pandas numpy seaborn scikit-learn matplotlib
```

---

## Results & Insights

- The notebook provides a comprehensive analysis of the data and highlights key salary determinants.
- Visualizations reveal trends and patterns (e.g., higher education/experience correlating with higher salaries).
- The model's performance is evaluated using standard regression metrics.

---

## License

This project is licensed under the MIT License.

---

## Author

Developed by [IdogaEne Jennifer]

---

## Acknowledgements

- scikit-learn for machine learning utilities.
- matplotlib & seaborn for visualization.
- pandas for data wrangling.

---
