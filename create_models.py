import numpy as np
import random
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from xgboost import XGBClassifier


def linear_model(X, Y, objective_fn, num_trials, SOMETHING):
    """
    Takes in the data and runs the linear logistic regression model with every possible
    combination of SOMETHING and outputs the best average score and the best model
    given the objective function

    Params:
        X (DataFrame): the 16 variables that are being considered to predict no-show
        Y (Series): the actual attendance status
        objective_fn: a fucntion that takes the model's ( true pos, false pos, true neg, false neg)
                        as input and outputs a float value
        num_trials (int): the number of trials to be conducted
        SOMETHING:


    Returns: (avg_score, best_model)
                avg_score is the best average score determined by the objective function and
                best_model is the best model
    """
    # initiate the total score variable
    total_score = 0

    # repeat for the number of trials specified
    for _ in range(num_trials):

        # split the data and train it
        train_X, train_Y, test_X, test_Y = split_data(X, Y)
        model = LogisticRegression()
        model.fit(train_X, train_Y)

        # evalulate the model and add the score to the total
        score = evaluate_model(test_X, test_Y, objective_fn, model)
        total_score += score

    # calculate the average score
    avg_score = total_score/num_trials

    # find the best model
    best_model = model.fit(X, Y)

    return avg_score, best_model


def tree_models(X, Y, objective_fn, num_trials):
    """
    Takes in the data and runs all three tree-based models with every possible combination
    of SOMETHING and outputs the best average score and the best model given the objective
    function for each model

    Params:
        X (DataFrame): the 16 variables that are being considered to predict no-show
        Y (Series): the actual attendance status
        objective_fn: a function that takes the model's (true pos, false pos, true neg, false neg)
                        as input and ouputs a float value
        num_trials (int): the number of trials to be conducted
        SOMETHING:

    Returns: (model_measurements, best_models)
                model_measurements is a dictionary mapping each tree-based model to the best average
                score determined by the objective function and best_models is a list of the best models
    """
    # define all three tree-based models
    models = {"Random Forest": RandomForestClassifier(), "Histogram-Based Gradient Boosting": HistGradientBoostingClassifier(),
              "Extreme Gradient Boosting": XGBClassifier()}
    model_measurements = {}
    best_models = []

    # loop through all models and run each one
    for name, model in models.items():

        # initiate a total score variable
        total_score = 0

        # repeat for the number of trials specified
        for _ in range(num_trials):

            # split the data and train it
            train_X, train_Y, test_X, test_Y = split_data(X, Y)
            model.fit(train_X, train_Y)

            # evaluate the model and add the score to the total
            score = evaluate_model(test_X, test_Y, objective_fn, model)
            total_score += score

        # calculate the average score and record it
        avg_score = total_score/num_trials
        model_measurements[name] = avg_score

        # find the best model and record it
        best_models.append(model.fit(X, Y))

    return model_measurements, best_models


#######################################################################################################
########################################## HELPER FUNCTIONS ###########################################
#######################################################################################################


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
    # split the data into shows and no shows
    show_X = X[Y == 0]
    show_Y = Y[Y == 0]
    no_show_X = X[Y == 1]
    no_show_Y = Y[Y == 1]

    # find the minimum size of both
    minimum = min(len(show_X), len(no_show_X))

    # randomly take the same amount of shows and no-shows
    sampled_show_X = show_X.sample(minimum)
    sampled_show_Y = show_Y[sampled_show_X.index]
    sampled_no_show_X = no_show_X.sample(minimum)
    sampled_no_show_Y = no_show_Y[sampled_no_show_X.index]

    # combine the show and no show back into one Series
    balanced_X = pd.concat([sampled_show_X, sampled_no_show_X])
    balanced_Y = pd.concat([sampled_show_Y, sampled_no_show_Y])

    # use the balanced X and Y and split the data
    train_X, test_X, train_Y, test_Y = train_test_split(balanced_X, balanced_Y)

    return train_X, train_Y, test_X, test_Y


def evaluate_model(val_X, val_Y, objective_fn, model):
    """
    Evaluates the given model according to the provided objective function

    Params:
        val_X (Series): data input to evaluate performance on
        val_Y (Series): data output to evaluate performance on
        objective_fn: a function that takes the model's (true pos, true neg, false pos, false neg)
                        as input and outputs a float value
        model: the type of model used

    Returns: a float of the model's score under the given objective function
    """
    # convert y values to a numpy array
    val_Y = val_Y.to_numpy()

    # uses the specified model to make predicted y values
    prediction = model.predict(val_X)
    tp, fp, tn, fn = 0, 0, 0, 0

    # counts the number of tp, fp, tn, and fn
    for i in range(len(prediction)):
        if prediction[i] == 1 and val_Y[i] == 1:
            tp += 1
        if prediction[i] == 1 and val_Y[i] == 0:
            fp += 1
        if prediction[i] == 0 and val_Y[i] == 0:
            tn += 1
        if prediction[i] == 0 and val_Y[i] == 1:
            fn += 1

    return objective_fn(tp, fp, tn, fn)


#######################################################################################################
######################################### OBJECTIVE FUNCTIONS #########################################
#######################################################################################################


def get_accuracy(tp, fp, tn, fn):
    if (tp + tn + fp + fn) == 0:
        return 0
    else:
        return (tp + tn)/(tp + tn + fp + fn)

def get_precision(tp, fp, tn, fn):
    if (tp + fp) == 0:
        return 0
    else:
        return tp / (tp + fp)

def get_recall(tp, fp, tn, fn):
    if (tp + fn) == 0:
        return 0
    else:
        return tp / (tp + fn)

def get_f1_score(tp, fp, tn, fn):
    if (((tp + fp) == 0) or ((tp + fn) == 0)):
        return 0
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    if (precision + recall) == 0:
        return 0
    else:
        return (2 * precision * recall) / (precision + recall)
