# Predicting No-Shows for HCUCH Medical Appointments

## Overview

This project implements a no-show (NSP — *No Se Presentó*) prediction model for the medical appointments managed by the Hospital Clínico Universidad de Chile (HCUCH). It was developed as part of a collaboration with the Center for Mathematical Modeling (CMM) at the University of Chile to improve save avoidable costs from missed appointments.

## Project Objectives

**Research Objective**
Implement the CMM medical appointment no-show prediction system for the different healthcare services provided by HCUCH in order to improve hospital scheduling efficiency.

**Internship Objective**
Explore the historical appointment data provided by HCUCH, characterize the NSP by different variables of interest, and train and evaluate predictive methods for the prediction of NSP.

## Dataset

The dataset contains anonymized ambulatory appointment records from HCUCH spanning 2023–2026. Each record represents a single appointment and includes information about the patient, the appointment, and their attendance status.

After processing the data, the following 14 variables of interest are used for prediction:

| Variable | Description |
|---|---|
| Previous No-Show | Number of prior no-shows for the same patient |
| Previous Late Arrival | Number of prior late arrivals for the same patient |
| Time Interval | Days between booking date and appointment date |
| Day of the Week | Day of the scheduled appointment |
| Appointment Time | Time of day of the scheduled appointment |
| Month of Entry | Month the appointment was booked |
| Speciality | Medical speciality of the appointment |
| Subspeciality | Medical subspeciality of the appointment |
| Nationality | Patient nationality |
| Sex | Patient sex |
| Municipality | Patient municipality of residence |
| Age | Patient age at time of visit |
| Hospital Location | Medical center where the appointment takes place |
| Type of Visit | Institutional, private, or extra-staff appointment |

## Models

Four machine learning models are trained and evaluated to identify the best predictor of no-show behavior:

- **Logistic Regression** — linear baseline model
- **Random Forest** — ensemble tree-based model
- **Histogram Gradient Boosting** — fast gradient boosted trees
- **XGBoost** — gradient boosted trees

Models are compared using accuracy, precision, recall, F1-score, balanced accuracy, Matthews Correlation Coefficient, and ROC-AUC.

## Project Structure

```
├── data/
│   └── df2023-2026_anon.csv       # Anonymized appointment data
├── create_models.py               # Model training and evaluation
├── data_analysis.py               # Analyze and interpret data
├── data_extraction.py             # Data loading, cleaning, and varaiable calculations
├── graph_visualization.py         # Plots all relevant graphs
├── main.py                        # Execute machine learning modeling
├── README.md
└── trials.md                      # All trial data
```

## File Descriptions

**`create_models.py`**
Handles model training, evaluation, and comparison. Loads the processed data from `data_extraction.py`, splits into train and test sets, fits each model, and evaluates performance using a configurable objective function.

**`data_analysis.py`**
Uses pandas to interpret the data and comprehend the correlations between each data entry. Separate from all other files and is only used to help better understand the data, not to develop the learning models.

**`data_extraction.py`**
Handles all data preprocessing. Loads the raw CSV file, removes irrelevant and redundant columns, engineers features from date and time columns, builds patient history features using patient IDs, and outputs a clean feature matrix ready for model training. Produces two versions of the data — one for tree-based models and one for logistic regression.

**`graph_visualization`**
Handles the plotting of the Receiver Operating Characteristic (ROC) based Area Under the Curve (AUC) graph and the Precision-Recall (PR) based Area Under the Curve (AUC) graph.

**`main.py`**
Incorporates all the functions from `create_models`, `data_extraction`, amd `graph_visualization` in order to process the data, intepret it, split it, fit it into each of the four models, evaluate the performance, and then print visuals of each model's effectiveness.
