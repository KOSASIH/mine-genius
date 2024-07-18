import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualization:
    def __init__(self):
        pass

    def plot_correlation_matrix(self, data):
        # Plot correlation matrix using Seaborn
        corr_matrix = data.corr()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
        plt.title('Correlation Matrix')
        plt.show()

    def plot_feature_importances(self, feature_importances):
        # Plot feature importances using Matplotlib
        plt.barh(range(len(feature_importances)), feature_importances)
        plt.xlabel('Feature Importance')
        plt.ylabel('Feature Index')
        plt.title('Feature Importances')
        plt.show()
