import matplotlib.pyplot as plt
import matplotlib.patches as patches
import data_extraction
import create_models
import graph_visualization

from data_extraction import load_data, simplify_data, tree_data, linear_data
from create_models import split_data, find_best_models, get_accuracy, get_precision, get_recall, get_f1_score, get_balanced_accuracy, get_mcc
from graph_visualization import plot_roc_auc, plot_pr_auc


# extracts data for both lienar and tree models
linear_x, y = linear_data(simplify_data(load_data("data/data2025anon.csv")))
tree_x, y = tree_data(simplify_data(load_data("data/data2025anon.csv")))

# split both data types
train_linear_x, train_linear_y, test_linear_x, test_linear_y = split_data(linear_x, y)
train_tree_x, train_tree_y, test_tree_x, test_tree_y = split_data(tree_x, y)

# define the objective function
objective_fn = get_f1_score()

# define the number of trials
num_trials = 100

# find the best model for each of the four learning model
results = find_best_models(train_linear_x, train_tree_x, train_linear_y, train_tree_y, objective_fn, num_trials)

print(results)
