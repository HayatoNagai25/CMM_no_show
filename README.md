# HCUCH Medical Appointment No-Show Prediction System

## Overview

This project implements a no-show (NSP — *No Se Presentó*) prediction system for the medical appointments managed by the Hospital Clínico Universidad de Chile (HCUCH). It was developed as part of a collaboration with the Center for Mathematical Modeling (CMM) to improve scheduling efficiency across the hospital's healthcare services.

## Project Objectives

**Institutional Objective**
Implement a predictive system capable of identifying patients at risk of missing their medical appointments, enabling HCUCH to optimize scheduling and reduce the operational impact of no-shows across its healthcare services.

**Research Objective**
Explore and characterize historical appointment data provided by HCUCH, identify the variables of interest that most influence no-show behavior, and train and evaluate machine learning models for NSP prediction.

## Dataset

The dataset contains anonymized ambulatory appointment records from HCUCH spanning 2023–2026. Each record represents a single appointment and includes information about the patient, the appointment, and the outcome.

After processing, the following 17 variables of interest are used for prediction:

| Variable | Description |
|---|---|
| Previous No-Show | Number of prior no-shows for the same patient |
| Previous Late Arrival | Number of prior late arrivals for the same patient |
| Time Interval | Days between booking date and appointment date |
| Day of the Week | Day of the scheduled appointment |
| Season | Season of the scheduled appointment |
| Appointment Time | Time of day of the scheduled appointment |
| Month of Entry | Month the appointment was booked |
| Speciality | Medical speciality of the appointment |
| Subspeciality | Medical subspeciality of the appointment |
| Nationality | Patient nationality |
| Sex | Patient sex |
| Municipality | Patient municipality of residence |
| Insurance | Patient health insurance coverage |
| Age | Patient age at time of visit |
| Procedure Description | Type of medical procedure or service |
| Hospital Location | Medical center where the appointment takes place |
| Type of Visit | Institutional, private, or extra-staff appointment |

## Models

Four machine learning models are trained and evaluated to identify the best predictor of no-show behavior:

- **Logistic Regression** — linear baseline model
- **Random Forest** — ensemble tree-based model
- **Histogram Gradient Boosting** — fast gradient boosted trees (sklearn)
- **XGBoost** — gradient boosted trees

Models are compared using precision, recall, F1-score, and ROC-AUC, with particular emphasis on recall for the no-show class.

## Project Structure

```
├── data/
│   └── df2023-2026_anon.csv       # Anonymized appointment data
├── data_extraction.py             # Data loading, cleaning, and feature engineering
├── model.py                       # Model training and evaluation
└── README.md
```

## File Descriptions

**`data_extraction.py`**
Handles all data preprocessing. Loads the raw CSV, removes irrelevant and redundant columns, engineers features from date and time columns, builds patient history features using patient IDs, and outputs a clean feature matrix ready for model training. Produces two versions of the data — one for tree-based models and one for logistic regression.

**`model.py`**
Handles model training, evaluation, and comparison. Loads the processed data from `data_extraction.py`, splits into balanced train and test sets, fits each model, and evaluates performance using a configurable objective function.
