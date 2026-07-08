import numpy as np
from imblearn.over_sampling import SMOTENC
import data_extraction
import create_models
import graph_visualization

from data_extraction import load_data, simplify_data, tree_data, linear_data
from create_models import split_data, find_best_models, print_stats, get_balanced_accuracy, get_precision, get_recall, get_f1_score, get_mcc, evaluate_model
from graph_visualization import plot_confusion_matrix, plot_roc_auc, plot_pr_auc, plot_feature_importance


# extracts data for both lienar and tree models
linear_x, y = linear_data(simplify_data(load_data("data/df2023-2026_anon.csv")))
tree_x, y = tree_data(simplify_data(load_data("data/df2023-2026_anon.csv")))

# split both data types
train_linear_x, test_linear_x, train_linear_y, test_linear_y = split_data(linear_x, y)
train_tree_x, test_tree_x, train_tree_y,  test_tree_y = split_data(tree_x, y)

# # define the inbalanced learning function
# smote = SMOTENC(random_state=42)

# # create new no show cases to balance the data sets
# train_linear_x, train_linear_y = smote.fit_resample(train_linear_x, train_linear_y)
# train_tree_x, train_tree_y = smote.fit_resample(train_tree_x, train_tree_y)

# define the objective function
objective_fn = get_f1_score

# define the number of trials
num_trials = 5

# find the best model for each of the four learning model
results = find_best_models(train_linear_x, train_tree_x, train_linear_y, train_tree_y, objective_fn, num_trials)

print("Objective Function: F1 Score")
print()

print("Logistic Regression")
print()

# # prints the stats
# lin_model, y_lin_pred = print_stats(results, test_linear_x, test_linear_y, "Logistic Regression")

# # find the prediction probability
# y_lin_score = lin_model.predict_proba(test_linear_x)[:, 1]

lin_model = results["Logistic Regression"][0]

y_lin_score = lin_model.predict_prob(test_linear_x)[:, 1]

best_threshold = 0.5
best_f1 = -1

thresholds = np.arange(0.05, 0.96, 0.05)
scores = []

for threshold in thresholds:
    y_lin_pred = (y_lin_score >= threshold).astype(int)

    f1 = evaluate_model(test_linear_y, y_lin_pred, get_f1_score)

    if f1 > best_f1:
        best_f1 = f1
        best_threshold = threshold

print(f"Best Threshold: {best_threshold:.2f}")
print(f"Best F1: {best_f1:.4f}")
print()

y_lin_pred = (y_lin_score >= threshold).astype(int)

print("Balanced Accuracy:", evaluate_model(test_linear_y, y_lin_pred, get_balanced_accuracy))
print("Precision:", evaluate_model(test_linear_y, y_lin_pred, get_precision))
print("Recall:", evaluate_model(test_linear_y, y_lin_pred, get_recall))
print("F1 Score:", evaluate_model(test_linear_y, y_lin_pred, get_f1_score))
print("MCC:", evaluate_model(test_linear_y, y_lin_pred, get_mcc))

# plot graphs
plot_confusion_matrix(test_linear_y, y_lin_pred, "Logistic Regression")
plot_roc_auc(test_linear_y, y_lin_score, "Logistic Regression")
plot_pr_auc(test_linear_y, y_lin_score, "Logistic Regression")
plot_feature_importance(train_linear_x, train_tree_x, test_tree_x, test_tree_y, "Logistic Regression", lin_model)

# track names of tree models
tree_names = ["Random Forest", "Histogram-based Gradient Boosting", "Extreme Gradient Boosting"]

# loops through all 3 tree-based models
for tree_name in tree_names:

    print(tree_name)
    print()

    # # prints the stats
    # model, y_pred = print_stats(results, test_tree_x, test_tree_y, tree_name)

    # # find the prediction probability
    # y_score = model.predict_proba(test_tree_x)[:, 1]

    model = results[tree_name][0]

    y_score = model.predict_prob(test_tree_x)[:, 1]

    best_threshold = 0.5
    best_f1 = -1

    thresholds = np.arange(0.05, 0.96, 0.05)
    scores = []

    for threshold in thresholds:
        y_pred = (y_score >= threshold).astype(int)

        f1 = evaluate_model(test_tree_y, y_pred, get_f1_score)

        if f1 > best_f1:
            best_f1 = f1
            best_threshold = threshold

    print(f"Best Threshold: {best_threshold:.2f}")
    print(f"Best F1: {best_f1:.4f}")
    print()

    y_pred = (y_score >= threshold).astype(int)

    print("Balanced Accuracy:", evaluate_model(test_tree_y, y_pred, get_balanced_accuracy))
    print("Precision:", evaluate_model(test_tree_y, y_pred, get_precision))
    print("Recall:", evaluate_model(test_tree_y, y_pred, get_recall))
    print("F1 Score:", evaluate_model(test_tree_y, y_pred, get_f1_score))
    print("MCC:", evaluate_model(test_tree_y, y_pred, get_mcc))

    # plot graphs
    plot_confusion_matrix(test_tree_y, y_pred, tree_name)
    plot_roc_auc(test_tree_y, y_score, tree_name)
    plot_pr_auc(test_tree_y, y_score, tree_name)
    plot_feature_importance(train_linear_x, train_tree_x, test_tree_x, test_tree_y, tree_name, model)
