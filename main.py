import data_extraction
import create_models
import graph_visualization

from data_extraction import load_data, simplify_data, tree_data, linear_data
from create_models import split_data, evaluate_model, find_best_models, get_balanced_accuracy, get_precision, get_recall, get_f1_score, get_mcc
from graph_visualization import plot_confusion_matrix, plot_roc_auc, plot_pr_auc, plot_feature_importance


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

    # find the current tree based model
    model = results[tree_name][0]

    print("Model:", model)
    print()
    print("Parameters:", results[tree_name][1])
    print()
    print("Score:", results[tree_name][2])
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

    # plot graphs
    plot_confusion_matrix(test_tree_y, y_pred, tree_name)
    plot_roc_auc(test_tree_y, y_score, tree_name)
    plot_pr_auc(test_tree_y, y_score, tree_name)
    plot_feature_importance(train_linear_x, train_tree_x, test_tree_x, test_tree_y, tree_name, model)
