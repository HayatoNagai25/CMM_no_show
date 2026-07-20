import numpy as np
from imblearn.over_sampling import SMOTE
import data_extraction
import create_models
import graph_visualization

from data_extraction import load_data, simplify_data, tree_data, linear_data
from create_models import split_data, find_best_models, print_stats, get_balanced_accuracy, get_precision, get_recall, get_f1_score, get_mcc, get_f2_score
from graph_visualization import plot_confusion_matrix, plot_roc_auc, plot_pr_auc, plot_feature_importance


# extracts data for both lienar and tree models
linear_x, y = linear_data(simplify_data(load_data("data/df2023-2026_anon.csv")))
tree_x, y = tree_data(simplify_data(load_data("data/df2023-2026_anon.csv")))

# split both data types
train_linear_x, test_linear_x, train_linear_y, test_linear_y = split_data(linear_x, y)
train_tree_x, test_tree_x, train_tree_y,  test_tree_y = split_data(tree_x, y)

# Combine X and y
train_tree = train_tree_x.copy()
train_tree["Attendance Status"] = train_tree_y

# Drop rows containing any NaN values
train_tree = train_tree.dropna()

# Split them back apart
train_tree_y = train_tree["Attendance Status"]
train_tree_x = train_tree.drop(columns="Attendance Status")

# # use smote to balance linear data
# smote_linear = SMOTE(random_state=42)
# train_linear_x, train_linear_y = smote_linear.fit_resample(train_linear_x, train_linear_y)

# # use smote to balance tree data
# smote_tree = SMOTE(random_state=42)
# train_tree_x, train_tree_y = smote_tree.fit_resample(train_tree_x, train_tree_y)

# define the objective function
objective_fn = get_f2_score

# define the number of trials
num_trials = 20

# find the best model for each of the four learning model
results = find_best_models(train_linear_x, train_tree_x, train_linear_y, train_tree_y, objective_fn, num_trials)

print("Objective Function: F2 Score")
print()

# prints the stats
lin_model, y_lin_pred, y_lin_score = print_stats(results, test_linear_x, test_linear_y, objective_fn, "Logistic Regression")

# plot graphs
plot_confusion_matrix(test_linear_y, y_lin_pred, "Logistic Regression")
plot_roc_auc(test_linear_y, y_lin_score, "Logistic Regression")
plot_pr_auc(test_linear_y, y_lin_score, "Logistic Regression")
plot_feature_importance(train_linear_x, train_tree_x, test_tree_x, test_tree_y, "Logistic Regression", lin_model)

print()
print("=" * 80)
print()

# track names of tree models
tree_names = ["Random Forest", "Histogram-based Gradient Boosting", "Extreme Gradient Boosting"]

# loops through all 3 tree-based models
for tree_name in tree_names:

    # prints the stats
    model, y_pred, y_score = print_stats(results, test_tree_x, test_tree_y, objective_fn, tree_name)

    # plot graphs
    plot_confusion_matrix(test_tree_y, y_pred, tree_name)
    plot_roc_auc(test_tree_y, y_score, tree_name)
    plot_pr_auc(test_tree_y, y_score, tree_name)
    plot_feature_importance(train_linear_x, train_tree_x, test_tree_x, test_tree_y, tree_name, model)

    print()
    print("=" * 80)
    print()
