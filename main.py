import matplotlib.pyplot as plt
import matplotlib.patches as patches
import data_extraction
import create_models
# import graph_visualization

from data_extraction import load_data, simplify_data, tree_data, linear_data
from create_models import split_data, evaluate_model, find_best_models, get_accuracy, get_precision, get_recall, get_f1_score, get_balanced_accuracy, get_mcc
# from graph_visualization import plot_roc_auc, plot_pr_auc


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

print(results)

# find logistic regression model
lin_model = results["Logisitic Regression"][0]

# predict and evaluate
y_lin_pred = lin_model.predict(test_linear_x)

print("Logisitc Regression")
print("Accuracy: ", evaluate_model(test_linear_y, y_lin_pred, get_accuracy))
print("Precision: ", evaluate_model(test_linear_y, y_lin_pred, get_precision))
print("Recall: ", evaluate_model(test_linear_y, y_lin_pred, get_recall))
print("F1 Score: ", evaluate_model(test_linear_y, y_lin_pred, get_f1_score))
print("Balanced Accuracy: ", evaluate_model(test_linear_y, y_lin_pred, get_balanced_accuracy))
print("MCC Score: ", evaluate_model(test_linear_y, y_lin_pred, get_mcc))

# track names of tree models
tree_names = ["Random Forest", "Histogram-based Gradient Boosting", "Extreme Gradient Boosting"]

# loops through all 3 tree-based models
for i in range(1, 4):

    # find the current tree based model
    model = results[tree_names[i-1]][0]

    # predict and evaluate
    y_pred = model.predict(test_tree_x)

    print(tree_names[i-1])
    print("Accuracy: ", evaluate_model(test_tree_y, y_pred, get_accuracy))
    print("Precision: ", evaluate_model(test_tree_y, y_pred, get_precision))
    print("Recall: ", evaluate_model(test_tree_y, y_pred, get_recall))
    print("F1 Score: ", evaluate_model(test_tree_y, y_pred, get_f1_score))
    print("Balanced Accuracy: ", evaluate_model(test_tree_y, y_pred, get_balanced_accuracy))
    print("MCC Score: ", evaluate_model(test_tree_y, y_pred, get_mcc))
