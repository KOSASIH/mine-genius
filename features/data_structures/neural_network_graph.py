import numpy as np

class NeuralNetworkGraph:
    def __init__(self, num_layers, num_neurons):
        self.num_layers = num_layers
        self.num_neurons = num_neurons
        self.weights = np.zeros((num_layers, num_neurons, num_neurons))
        self.biases = np.zeros((num_layers, num_neurons))

    def add_layer(self, layer):
        # adds a layer to the neural network graph
        pass

    def add_neuron(self, neuron):
        # adds a neuron to the neural network graph
        pass

    def get_weights(self):
        # returns the weights of the neural network graph
        pass

    def get_biases(self):
        # returns the biases of the neural network graph
        pass
