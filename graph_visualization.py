import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score, roc_curve, precision_recall_curve, auc


def plot_roc_auc(y_true, y_scores):
    """


    Params:
        y_true:
        y_scores:

    Returns: None (plots a ROC AUC graph)
    """
    auc_score = roc_auc_score(y_true, y_scores)

    print(f"ROC AUC Score: {auc_score:.4f}")

    fpr, tpr, _ = roc_curve(y_true, y_scores)

    roc_auc = auc(fpr, tpr)

    plt.figure(figsize=(8,6))
    plt.plot(fpr, tpr, color="blue", lw=2, label="ROC Curve")
    plt.plot([0, 1], [0, 1], color="gray", linestyle="--", label="Random Guessing")

    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("Receiver Operation Characteristic (ROC)")
    plt.legend(loc="Lower Right")
    plt.show()


def plot_pr_auc(y_true, y_scores):
    """


    Params:
        y_true:
        y_scores:

    Returns: None (plots a PR AUC graph)
    """
    precision, recall, _ = precision_recall_curve(y_true, y_scores)

    pr_auc = auc(recall, precision)

    print(f"PR AUC Score: {pr_auc}")

    plt.figure(figsize=(6, 5))
    plt.plot(recall, precision, label="PR Curve")

    baseline = sum(y_test) / len(y_test)
    plt.axhline(y=baseline, color="red", linestyle="--", label="Baseline")

    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title("Precision-Recall Curve")
    plt.legend(loc="Lower Left")
    plt.grid(True)
    plt.show()
