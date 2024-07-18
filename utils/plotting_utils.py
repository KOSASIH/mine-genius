import matplotlib.pyplot as plt

class PlottingUtils:
    def __init__(self):
        pass

    def plot_predictions(self, predictions):
        # Plot predictions using Matplotlib
        plt.plot(predictions)
        plt.xlabel('Time')
        plt.ylabel('Predicted Value')
        plt.title('Predicted Values Over Time')
        plt.show()
