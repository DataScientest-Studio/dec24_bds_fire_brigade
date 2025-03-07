# London Fire Brigade
==============================

This Data Science project focuses on analyzing and estimating the attendance time of the London Fire Brigade. As the busiest fire and rescue service in the UK and one of the largest globally, understanding its response efficiency is crucial. The study aims to provide insights into factors affecting response times and overall operational performance.

Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data               <- Should be in your computer but not on Github (only in .gitignore)
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's name, and a short `-` delimited description, e.g.
    │                         `1.0-alban-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, links, and all other explanatory materials.
    │
    ├── reports            <- The reports that you'll make during this project as PDF
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   ├── visualization  <- Scripts to create exploratory and results oriented visualizations
    │   │   └── visualize.py

--------
# Context

The London Fire Brigade (LFB) is the world’s largest fire service, operating 103 stations with a team of over 5,000 professional firefighters. Covering 13 boroughs across London—home to 8 million residents—the Brigade responds to between 100,000 and 130,000 emergency calls annually, serving a vast area of 1,587 square kilometers.

In life-threatening emergencies, every minute counts. Delays in response time can reduce survival chances or increase the severity of consequences. When it comes to fires, a well-known saying illustrates the urgency: "In the first minute, a fire can be extinguished with a glass of water; in the second, with a bucket; and in the third, with a tanker." Rapid response is essential for minimizing damage and saving lives.

Given this urgency, predicting firefighter intervention times following an emergency call would be highly valuable. Accurate estimations could help call centers reassure those in distress, optimize emergency logistics, and refine dispatch and routing strategies—ultimately reducing response times and improving overall efficiency.

--------
# Data
This project relies on two datasets: [LFB's incident data](https://data.london.gov.uk/dataset/london-fire-brigade-incident-records) and [LFB's mobilization data](https://data.london.gov.uk/dataset/london-fire-brigade-mobilisation-records).
Both datasets are sourced from The London Datastore, a free and open data-sharing platform that provides public access to various datasets related to London.

--------

# Project Roadmap  

## 1️⃣ Data Exploration  
- Downloading the dataset  
- Getting an overview (features, target variable, missing values)  
- Descriptive statistics & visualization  
- Checking correlations between features  

## 2️⃣ Data Preparation  
- Handling missing values  
- Selecting target variable  
- Feature engineering  
- Encoding categorical features  
- Standardization & normalization  
- Splitting data into train/test sets  

## 3️⃣ Modeling  
### 🔹 Baseline Models  
- Testing simple models:  
  - Linear Regression  
  - Random Forest  
  - XGBoost  
- Evaluating baseline performance  

### 🔹 Model Optimization  
- Hyperparameter tuning with **Random Search**  
- Feature selection and importance analysis  

### 🔹 Advanced Modeling  
- Training an **MLPRegressor** (Multi-Layer Perceptron)  
- Experimenting with **Neural Networks** for improved performance  

## 4️⃣ Model Evaluation  
- Comparing model performance using metrics (MAE, RMSE, R²)  
- Cross-validation for robustness  
- Analyzing feature importance  

## 5️⃣ Streamlit App  
- Building an interactive **Streamlit** application  
- Showcasing the modeling process & predictions  
- Adding visualizations for insights  
---



