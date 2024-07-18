import pandas as pd
from sklearn.preprocessing import StandardScaler

class DataPreprocessing:
    def __init__(self):
        pass

    def preprocess_data(self, data):
        # Preprocess data using StandardScaler
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(data)
        return scaled_data
