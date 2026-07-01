from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import confusion_matrix, make_scorer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from xgboost import XGBClassifier


def split_data(X, Y):
    """
    Ensures data represents show and no show an equal amount and
    then splits the data randomly into a train and test group

    Params:
        X (DataFrame): the 16 variables that are being considered to predict no-show
        Y (Series): the actual attendance status

    Returns: (train_X, train_Y, test_X, test_Y)
                a tuple containing the variable values for training (train_X),
                the attendance status for those values (train_Y), the variable
                values for testing (test_X), and the attendance status for
                those values (test_Y)
    """
    # split the data
    train_X, test_X, train_Y, test_Y = train_test_split(X, Y, stratify=Y)

    return train_X, test_X, train_Y, test_Y


def evaluate_model(y_true, y_pred, objective_fn):
    """
    Evaluates the given model according to the provided objective function

    Params:
        y_true (Series): the actual y values
        y_pred (Series): the predicted y values
        objective_fn: a function that takes the model's (true neg, false pos, false neg, true pos)
                        as input and outputs a float value

    Returns: a float of the model's score under the given objective function
    """
    # find the nubmer of tp, fp, tn, and fn
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

    return objective_fn(tn, fp, fn, tp)


def find_best_models(linear_X, tree_X, linear_Y, tree_Y, objective_fn, num_trials):
    """
    Takes in the data and runs the all four models with every possible combinatoon of each parameter

    Params:
        linear_X (DataFrame): the 16 variables that are being considered to predict no-show for
                              linear models
        tree_X (DataFrame): the 16 variables that are beign considered to predict no-show for
                            tree models
        linear_Y (Series): the actual attendance status for linear models
        tree_Y (Series): the actual attendance status for tree models
        objective_fn: a function that takes the model's (true neg, false pos, false neg, true pos)
                        as input and outputs a float value
        num_trials (int): the number of trials to be conducted

    Returns: a dictionary of the results of each of the four models

    """
    # create a results dictionary
    results = {}

    # compute the best logistic regression model and add to results
    lr_model, lr_params, lr_score = logistic_regression(linear_X, linear_Y, objective_fn, num_trials)
    results["Logistic Regression"] = (lr_model, lr_params, lr_score)

    # compute the best random forest model and add to results
    rf_model, rf_params, rf_score = random_forest(tree_X, tree_Y, objective_fn, num_trials)
    results["Random Forest"] = (rf_model, rf_params, rf_score)

    # compute the best histogram-based gradient boosting model and add to results
    hgb_model, hgb_params, hgb_score = hist_grad_boost(tree_X, tree_Y, objective_fn, num_trials)
    results["Histogram-based Gradient Boosting"] = (hgb_model, hgb_params, hgb_score)

    # compute the best extreme gradient boosting model and add to results
    xgb_model, xgb_params, xgb_score = x_grad_boost(tree_X, tree_Y, objective_fn, num_trials)
    results["Extreme Gradient Boosting"] = (xgb_model, xgb_params, xgb_score)

    return results


#######################################################################################################
########################################## HELPER FUNCTIONS ###########################################
#######################################################################################################


def search_model(val_X, val_Y, params, objective_fn, num_trials, model):
    """
    Finds the optimal parameters that gives the best score and creates a model based on these parameters

    Params:
        val_X (Series): data input to evaluate performance on
        val_Y (Series): data output to evaluate performance on
        params (list): all the variations in each parameter
        objective_fn: a function that takes the model's (true neg, false pos, false neg, true pos)
                        as input and outputs a float value
        num_trials (int): the number of trials to be conducted
        model: the type of model used

        Returns: (search.best_estimator_, search.best_params_, search.best_score_)
                    a tuple containing the best model, the parameters for the best model, and the best
                    model's score
    """
    # creates the scorer
    scorer = make_scorer(evaluate_model, objective_fn=objective_fn)

    # uses randomized search CV to find the optimal parameter conditions
    search = RandomizedSearchCV(model, param_distributions=params, n_iter=num_trials, scoring=scorer, n_jobs = -1, cv=3, random_state=42)

    # uses the optimal model and fits to data
    search.fit(val_X, val_Y)

    return search.best_estimator_, search.best_params_, search.best_score_


def logistic_regression(val_X, val_Y, objective_fn, num_trials):
    """
    Searches for the best logistic regression model given a set of differing
    parameters and based on a score given by an objective function

    Params:
        val_X (DataFrame): the 16 variables that are being considered to predict no-show for
                        linear models
        val_Y (Series): the actual attendance status
        objective_fn: a function that takes the model's (true neg, false pos, false neg, true pos)
                        as input and outputs a float value
        num_trials (int): the number of trials to be conducted

    Returns: (best_model, parameters, score)
                best_model is the best model given the set of parameters, and measured by the score
    """
    # the parameters to test
    params = {"C": [0.01, 0.1, 1, 10, 100],
              "class_weight": ["balanced", None, {0: 1, 1: 1}, {0: 1, 1: 2},
                               {0: 1, 1: 3}, {0: 1, 1: 4}, {0: 1, 1: 5}]}

    # finds the best model, its parameters, and its score
    best_model, parameters, score = search_model(val_X, val_Y, params, objective_fn, num_trials, LogisticRegression(max_iter=1000, random_state=42))

    return best_model, parameters, score


def random_forest(val_X, val_Y, objective_fn, num_trials):
    """
    Searches for the best random forest regression model given a set of
    differing parameters and based on a score given by an objective function

    Params:
        vall_X (DataFrame): the 16 variables that are being considered to predict no-show for
                        linear models
        val_Y (Series): the actual attendance status
        objective_fn: a function that takes the model's (true neg, false pos, false neg, true pos)
                        as input and outputs a float value
        num_trials (int): the number of trials to be conducted

    Returns: (best_model, parameters, score)
                best_model is the best model given the set of parameters, and measured by the score
    """
    # the parameters to test
    params = {"n_estimators": [100, 200, 500],
              "max_features": ["sqrt", "log2", None],
              "max_depth": [None, 10, 20, 30],
              "min_samples_leaf": [1, 5, 10],
              "class_weight": ["balanced", "balanced_subsample", None]}

    # finds the best model, its parameters, and its score
    best_model, parameters, score = search_model(val_X, val_Y, params, objective_fn, num_trials, RandomForestClassifier(random_state=42))

    return best_model, parameters, score


def hist_grad_boost(val_X, val_Y, objective_fn, num_trials):
    """
    Searches for the best histogram-based gradient boosting model given a set
    of differing parameters and based on a score given by an objective function

    Params:
        val_X (DataFrame): the 16 variables that are being considered to predict no-show for
                        linear models
        val_Y (Series): the actual attendance status
        objective_fn: a function that takes the model's (true neg, false pos, false neg, true pos)
                        as input and outputs a float value
        num_trials (int): the number of trials to be conducted

    Returns: (best_model, parameters, score)
                best_model is the best model given the set of parameters, and measured by the score
    """
    # the parameters to test
    params = {"learning_rate": [0.01, 0.05, 0.1, 0.3],
              "max_iter": [100, 200, 300],
              "max_depth": [None, 3, 9, 15],
              "max_leaf_nodes": [31, 62, 124],
              "min_samples_leaf": [10, 20, 30]}

    # finds the best model, its parameters, and its score
    best_model, parameters, score = search_model(val_X, val_Y, params, objective_fn, num_trials, HistGradientBoostingClassifier(random_state=42))

    return best_model, parameters, score


def x_grad_boost(val_X, val_Y, objective_fn, num_trials):
    """
    Searches for the best extreme gradient boosting model given a set of
    differing parameters and based on a score given by an objective function

    Params:
        val_X (DataFrame): the 16 variables that are being considered to predict no-show for
                        linear models
        val_Y (Series): the actual attendance status
        objective_fn: a function that takes the model's (true neg, false pos, false neg, true pos)
                        as input and outputs a float value
        num_trials (int): the number of trials to be conducted

    Returns: (best_model, parameters, score)
                best_model is the best model given the set of parameters, and measured by the score
    """
    # the parameters to test
    params = {"learning_rate": [0.01, 0.05, 0.1, 0.3],
              "n_estimators": [100, 200,300],
              "max_depth": [3, 6, 9],
              "subsample": [0.7, 0.9, 1.0],
              "colsample_bytree": [0.7, 0.9, 1.0],
              "scale_pos_weight": [1, 2, 4]}

    # finds the best model, its parameters, and its score
    best_model, parameters, score = search_model(val_X, val_Y, params, objective_fn, num_trials, XGBClassifier(random_state=42))

    return best_model, parameters, score


#######################################################################################################
######################################### OBJECTIVE FUNCTIONS #########################################
#######################################################################################################


def get_accuracy(tn, fp, fn, tp):
    if (tp + tn + fp + fn) == 0:
        return 0
    return (tp + tn)/(tp + tn + fp + fn)


def get_precision(tn, fp, fn, tp):
    if (tp + fp) == 0:
        return 0
    return tp / (tp + fp)


def get_recall(tn, fp, fn, tp):
    if (tp + fn) == 0:
        return 0
    return tp / (tp + fn)


def get_f1_score(tn, fp, fn, tp):
    if (tp + fp == 0 or tp + fn == 0):
        return 0
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    if (precision + recall) == 0:
        return 0
    return (2 * precision * recall) / (precision + recall)


def get_balanced_accuracy(tn, fp, fn, tp):
    if (tp + fn == 0 or tn + fp == 0):
        return 0
    sensitivity = tp / (tp + fn)
    specificity = tn / (tn + fp)
    return (sensitivity + specificity) / 2


def get_mcc(tn, fp, fn, tp):
    den = (tp + fp) * (tp + fn) * (tn + fp) * (tn + fn)
    if den == 0:
        return 0
    return ((tp * tn) - (fp * fn)) / (den ** 0.5)
