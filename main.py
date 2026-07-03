import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from sklearn.inspection import permutation_importance
import data_extraction
import create_models
import graph_visualization

from data_extraction import load_data, simplify_data, tree_data, linear_data
from create_models import split_data, evaluate_model, find_best_models, get_balanced_accuracy, get_precision, get_recall, get_f1_score, get_mcc
from graph_visualization import plot_roc_auc, plot_pr_auc


# extracts data for both lienar and tree models
linear_x, y = linear_data(simplify_data(load_data("data/df2023-2026_anon.csv")))
tree_x, y = tree_data(simplify_data(load_data("data/df2023-2026_anon.csv")))

# split both data types
train_linear_x, test_linear_x, train_linear_y, test_linear_y = split_data(linear_x, y)
train_tree_x, test_tree_x, train_tree_y,  test_tree_y = split_data(tree_x, y)

# define the objective function
objective_fn = get_f1_score

# define the number of trials
num_trials = 10

# find the best model for each of the four learning model
results = find_best_models(train_linear_x, train_tree_x, train_linear_y, train_tree_y, objective_fn, num_trials)

print("Logistic Regression")
print()

# find logistic regression model
lin_model = results["Logistic Regression"][0]

print("Model:", lin_model)
print()
print("Parameters:", results["Logistic Regression"][1])
print()
print("Score:", results["Logistic Regression"][2])
print()

# displays the influnece of each variable
importance = pd.Series(lin_model.coef_[0], index=train_linear_x.columns).sort_values()

# positive increases no-show probability, negative decreases no show probability
print(importance)
print()

# predict and evaluate
y_lin_pred = lin_model.predict(test_linear_x)

print("Balanced Accuracy:", evaluate_model(test_linear_y, y_lin_pred, get_balanced_accuracy))
print("Precision:", evaluate_model(test_linear_y, y_lin_pred, get_precision))
print("Recall:", evaluate_model(test_linear_y, y_lin_pred, get_recall))
print("F1 Score:", evaluate_model(test_linear_y, y_lin_pred, get_f1_score))
print("MCC Score:", evaluate_model(test_linear_y, y_lin_pred, get_mcc))
print()

# find the prediction probability
y_lin_score = lin_model.predict_proba(test_linear_x)[:, 1]

# plot roc graphs
plot_roc_auc(test_linear_y, y_lin_score)
plot_pr_auc(test_linear_y, y_lin_score)

# track names of tree models
tree_names = ["Random Forest", "Histogram-based Gradient Boosting", "Extreme Gradient Boosting"]

# loops through all 3 tree-based models
for tree_name in tree_names:

    print(tree_name)

    # find the current tree based model
    model = results[tree_name][0]

    print("Model:", model)
    print()
    print("Parameters:", results[tree_name][1])
    print()
    print("Score:", results[tree_name][2])
    print()


    # finds importance for Random Forest
    if tree_name == "Random Forest":
        importance = pd.Series(model.feature_importances_, index=train_tree_x.columns).sort_values()

    # finds importance for Histogram-based Gradient Boosting
    elif tree_name == "Histogram-based Gradient Boosting":
        result = permutation_importance(model, test_tree_x, test_tree_y, n_repeats=5, random_state=42)
        importance = pd.Series(result.importances_mean, index=test_tree_x.columns).sort_values()

    # finds importance for Extreme Gradient Boosting
    elif tree_name == "Extreme Gradient Boosting":
        importance = pd.Series(model.feature_importances_, index=train_tree_x.columns).sort_values()

    print(importance)
    print()

    # predict and evaluate
    y_pred = model.predict(test_tree_x)


    print("Balanced Accuracy:", evaluate_model(test_tree_y, y_pred, get_balanced_accuracy))
    print("Precision:", evaluate_model(test_tree_y, y_pred, get_precision))
    print("Recall:", evaluate_model(test_tree_y, y_pred, get_recall))
    print("F1 Score:", evaluate_model(test_tree_y, y_pred, get_f1_score))
    print("MCC Score:", evaluate_model(test_tree_y, y_pred, get_mcc))
    print()

    # find the prediction probability
    y_score = model.predict_proba(test_tree_x)[:, 1]

    # plot roc graphs
    plot_roc_auc(test_tree_y, y_score)
    plot_pr_auc(test_tree_y, y_score)
