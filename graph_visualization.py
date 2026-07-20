import pandas as pd
import matplotlib.pyplot as plt
from sklearn.inspection import permutation_importance
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, roc_auc_score, roc_curve, precision_recall_curve, auc


def plot_confusion_matrix(y_true, y_pred, name):
    """
    Plots the confusion matrix, which is a graph
    that displays the tp, fp, fn, and tn

    Params:
        y_true (Series): the actual attendance status
        y_pred (Series): the predicted attendance status
        name (string): the name of the model

    Returns: None (plots a confusion matrix)
    """
    # find the tp, fp, fn, tn
    cm = confusion_matrix(y_true, y_pred)

    # sets the size of the figure
    _, ax = plt.subplots(figsize=(6,6))

    # displays the confusion matrix
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Show", "No-Show"])
    disp.plot(ax=ax)
    ax.set_title(name + " Confusion Matrix")
    plt.tight_layout()
    plt.show()


def plot_roc_auc(y_true, y_score, name):
    """
    Plots the receiver operating characteristic (ROC) area under the curve graph

    Params:
        y_true (Series) : the actual attendance status
        y_score (Series): the probability of predicting no-show
        name (string): the name of the model

    Returns: None (plots a ROC AUC graph)
    """
    # finds the auc score
    auc_score = roc_auc_score(y_true, y_score)

    print(f"ROC AUC Score: {auc_score:.4f}")

    # computes the receiver operating characteristic
    fpr, tpr, _ = roc_curve(y_true, y_score)

    plt.figure(figsize=(8,6))
    plt.plot(fpr, tpr, color="blue", lw=2, label=f"ROC Curve (AUC = {auc_score:.3f})")
    plt.plot([0, 1], [0, 1], color="gray", linestyle="--", label="Random Guessing")
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title(name + " Receiver Operating Characteristic (ROC)")
    plt.legend(loc="lower right")
    plt.show()


def plot_pr_auc(y_true, y_score, name):
    """
    Plots the precision-recall (PR) area under the curve graph

    Params:
        y_true (Series): the actual attendance status
        y_score (Series): the probablity of predicting no-show
        name (string): the name of the model

    Returns: None (plots a PR AUC graph)
    """
    # calculates the precision and recall
    precision, recall, _ = precision_recall_curve(y_true, y_score)

    # computes the area udner the PR graph
    pr_auc = auc(recall, precision)

    print(f"PR AUC Score: {pr_auc}")

    plt.figure(figsize=(8,6))
    plt.plot(recall, precision, label=f"PR Curve (AUC = {pr_auc:.3f})")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title(name + " Precision-Recall Curve")
    plt.legend(loc="lower left")
    plt.grid(True)
    plt.show()


def plot_feature_importance(train_linear_x, train_tree_x, test_tree_x, test_tree_y, name, model):
    """
    Plots the feature importance bar graph

    Params:
        train_linear_x (DataFrame): the training split of the data for linear models
        train_tree_x (DataFrame): the training split of the data for tree models
        test_tree_x (DataFrame): the test split of the data for tree models
        test_tree_y (Series): the test split of the attendance status for tree models
        name (string): the name of the model
        model: the type of model

    Returns: None (plots the feature importance graph)
    """
    # checks which model it is
    if name == "Logistic Regression":

        # finds the feature importance for Logistic Regression
        importance = pd.Series(model.coef_[0], index=train_linear_x.columns).sort_values()

        # gets the 20 most influential values
        top_20 = importance.reindex(importance.abs().sort_values(ascending=False).index).head(20).sort_values()

    elif name == "Random Forest":

        # finds the feature importance for Random Forest
        importance = pd.Series(model.feature_importances_, index=train_tree_x.columns).sort_values()

        # gets the 20 most infulential values
        top_20 = importance.sort_values(ascending=False).head(20)

    elif name == "Histogram-based Gradient Boosting":

        # finds the feature importance for Histogram-based Gradient Boosting
        result = permutation_importance(model, test_tree_x, test_tree_y, n_repeats=5, random_state=42)
        importance = pd.Series(result.importances_mean, index=test_tree_x.columns).sort_values()

        # gets the 20 most influential values
        top_20 = importance.sort_values(ascending=False).head(20)

    elif name == "Extreme Gradient Boosting":

        # finds the feature importance for Extreme Gradient Boosting
        importance = pd.Series(model.feature_importances_, index=train_tree_x.columns).sort_values()

        # gets the 20 most influential values
        top_20 = importance.sort_values(ascending=False).head(20)

    top_20.plot.barh(figsize=(10,7))
    plt.gca().invert_yaxis()
    plt.title(name + " Feature Importance")
    plt.xlabel("Importance")
    plt.ylabel("Most Important Features")
    plt.tight_layout()
    plt.show()
