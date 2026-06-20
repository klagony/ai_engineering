from sklearn.metrics import f1_score, accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def evaluate_pred(true, predictions):
    true_labels = true["label"].tolist()
    pred_labels = [item["label"] for item in predictions]

    accuracy = accuracy_score(true_labels, pred_labels)
    macro_f1 = f1_score(true_labels, pred_labels, average='macro')

    print("Classification Report:")
    print(classification_report(true_labels, pred_labels))

    print("Confusion Matrix:")
    cm = confusion_matrix(true_labels, pred_labels, labels=list(set(true_labels)))
    sns.heatmap(cm, cmap='coolwarm', annot=True, fmt='d', xticklabels=list(set(true_labels)), yticklabels=list(set(true_labels)))
    plt.xlabel('Predicted Labels')
    plt.ylabel('True Labels')
    plt.title('Confusion Matrix')

    return accuracy, macro_f1