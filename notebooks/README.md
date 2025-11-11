🌍 **Solar Resource Analysis — Benin, Sierra Leone, and Togo**

📘 **Project Overview**

This repository presents an exploratory and comparative analysis of solar resource potential across Benin, Sierra Leone, and Togo. The goal is to evaluate and compare key solar radiation metrics — GHI (Global Horizontal Irradiance), DNI (Direct Normal Irradiance), and DHI (Diffuse Horizontal Irradiance) — to identify relative strengths and variability between the three countries.

📂 **Repository Structure**

solar-resource-analysis/
│

├── data/                               # Contains raw and cleaned datasets

│   ├── benin_clean.csv

│   ├── sierraleone_clean.csv

│   └── togo_clean.csv
│
├── notebooks/

│   ├── eda_benin.ipynb  # EDA for Benin - data cleaning, trend visualization

│   ├── sierraleone_eda.ipynb           # EDA for Sierra Leone - missing value checks

│   ├── togo_eda.ipynb                  # EDA for Togo - distribution analysis

│   └── compare_countries.ipynb         # Comparative analysis across all three countries
│

├── results/                            # Generated summary tables and plots

│   ├── boxplot_GHI.png

│   ├── boxplot_DNI.png

│   ├── boxplot_DHI.png

│   ├── ghi_ranking.png

│   └── summary_statistics.csv
│
├── scripts/

│   └── comparative_analysis.py         # Script version of comparative analysis
│
└── README.md

⚙️ **Analysis Summary**

**Task 1 & 2 — Country-Level EDA**

Each EDA notebook:

· Loads and cleans country-specific solar radiation data
· Handles missing values and formats numeric metrics
· Produces visual summaries (line charts, histograms, etc.)
· Outputs key descriptive statistics for GHI, DNI, and DHI

**Task 3 — Cross-Country Comparison**

The compare_countries.ipynb notebook:

· Loads the cleaned CSVs from data/
· Compares GHI, DNI, and DHI distributions across countries
· Generates boxplots and a bar chart ranking countries by average GHI
· Computes a summary table (mean, median, standard deviation)
· Performs ANOVA and Kruskal–Wallis tests to check statistical significance
· Concludes with 3 key observations highlighting insights

📊 **Key Outputs**

· Boxplots: GHI, DNI, DHI by country
· Summary Table: Mean, Median, Std for each metric
· Statistical Tests: ANOVA and Kruskal–Wallis p-values
· Bar Chart: Average GHI ranking
· Observations: 3 concise bullet points summarizing results


🚀 **How to Run**

1. Clone this repository:

git clone https://github.com/<your-username>/solar-resource-analysis.git

cd solar-resource-analysis

2. Install required dependencies:

pip install -r requirements.txt

3. Ensure cleaned datasets are placed under data/:

data/

├── benin_clean.csv

├── sierraleone_clean.csv

└── togo_clean.csv

4. Run the analysis:

Option A: Using Jupyter Notebooks

jupyter notebook notebooks/compare_countries.ipynb

Option B: Using Python script

python scripts/comparative_analysis.py

5. Outputs (plots, summary CSV) will be saved under:

data/

🧠 **Insights Example**

· Benin shows the highest median GHI and overall solar potential
· Sierra Leone exhibits greater variability in GHI values, suggesting inconsistent conditions
· Statistical testing confirms whether observed differences are significant (p < 0.05)

✨ **Author**

Developed as part of Task 3 — Cross-Country Solar Comparison for the Software Engineering data analysis module.
