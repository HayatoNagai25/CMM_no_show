import matplotlib.pyplot as plt
import matplotlib.patches as patches
import data_extraction
import create_models

from data_extraction import load_data, simplify_data, tree_data, linear_data
from create_models import linear_model, tree_models

linear_df, l_attendance = linear_data(simplify_data(load_data("data/data2025anon.csv")))
tree_df, t_attendance = tree_data(simplify_data(load_data("data/data2025anon.csv")))
lin_reg_Y = linear_model(linear_df, l_attendance, 1000)
rand_forest_Y, his_gra_boost_Y, x_gra_boost_Y = tree_models(tree_df, t_attendance, 1000)
