# Trial Runs

## First Trial

**Output:**

Outputed results containing all four model types, parameters, and optimal score.

- **Logistic Regression**

    Model: LogisticRegression(C=100, random_state=42)

    Parameters: 'class_weight': None, 'C': 100

    Score: 0.9639977992962221

- **Random Forest**

    Model: RandomForestClassifier(min_samples_leaf=5, random_state=42)

    Parameters: 'n_estimators': 100, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'max_depth': None, 'class_weight': None

    Score: 0.9642385899044011

- **Histogram Gradient Boosting**

    Model: HistGradientBoostingClassifier(learning_rate=0.05, max_depth=15, max_leaf_nodes=124, min_samples_leaf=10, random_state=42)

    Parameters: 'min_samples_leaf': 10, 'max_leaf_nodes': 124, 'max_iter': 100, 'max_depth': 15, 'learning_rate': 0.05

    Score: 0.9642075415852792

- **XGBoost**

    Model: XGBClassifier(base_score=None, booster=None, callbacks=None, colsample_bylevel=None, colsample_bynode=None, colsample_bytree=1.0, device=None, early_stopping_rounds=Non, enable_categorical=False, eval_metric=None, feature_types=None, feature_weights=None, gamma=None, grow_policy=None, importance_type=None, interaction_constraints=None, learning_rate=0.1, max_bin=None, max_cat_threshold=None, max_cat_to_onehot=None, max_delta_step=None, max_depth=6, max_leaves=None, min_child_weight=None, missing=nan, monotone_constraints=None, multi_strategy=None, n_estimators=300, n_jobs=None, num_parallel_tree=None, ...)

    Parameters: 'subsample': 0.7, 'scale_pos_weight': 1, 'n_estimators': 300, 'max_depth': 6, 'learning_rate': 0.1, 'colsample_bytree': 1.0

    Score: 0.9642536650556953

**Error:**

Wrong indexing through results dictionary, so could not print scores for test values

## Second Trial

**Output**

Outputed results containing all four model types, the importance of each varaible, and the scores from each objective function

- **Logistic Regression**

    Model: LogisticRegression(C=100, max_iter=1000, random_state=42)

    Parameters: 'class_weight': None, 'C': 100

    Score: 0.9448955357886013

    Insurance_FONASA                                                     -14.628959
    Procedure Description_OTHER                                          -12.053531
    Insurance_ISAPRES                                                     -8.818080
    Medical Center Name_HOSPITAL CLINICO UNIVERSIDAD DE CHILE             -3.784913
    Insurance_OTRAS PREVISIONES                                           -3.242870
                                                                            ...
    Speciality Description_UNIDAD PROCED CLINICOS AMBULATORIOS ADULTOS     2.536635
    Subspeciality Description_PROCED (S) COLONO - GASTRO                   2.624671
    Speciality Description_MEDICINA FISICA                                 5.635446
    Speciality Description_DENTO MAXILO FACIAL                             7.129654
    Procedure Description_                                                22.229241
    Length: 187

    Accuracy: 0.9990742291656293
    Precision: 0.9966647718703959
    Recall: 0.9985877840413785
    F1 Score: 0.9976253512622215
    Balanced Accuracy: 0.998889826347017
    MCC Score: nan

- **Random Forest**

    Model: RandomForestClassifier(max_depth=10, max_features=None, min_samples_leaf=5, n_estimators=500, random_state=42)

    Parameters: 'n_estimators': 500, 'min_samples_leaf': 5, 'max_features': None, 'max_depth': 10, 'class_weight': None

    Score: 0.9450249809934229

    Nationality                  0.000005
    Sex                          0.000038
    Previous Late Arrival        0.000142
    Municipality                 0.000185
    Day of the Week              0.000250
    Procedure Description        0.000338
    Time                         0.000573
    Month of Entry               0.000694
    Medical Center Name          0.000826
    Previous No-Show             0.001181
    Time Interval                0.001465
    Age                          0.002966
    Type of Visit                0.004239
    Subspeciality Description    0.004727
    Speciality Description       0.006112
    Insurance                    0.976260

    Accuracy: 0.9989712399896784
    Precision: 0.9967033668607115
    Recall: 0.9980182483872843
    F1 Score: 0.9973603742518883
    Balanced Accuracy: 0.998609977580345
    MCC Score: 45.7913086000612

- **Histogram Gradient Boosting**

    Model: HistGradientBoostingClassifier(learning_rate=0.05, max_depth=3, max_iter=300, random_state=42)

    Parameters: 'min_samples_leaf': 20, 'max_leaf_nodes': 31, 'max_iter': 300, 'max_depth': 3, 'learning_rate': 0.05

    Score: 0.9451251244694722

    Type of Visit               -5.681381e-05
    Subspeciality Description   -4.821252e-05
    Medical Center Name         -3.349978e-05
    Speciality Description      -3.259438e-05
    Previous No-Show            -1.652354e-05
    Time                        -1.516544e-05
    Month of Entry              -1.109114e-05
    Age                         -2.489848e-06
    Sex                          0.000000e+00
    Previous Late Arrival        0.000000e+00
    Nationality                  9.053993e-07
    Municipality                 1.584449e-06
    Day of the Week              2.716198e-06
    Time Interval                5.828508e-04
    Procedure Description        1.542737e-01
    Insurance                    1.561243e-01

    Accuracy: 0.9991896675826291
    Precision: 0.9967070554814772
    Recall: 0.9991398849305515
    F1 Score: 0.9979219874622707
    Balanced Accuracy: 0.9991707958519785
    MCC Score: 103.54205598528588

- **Extreme Gradient Boosting**

    Model: XGBClassifier(base_score=None, booster=None, callbacks=None, colsample_bylevel=None, colsample_bynode=None, colsample_bytree=1.0, device=None, early_stopping_rounds=None, enable_categorical=False, eval_metric=None, feature_types=None, feature_weights=None, gamma=None, grow_policy=None, importance_type=None, interaction_constraints=None, learning_rate=0.05, max_bin=None, max_cat_threshold=None, max_cat_to_onehot=None, max_delta_step=None, max_depth=6, max_leaves=None, min_child_weight=None, missing=nan, monotone_constraints=None, multi_strategy=None, n_estimators=200, n_jobs=None, num_parallel_tree=None, ...)

    Parameters: 'subsample': 1.0, 'scale_pos_weight': 1, 'n_estimators': 200, 'max_depth': 6, 'learning_rate': 0.05, 'colsample_bytree': 1.0

    Score: 0.9451998368314394

    Municipality                 0.000101
    Previous Late Arrival        0.000101
    Sex                          0.000118
    Nationality                  0.000148
    Time                         0.000219
    Day of the Week              0.000226
    Time Interval                0.000470
    Month of Entry               0.000522
    Age                          0.000855
    Speciality Description       0.001255
    Subspeciality Description    0.001384
    Previous No-Show             0.001440
    Type of Visit                0.001722
    Medical Center Name          0.002571
    Procedure Description        0.249674
    Insurance                    0.739192

    Accuracy: 0.9990266956998058
    Precision: 0.9967043041323849
    Recall: 0.9983030162143314
    F1 Score: 0.9975030196041995
    Balanced Accuracy: 0.9987523614938685
    MCC Score: nan

**Error**

MCC calculation couldn't be computed because of integer overflow

## Third Trial

**Output**

Changed the output to include plots and removed Insurance and Procedure Description

- **Logistic Regression**

    Model: LogisticRegression(C=0.1, class_weight={0: 1, 1: 4}, max_iter=1000, random_state=42)

    Parameters: 'class_weight': {0: 1, 1: 4}, 'C': 0.1

    Score: 0.42804333611838885

    Subspeciality Description_TRATAMIENTO ANTICOAGULANTE (T.A.C.)   -3.440762
    Speciality Description_CENTRO DE VACUNAS                        -2.305398
    Subspeciality Description_REUMATOLOGIA (S) CREA                 -2.131121
    Subspeciality Description_PROCED (S) QUIMIOTERAPIA              -1.751524
    Subspeciality Description_DENTAL: ODONTOLOGIA INTEGRAL          -1.299105
                                                                    ...
    Subspeciality Description_GINECOLOGIA GENERAL                    0.777914
    Subspeciality Description_MEDICINA GENERAL HCUCH                 1.042415
    Subspeciality Description_UROLOGIA ADULTO                        1.832624
    Speciality Description_DENTO MAXILO FACIAL                       2.255928
    Subspeciality Description_CL-QUILIN: (S) KINESIOTERAPIA          3.137341
    Length: 159

    Accuracy:  0.7401085121119798
    Precision:  0.3764025403532276
    Recall:  0.5094263962340908
    F1 Score:  0.43292645283009557
    Balanced Accuracy:  0.6526609661285363
    MCC Score:  0.27443769258671347

    ROC AUC Score: 0.7406

- **Random Forest**

    Model: RandomForestClassifier(class_weight='balanced_subsample', max_depth=30, min_samples_leaf=10, n_estimators=200, random_state=42)

    Parameters: 'n_estimators': 200, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'max_depth': 30, 'class_weight': 'balanced_subsample'

    Score: 0.46210669029498314

    *Error caused output to not appear*

- **Histogram Gradient Boosting**

    Model: HistGradientBoostingClassifier(learning_rate=0.3, max_depth=9, max_iter=200, max_leaf_nodes=62, min_samples_leaf=30, random_state=42)

    Parameters: 'min_samples_leaf': 30, 'max_leaf_nodes': 62, 'max_iter': 200, 'max_depth': 9, 'learning_rate': 0.3

    Score: 0.355917336078226

    *Error caused output to not appear*

- **Extreme Gradient Boosting**

    Model: XGBClassifier(base_score=None, booster=None, callbacks=None, colsample_bylevel=None, colsample_bynode=None, colsample_bytree=0.9, device=None, early_stopping_rounds=None enable_categorical=False, eval_metric=None, feature_types=None, feature_weights=None, gamma=None, grow_policy=None, importance_type=None, interaction_constraints=None, learning_rate=0.05, max_bin=None, max_cat_threshold=None, max_cat_to_onehot=None, max_delta_step=None, max_depth=9, max_leaves=None, min_child_weight=None, missing=nan, monotone_constraints=None, multi_strategy=None, n_estimators=300, n_jobs=None, num_parallel_tree=None, ...)

    Parameters: 'subsample': 1.0, 'scale_pos_weight': 4, 'n_estimators': 300, 'max_depth': 9, 'learning_rate': 0.05, 'colsample_bytree': 0.9

    Score: 0.45963894229659696

    *Error caused output to not appear*
