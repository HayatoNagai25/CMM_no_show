# Trial Runs

## First Trial

**Output**

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

**Error**
Wrong indexing through results dictionary, so could not print scores for test values
