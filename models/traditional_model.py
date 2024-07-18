import pandas as pd
from sklearn.linear_model import LinearRegression

class TraditionalModel:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, X, y):
        # Train traditional model
        self.model.fit(X, y)

    def predict(self, X):
        # Make predictions using traditional model
        predictions = self.model.predict(X)
        return predictions
