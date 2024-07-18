import pandas as pd
from sklearn.preprocessing import StandardScaler

class FeatureEngineering:
    def __init__(self):
        self.scaler = StandardScaler()

    def extract_features(self, data):
        # Extract relevant features from data
        features = pd.DataFrame({
            'ean_hash_rate': data['hash_rate'].rolling(window=10).mean(),
            'td_hash_rate': data['hash_rate'].rolling(window=10).std(),
            'ean_energy_consumption': data['energy_consumption'].rolling(window=10).mean(),
            'td_energy_consumption': data['energy_consumption'].rolling(window=10).std(),
            #...
        })
        return features

    def scale_features(self, features):
        # Scale features using StandardScaler
        scaled_features = self.scaler.fit_transform(features)
        return scaled_features
