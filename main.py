import matplotlib.pyplot as plt
import matplotlib.patches as patches
import data_extraction
import create_models
import graph_visualization

from data_extraction import load_data, simplify_data, tree_data, linear_data
from create_models import linear_model, tree_models, get_all, get_accuracy, get_precision, get_recall, get_f1_score, get_balanced_accuracy, get_mcc
from graph_visualization import plot_roc_auc, plot_pr_auc


linear_x, y = linear_data(simplify_data(load_data("data/data2025anon.csv")))
tree_x, y = tree_data(simplify_data(load_data("data/data2025anon.csv")))
lin_reg_Y = linear_model(linear_x, y, 1000)
rand_forest_Y, his_gra_boost_Y, x_gra_boost_Y = tree_models(tree_x, y, 1000)
