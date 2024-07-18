import pandas as pd

class DataLoader:
    def __init__(self):
        self.data_path = 'data/market_data.csv'

    def load_data(self):
        # Load market data from CSV file
        data = pd.read_csv(self.data_path)
        return data
