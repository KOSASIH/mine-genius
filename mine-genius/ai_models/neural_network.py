import numpy as np

class NeuralNetwork:
    def __init__(self, input_dim, hidden_dim, output_dim):
        self.weights1 = np.random.rand(input_dim, hidden_dim)
        self.weights2 = np.random.rand(hidden_dim, output_dim)

    def forward(self, X):
        # implements forward pass
        pass

    def backward(self, X, y):
        # implements backward pass
        pass

    def train(self, X, y):
        # implements training loop
        pass
