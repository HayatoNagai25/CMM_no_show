# Trial Runs

## First Trial

**Output:**

Outputed results containing all four model types, parameters, and optimal score.

- **Logistic Regression**

    Model: LogisticRegression(C=100, random_state=42)

    Parameters: 'class_weight': None, 'C': 100

    Score: 0.9639977992962221

================================================================================

- **Random Forest**

    Model: RandomForestClassifier(min_samples_leaf=5, random_state=42)

    Parameters: 'n_estimators': 100, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'max_depth': None, 'class_weight': None

    Score: 0.9642385899044011

================================================================================

- **Histogram Gradient Boosting**

    Model: HistGradientBoostingClassifier(learning_rate=0.05, max_depth=15, max_leaf_nodes=124, min_samples_leaf=10, random_state=42)

    Parameters: 'min_samples_leaf': 10, 'max_leaf_nodes': 124, 'max_iter': 100, 'max_depth': 15, 'learning_rate': 0.05

    Score: 0.9642075415852792

================================================================================

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

    Balanced Accuracy: 0.998889826347017
    Precision: 0.9966647718703959
    Recall: 0.9985877840413785
    F1 Score: 0.9976253512622215
    MCC Score: nan

================================================================================

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

    Balanced Accuracy: 0.998609977580345
    Precision: 0.9967033668607115
    Recall: 0.9980182483872843
    F1 Score: 0.9973603742518883
    MCC Score: 45.7913086000612

================================================================================

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

    Balanced Accuracy: 0.9991707958519785
    Precision: 0.9967070554814772
    Recall: 0.9991398849305515
    F1 Score: 0.9979219874622707
    MCC Score: 103.54205598528588

================================================================================

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

    Balanced Accuracy: 0.9987523614938685
    Precision: 0.9967043041323849
    Recall: 0.9983030162143314
    F1 Score: 0.9975030196041995
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

    Balanced Accuracy: 0.6526609661285363
    Precision: 0.3764025403532276
    Recall: 0.5094263962340908
    F1 Score: 0.43292645283009557
    MCC Score: 0.27443769258671347

    ROC AUC Score: 0.7406

================================================================================

- **Random Forest**

    Model: RandomForestClassifier(class_weight='balanced_subsample', max_depth=30, min_samples_leaf=10, n_estimators=200, random_state=42)

    Parameters: 'n_estimators': 200, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'max_depth': 30, 'class_weight': 'balanced_subsample'

    Score: 0.46210669029498314

    *Error caused output to not appear*

================================================================================

- **Histogram Gradient Boosting**

    Model: HistGradientBoostingClassifier(learning_rate=0.3, max_depth=9, max_iter=200, max_leaf_nodes=62, min_samples_leaf=30, random_state=42)

    Parameters: 'min_samples_leaf': 30, 'max_leaf_nodes': 62, 'max_iter': 200, 'max_depth': 9, 'learning_rate': 0.3

    Score: 0.355917336078226

    *Error caused output to not appear*

================================================================================

- **Extreme Gradient Boosting**

    Model: XGBClassifier(base_score=None, booster=None, callbacks=None, colsample_bylevel=None, colsample_bynode=None, colsample_bytree=0.9, device=None, early_stopping_rounds=None enable_categorical=False, eval_metric=None, feature_types=None, feature_weights=None, gamma=None, grow_policy=None, importance_type=None, interaction_constraints=None, learning_rate=0.05, max_bin=None, max_cat_threshold=None, max_cat_to_onehot=None, max_delta_step=None, max_depth=9, max_leaves=None, min_child_weight=None, missing=nan, monotone_constraints=None, multi_strategy=None, n_estimators=300, n_jobs=None, num_parallel_tree=None, ...)

    Parameters: 'subsample': 1.0, 'scale_pos_weight': 4, 'n_estimators': 300, 'max_depth': 9, 'learning_rate': 0.05, 'colsample_bytree': 0.9

    Score: 0.45963894229659696

    *Error caused output to not appear*

================================================================================

**Error**

All stats were not printed

## Fourth Trial

**Output**

Optimized threshold with a range from 0.05 to 0.96, incremented by 0.05

Objective Function: F1 Score

- **Logistic Regression**

    Model: LogisticRegression(C=10, class_weight={0: 1, 1: 4}, max_iter=1000, random_state=42)

    Parameters: {'class_weight': {0: 1, 1: 4}, 'C': 10}

    Score: 0.42796703838211686

    Balanced Accuracy: 0.6526203551560759
    Precision: 0.3759775459044844
    Recall: 0.5099087580635788
    F1 Score: 0.4328190708744929
    MCC Score: 0.2741820101794323

    ROC AUC Score: 0.7405
    PR AUC Score: 0.4471214070485371

================================================================================

- **Random Forest**

    Model: RandomForestClassifier(class_weight='balanced_subsample', max_features=None, min_samples_leaf=10, random_state=42)

    Parameters: {'n_estimators': 100, 'min_samples_leaf': 10, 'max_features': None, 'max_depth': None, 'class_weight': 'balanced_subsample'}

    Score: 0.4473705692633168

    Balanced Accuracy: 0.6507723249298547
    Precision: 0.461598891237841
    Recall: 0.4200209217179055
    F1 Score: 0.43982947958410545
    MCC Score: 0.3127297564894693

    ROC AUC Score: 0.7569
    PR AUC Score: 0.5045214224741926

================================================================================

- **Histogram-based Gradient Boosting**

    Model: HistGradientBoostingClassifier(learning_rate=0.3, max_depth=9, max_iter=200, max_leaf_nodes=62, min_samples_leaf=30, random_state=42)

    Parameters: {'min_samples_leaf': 30, 'max_leaf_nodes': 62, 'max_iter': 200, 'max_depth': 9, 'learning_rate': 0.3}

    Score: 0.355917336078226

    Balanced Accuracy: 0.5900393556652043
    Precision: 0.784076147287371
    Recall: 0.1929272970302784
    F1 Score: 0.30966050865402106
    MCC Score: 0.3338684035940022

    ROC AUC Score: 0.7667
    PR AUC Score: 0.5116218127739453

================================================================================

- **Extreme Gradient Boosting**

    Model: XGBClassifier(base_score=None, booster=None, callbacks=None, colsample_bylevel=None, colsample_bynode=None, colsample_bytree=0.7, device=None, early_stopping_rounds=None, enable_categorical=False, eval_metric=None, feature_types=None, feature_weights=None, gamma=None, grow_policy=None, importance_type=None, interaction_constraints=None, learning_rate=0.05, max_bin=None, max_cat_threshold=None, max_cat_to_onehot=None, max_delta_step=None, max_depth=3, max_leaves=None, min_child_weight=None, missing=nan, monotone_constraints=None, multi_strategy=None, n_estimators=300, n_jobs=None, num_parallel_tree=None, ...)

    Parameters: {'subsample': 0.9, 'scale_pos_weight': 4, 'n_estimators': 300, 'max_depth': 3, 'learning_rate': 0.05, 'colsample_bytree': 0.7}

    Score: 0.4462947574861739

    Balanced Accuracy: 0.676183321251626
    Precision: 0.38389211303182214
    Recall: 0.5758760969372929
    F1 Score: 0.46068267192323425
    MCC Score: 0.30684987399924685

    ROC AUC Score: 0.7606
    PR AUC Score: 0.49164300917504167

## Fifth Trial

**Output**

Changed so balances the training set using inbalanced learn

- **Logistic Regression**

    Model: LogisticRegression(C=10, class_weight='balanced', max_iter=1000, random_state=42)

    Parameters: {'class_weight': 'balanced', 'C': 10}

    Score: 0.8188111307337674

    Balanced Accuracy: 0.5874975421503522
    Precision: 0.6809641260101466
    Recall: 0.19735572732027662
    F1 Score: 0.3060210237948265
    MCC Score: 0.30029368204694323

    ROC AUC Score: 0.7325
    PR AUC Score: 0.43945269791196784

================================================================================

- **Random Forest**

    Model: RandomForestClassifier(class_weight='balanced_subsample', random_state=42)

    Parameters: {'n_estimators': 100, 'min_samples_leaf': 1, 'max_features': 'sqrt', 'max_depth': None, 'class_weight': 'balanced_subsample'}

    Score: 0.8256812553704355

    Balanced Accuracy: 0.6078311495488606
    Precision: 0.6032095356561915
    Recall: 0.2564595804033242
    F1 Score: 0.3599032732937238
    MCC Score: 0.30990871509389767

    ROC AUC Score: 0.7342
    PR AUC Score: 0.48129402481378725

================================================================================

- **Histogram-based Gradient Boosting**

    Model: HistGradientBoostingClassifier(learning_rate=0.3, max_depth=15, max_iter=300, random_state=42)

    Parameters: {'min_samples_leaf': 20, 'max_leaf_nodes': 31, 'max_iter': 300, 'max_depth': 15, 'learning_rate': 0.3}

    Score: 0.8212794531202722

    Balanced Accuracy: 0.5963566099263672
    Precision: 0.7189156295394763
    Recall: 0.2128377985703493
    F1 Score: 0.32843972521658027
    MCC Score: 0.32740766075138156

    ROC AUC Score: 0.7624
    PR AUC Score: 0.5012412231791918

================================================================================

- **Extreme Gradient Boosting**

    Model: XGBClassifier(base_score=None, booster=None, callbacks=None, colsample_bylevel=None, colsample_bynode=None, colsample_bytree=0.7, device=None, early_stopping_rounds=None, enable_categorical=False, eval_metric=None, feature_types=None, feature_weights=None, gamma=None, grow_policy=None, importance_type=None, interaction_constraints=None, learning_rate=0.3, max_bin=None, max_cat_threshold=None, max_cat_to_onehot=None, max_delta_step=None, max_depth=6, max_leaves=None, min_child_weight=None, missing=nan, monotone_constraints=None, multi_strategy=None, n_estimators=100, n_jobs=None, num_parallel_tree=None, ...)

    Parameters: {'subsample': 0.7, 'scale_pos_weight': 1, 'n_estimators': 100, 'max_depth': 6, 'learning_rate': 0.3, 'colsample_bytree': 0.7}

    Score: 0.8191187242773887

    Balanced Accuracy: 0.5957872866124543
    Precision: 0.7208689275166987
    Recall: 0.21136746672865694
    F1 Score: 0.3268875576906657
    MCC Score: 0.3269506495173912

    ROC AUC Score: 0.7605
    PR AUC Score: 0.5022496526709197

## Sixth Trial

**Output**

Removed Subspeciality Description

Objective Function: F1 Score

- **Logistic Regression**

Model: LogisticRegression(C=10, class_weight={0: 1, 1: 4}, max_iter=1000, random_state=42)

Parameters: {'class_weight': {0: 1, 1: 4}, 'C': 10}

Score: 0.4111625413495703

Balanced Accuracy: 0.6397339303329578
Precision: 0.35027372665892814
Recall: 0.5068169930842099
F1 Score: 0.41424944364088057
MCC Score: 0.24600682884063738

ROC AUC Score: 0.7061
PR AUC Score: 0.4024686196249958

================================================================================

- **Random Forest**

Model: RandomForestClassifier(class_weight='balanced_subsample', max_features=None, min_samples_leaf=10, random_state=42)

Parameters: {'n_estimators': 100, 'min_samples_leaf': 10, 'max_features': None, 'max_depth': None, 'class_weight': 'balanced_subsample'}

Score: 0.4376396475895638

Balanced Accuracy: 0.6462690225950476
Precision: 0.4501439760060993
Recall: 0.41518568024641134
F1 Score: 0.43195869120283453
MCC Score: 0.3017841876122704

ROC AUC Score: 0.7428
PR AUC Score: 0.49333292908351023

================================================================================

- **Histogram-based Gradient Boosting**

Model: HistGradientBoostingClassifier(learning_rate=0.3, max_depth=9, max_iter=200, max_leaf_nodes=62, min_samples_leaf=30, random_state=42)

Parameters: {'min_samples_leaf': 30, 'max_leaf_nodes': 62, 'max_iter': 200, 'max_depth': 9, 'learning_rate': 0.3}

Score: 0.35074065174603536

Balanced Accuracy: 0.5869464267803396
Precision: 0.7954426466555309
Recall: 0.18542453652583252
F1 Score: 0.3007432333715083
MCC Score: 0.3307949662497933

ROC AUC Score: 0.7527
PR AUC Score: 0.5014242053235135

================================================================================

- **Extreme Gradient Boosting**

Model: XGBClassifier(base_score=None, booster=None, callbacks=None, colsample_bylevel=None, colsample_bynode=None, colsample_bytree=0.7, device=None, early_stopping_rounds=None, enable_categorical=False, eval_metric=None, feature_types=None, feature_weights=None, gamma=None, grow_policy=None, importance_type=None, interaction_constraints=None, learning_rate=0.05, max_bin=None, max_cat_threshold=None, max_cat_to_onehot=None, max_delta_step=None, max_depth=3, max_leaves=None, min_child_weight=None, missing=nan, monotone_constraints=None, multi_strategy=None, n_estimators=300, n_jobs=None, num_parallel_tree=None, ...)

Parameters: {'subsample': 0.9, 'scale_pos_weight': 4, 'n_estimators': 300, 'max_depth': 3, 'learning_rate': 0.05, 'colsample_bytree': 0.7}

Score: 0.44033661968067767

Balanced Accuracy: 0.6652157355913617
Precision: 0.3833060138546823
Recall: 0.5408787121520312
F1 Score: 0.448659358458913
MCC Score: 0.29311771739083187

ROC AUC Score: 0.7407
PR AUC Score: 0.4752225460022929

## Seventh Trial

**Output**

Used threshold fine-tuning and increased number of trials/iterations. Did not use inbalanced learn and added Subspeciality Description back

Objective Function: F1 Score

- **Logistic Regression**

    Best Threshold: 0.45
    Best F1: 0.4363

    Balanced Accuracy: 0.5170332527287216
    Precision: 0.8266398929049531
    Recall: 0.035886557796245715
    F1 Score: 0.06878689985518548
    MCC: 0.14734367866655565
    ROC AUC Score: 0.7406
    PR AUC Score: 0.44716819692283505

================================================================================

- **Random Forest**

    Best Threshold: 0.45
    Best F1: 0.4704

    Balanced Accuracy: 0.5512654827183334
    Precision: 0.931683784624961
    Recall: 0.10438193758354158
    F1 Score: 0.18773125405021218
    MCC: 0.2779296080127921
    ROC AUC Score: 0.7697
    PR AUC Score: 0.5158917453688137

================================================================================

- **Histogram-based Gradient Boosting**

    Best Threshold: 0.20
    Best F1: 0.4674

    Balanced Accuracy: 0.5434911997927802
    Precision: 0.9514660639166196
    Recall: 0.08806880920555588
    F1 Score: 0.16121533854263634
    MCC: 0.2589016873376081
    ROC AUC Score: 0.7672
    PR AUC Score: 0.5131609220720333

================================================================================

- **Extreme Gradient Boosting**

    Best Threshold: 0.50
    Best F1: 0.4727

    Balanced Accuracy: 0.5605934933015987
    Precision: 0.9234875444839857
    Recall: 0.12366478758644738
    F1 Score: 0.2181208741645824
    MCC: 0.30113024697693636
    ROC AUC Score: 0.7720
    PR AUC Score: 0.5197172946348194

**Error**

Did not print the model, its parameters, and the score

## Eigth Trial

**Output**

Used f2 score instead of f1 score and fixed threshold

Objective Function: F2 Score

- **Logistic Regression**

    Model: LogisticRegression(C=0.1, class_weight={0: 1, 1: 5}, max_iter=1000,
                    random_state=42)

    Parameters: {'class_weight': {0: 1, 1: 5}, 'C': 0.1}

    Score: 0.5576221369172651

    Best Threshold: 0.36

    Balanced Accuracy: 0.6284024163818982
    Precision: 0.250791550493833
    Recall: 0.9252629743708956
    F1 Score: 0.3946213905068782
    MCC Score: 0.2261160906236329
    F2 Score: 0.6016506564080084

    ROC AUC Score: 0.7405
    PR AUC Score: 0.44665204793258184

================================================================================

- **Random Forest**

    Model: RandomForestClassifier(class_weight='balanced', max_depth=10, min_samples_leaf=10, min_samples_split=20, random_state=42)

    Parameters: {'n_estimators': 100, 'min_samples_split': 20, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'max_depth': 10, 'class_weight': 'balanced'}

    Score: 0.5563197542079444

    Best Threshold: 0.38

    Balanced Accuracy: 0.6520170122366294
    Precision: 0.2680866844604159
    Recall: 0.8948567443482304
    F1 Score: 0.4125723946952758
    MCC Score: 0.25242704884940464
    F2 Score: 0.6097467288749991

    ROC AUC Score: 0.7589
    PR AUC Score: 0.49204530949943776

================================================================================

- **Histogram-based Gradient Boosting**

    Model: HistGradientBoostingClassifier(learning_rate=0.3, max_depth=9, max_iter=200, max_leaf_nodes=62, min_samples_leaf=30, random_state=42)

    Parameters: {'min_samples_leaf': 30, 'max_leaf_nodes': 62, 'max_iter': 200, 'max_depth': 9, 'learning_rate': 0.3}

    Score: 0.2681182624259133

    Best Threshold: 0.10

    Balanced Accuracy: 0.6593659738500076
    Precision: 0.2741951733791024
    Recall: 0.8857267391178009
    F1 Score: 0.41875576999164726
    MCC Score: 0.26129106976474126
    F2 Score: 0.6125121974352833

    ROC AUC Score: 0.7672
    PR AUC Score: 0.5131609220720333

================================================================================

- **Extreme Gradient Boosting**

    Model: XGBClassifier(base_score=None, booster=None, callbacks=None, colsample_bylevel=None, colsample_bynode=None, colsample_bytree=1.0, device=None, early_stopping_rounds=None, enable_categorical=False, eval_metric=None, feature_types=None, feature_weights=None, gamma=None, grow_policy=None, importance_type=None, interaction_constraints=None, learning_rate=0.05, max_bin=None, max_cat_threshold=None, max_cat_to_onehot=None, max_delta_step=None, max_depth=9, max_leaves=None, min_child_weight=None, missing=nan, monotone_constraints=None, multi_strategy=None, n_estimators=200, n_jobs=None, num_parallel_tree=None, ...)

    Parameters: {'subsample': 1.0, 'scale_pos_weight': 4, 'n_estimators': 200, 'max_depth': 9, 'learning_rate': 0.05, 'colsample_bytree': 1.0}

    Score: 0.5462593426578185

    Best Threshold: 0.32

    Balanced Accuracy: 0.6640255685476641
    Precision: 0.27788112078694327
    Recall: 0.8829197419654792
    F1 Score: 0.4227197538095112
    MCC Score: 0.26747023234989703
    F2 Score: 0.6150754289665694

    ROC AUC Score: 0.7710
    PR AUC Score: 0.5167170279727622

## Ninth Trial

**Output**

Changed threshold function to consider both f2 score and precision

Objective Function: F2 Score

Logistic Regression

Model: LogisticRegression(C=0.1, class_weight={0: 1, 1: 5}, max_iter=1000,
                   random_state=42)

Parameters: {'class_weight': {0: 1, 1: 5}, 'C': 0.1}

Score: 0.5576221369172651

Best Threshold: 0.36

Balanced Accuracy: 0.6284024163818982
Precision: 0.250791550493833
Recall: 0.9252629743708956
F1 Score: 0.3946213905068782
MCC Score: 0.2261160906236329
F2 Score: 0.6016506564080084

ROC AUC Score: 0.7405
PR AUC Score: 0.44665204793258184

================================================================================

Random Forest

Model: RandomForestClassifier(class_weight='balanced', max_depth=10,
                       min_samples_leaf=10, min_samples_split=20,
                       random_state=42)

Parameters: {'n_estimators': 100, 'min_samples_split': 20, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'max_depth': 10, 'class_weight': 'balanced'}

Score: 0.5563197542079444

Best Threshold: 0.38

Balanced Accuracy: 0.6520170122366294
Precision: 0.2680866844604159
Recall: 0.8948567443482304
F1 Score: 0.4125723946952758
MCC Score: 0.25242704884940464
F2 Score: 0.6097467288749991

ROC AUC Score: 0.7589
PR AUC Score: 0.49204530949943776

================================================================================

Histogram-based Gradient Boosting

Model: HistGradientBoostingClassifier(learning_rate=0.3, max_depth=9, max_iter=200,
                               max_leaf_nodes=62, min_samples_leaf=30,
                               random_state=42)

Parameters: {'min_samples_leaf': 30, 'max_leaf_nodes': 62, 'max_iter': 200, 'max_depth': 9, 'learning_rate': 0.3}

Score: 0.2681182624259133

Best Threshold: 0.10

Balanced Accuracy: 0.6593659738500076
Precision: 0.2741951733791024
Recall: 0.8857267391178009
F1 Score: 0.41875576999164726
MCC Score: 0.26129106976474126
F2 Score: 0.6125121974352833

ROC AUC Score: 0.7672
PR AUC Score: 0.5131609220720333

================================================================================

Extreme Gradient Boosting

Model: XGBClassifier(base_score=None, booster=None, callbacks=None,
              colsample_bylevel=None, colsample_bynode=None,
              colsample_bytree=1.0, device=None, early_stopping_rounds=None,
              enable_categorical=False, eval_metric=None, feature_types=None,
              feature_weights=None, gamma=None, grow_policy=None,
              importance_type=None, interaction_constraints=None,
              learning_rate=0.05, max_bin=None, max_cat_threshold=None,
              max_cat_to_onehot=None, max_delta_step=None, max_depth=9,
              max_leaves=None, min_child_weight=None, missing=nan,
              monotone_constraints=None, multi_strategy=None, n_estimators=200,
              n_jobs=None, num_parallel_tree=None, ...)

Parameters: {'subsample': 1.0, 'scale_pos_weight': 4, 'n_estimators': 200, 'max_depth': 9, 'learning_rate': 0.05, 'colsample_bytree': 1.0}

Score: 0.5462593426578185

Best Threshold: 0.32

Balanced Accuracy: 0.6640255685476641
Precision: 0.27788112078694327
Recall: 0.8829197419654792
F1 Score: 0.4227197538095112
MCC Score: 0.26747023234989703
F2 Score: 0.6150754289665694

ROC AUC Score: 0.7710
PR AUC Score: 0.5167170279727622

## Tenth Trial

**Output**

Increased lowest threshold to 0.40

Objective Function: F2 Score

Logistic Regression

Model: LogisticRegression(C=0.1, class_weight={0: 1, 1: 5}, max_iter=1000,
                   random_state=42)

Parameters: {'class_weight': {0: 1, 1: 5}, 'C': 0.1}

Score: 0.5576221369172651

Best Threshold: 0.40

Balanced Accuracy: 0.6416098058983626
Precision: 0.26252830755783724
Recall: 0.8832451909106759
F1 Score: 0.40475166416104846
MCC Score: 0.23596220004764104
F2 Score: 0.5996737661075024

ROC AUC Score: 0.7405
PR AUC Score: 0.44665204793258184

================================================================================

Random Forest

Model: RandomForestClassifier(class_weight='balanced', max_depth=10,
                       min_samples_leaf=10, min_samples_split=20,
                       random_state=42)

Parameters: {'n_estimators': 100, 'min_samples_split': 20, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'max_depth': 10, 'class_weight': 'balanced'}

Score: 0.5563197542079444

Best Threshold: 0.40

Balanced Accuracy: 0.6609123048130676
Precision: 0.27745225151031205
Recall: 0.8693090021502877
F1 Score: 0.42064856854008104
MCC Score: 0.2613058941454673
F2 Score: 0.6093414816764121

ROC AUC Score: 0.7589
PR AUC Score: 0.49204530949943776

================================================================================

Histogram-based Gradient Boosting

Model: HistGradientBoostingClassifier(learning_rate=0.3, max_depth=9, max_iter=200,
                               max_leaf_nodes=62, min_samples_leaf=30,
                               random_state=42)

Parameters: {'min_samples_leaf': 30, 'max_leaf_nodes': 62, 'max_iter': 200, 'max_depth': 9, 'learning_rate': 0.3}

Score: 0.2681182624259133

Best Threshold: 0.50

Balanced Accuracy: 0.589959688025581
Precision: 0.7890997520503529
Recall: 0.19235194978787704
F1 Score: 0.3093068677750054
MCC Score: 0.3350613416324715
F2 Score: 0.22662908915620414

ROC AUC Score: 0.7672
PR AUC Score: 0.5131609220720333

================================================================================

Extreme Gradient Boosting

Model: XGBClassifier(base_score=None, booster=None, callbacks=None,
              colsample_bylevel=None, colsample_bynode=None,
              colsample_bytree=1.0, device=None, early_stopping_rounds=None,
              enable_categorical=False, eval_metric=None, feature_types=None,
              feature_weights=None, gamma=None, grow_policy=None,
              importance_type=None, interaction_constraints=None,
              learning_rate=0.05, max_bin=None, max_cat_threshold=None,
              max_cat_to_onehot=None, max_delta_step=None, max_depth=9,
              max_leaves=None, min_child_weight=None, missing=nan,
              monotone_constraints=None, multi_strategy=None, n_estimators=200,
              n_jobs=None, num_parallel_tree=None, ...)

Parameters: {'subsample': 1.0, 'scale_pos_weight': 4, 'n_estimators': 200, 'max_depth': 9, 'learning_rate': 0.05, 'colsample_bytree': 1.0}

Score: 0.5462593426578185

Best Threshold: 0.40

Balanced Accuracy: 0.6875584856692046
Precision: 0.31924658830405717
Recall: 0.7745278084500494
F1 Score: 0.45213228820876256
MCC Score: 0.29754465550290027
F2 Score: 0.6026411248203692

ROC AUC Score: 0.7710
PR AUC Score: 0.5167170279727622
