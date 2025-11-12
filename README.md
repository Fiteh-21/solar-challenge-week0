# Solar Challenge Project

A comprehensive data science project focused on analyzing and comparing solar energy potential across West African countries: Benin, Sierra Leone, and Togo. The project spans environment setup, data profiling and cleaning, exploratory data analysis (EDA), cross-country comparison, and an interactive dashboard for visualization.

 ## 🚀 Project Overview

This repository contains a multi-phase solar energy analysis to evaluate solar irradiance data, extract meaningful insights, and support decision-making for solar energy initiatives. It emphasizes reproducibility, collaboration, and clean coding practices.

 ## 🚀 Environment Setup Instructions
 ### 1 Clone the Repository
 git clone https://github.com/Fiteh-21/solar-challenge-week0.git
 cd solar-challenge-week0
 ### 2 Create and Activate Virtual Environment
 For Windows CMD:
 - python -m venv venv
 - venv\Scripts\activate
 
 For macOS/Linux:
 - python3 -m venv venv
 - source venv/bin/activate
 ### 3 Install Dependencies
 pip install -r requirements.txt
 ### 4 Verify Python and Pip
 python --version
 
 pip --version
 ### 5 Run Tests (Optional)
 python -m unittest
 ## 📁Suggested Folder Structure
.vscode/
   -  settings.json
    
.github/
   -  workflows/
       -  unittest.yml
        
 .gitignore
 
requirements.txt

README.md

 src/
 
 notebooks/
   -  __init__.py
   -  README.md
   -  <country>_eda.ipynb
    
 tests/
   -  __init__.py
    
 scripts/
   -  __init__.py
   -  README.md

 app/
    - init.py
    - main.py
    - utils.py
    
## 📌 Project Tasks and Milestones

### Task 1: Git & Environment Setup

Initialize the repository and set up Python virtual environment.

Create branch setup-task for environment setup.

Add .gitignore (ignoring data/ and .csv files).

Add requirements.txt.

Add GitHub Actions workflow (.github/workflows/ci.yml) for continuous integration, running pip install and verifying Python version.

Commit with clear messages (e.g., init: add .gitignore, chore: venv setup, ci: add GitHub Actions workflow).

Merge setup-task into main via Pull Request.

### Task 2: Data Profiling, Cleaning & Exploratory Data Analysis (EDA)

Create branches eda-benin, eda-sierraleone, eda-togo.

Perform detailed EDA on solar datasets for each country:

Summary statistics and missing value reports.

Outlier detection using Z-scores (|Z| > 3) on key variables like GHI, DNI, DHI, ModA, ModB, WS, WSgust.

Handle missing values by dropping or imputing median values.

Visualize time series of solar irradiance and temperature data.

Analyze cleaning impact and correlations.

Plot wind rose charts, histograms, scatter plots, and bubble charts to explore relationships.

Export cleaned datasets to data/<country>_clean.csv (data folder ignored by Git).

Document insights and findings in notebooks.

Commit often with meaningful messages.


### Task 3: Cross-Country Comparison

Create branch compare-countries.

Load cleaned datasets for Benin, Sierra Leone, and Togo.

Compare key metrics (GHI, DNI, DHI) using boxplots and summary tables.

Perform statistical testing (e.g., one-way ANOVA or Kruskal–Wallis) to assess differences.

Summarize findings with key observations.

(Optional) Create a bar chart ranking countries by average GHI.

Commit all changes and merge back into main.


### Bonus Task: Interactive Dashboard with Streamlit

Create branch dashboard-dev.

Build a Streamlit app (app/main.py) that:

Provides widgets to select countries.

Displays boxplots and tables of solar metrics.

Shows top regions with solar potential.

Implement interactive and user-friendly features.

Ensure no raw data files are committed; load CSVs locally.

Commit as feat: basic Streamlit UI.

Document dashboard usage in README.


## 📈 Key Performance Indicators (KPIs)

Dev Environment Setup: Reproducible environment and effective version control.

Data Analysis: Thorough EDA with actionable insights and statistical rigor.

Cross-country Comparison: Clear, statistically valid comparisons with visualization.

Dashboard Usability: Intuitive UI, interactivity, and clear visual communication.

Git Hygiene: Clean commits, branching strategy, and CI integration.


## 📝 Notes

Use Python 3.10 or later.

Always activate the virtual environment before running commands.

Keep requirements.txt updated.

Follow clear commit message conventions.

Never commit raw data files; keep them in .gitignore.

After review, merge feature branches into main via Pull Requests.


 ##
 **Author**: Fiteh Tesfaye
 
 **Date**: November 7, 2025
