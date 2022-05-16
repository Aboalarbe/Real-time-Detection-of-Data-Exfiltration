import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

def plot_confusion_matrix(y_test, y_pred, model_name)
    cm = confusion_matrix(y_test, y_pred)
    f = sns.heatmap(cm, annot=True, fmt='d')
    plt.savefig('../../reports/figures/' + str(model_name) + '.png')
    
def plot_cls_distribution(data, figure_name):
    data.Label.value_counts().plot(kind='bar');
    plt.title('Distribution of the target label')
    plt.xlabel('Classes')
    plt.ylabel('Count')
    plt.savefig('../../reports/figures/' + str(figure_name) + '.png')