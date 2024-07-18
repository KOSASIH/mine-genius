import pandas as pd
from sklearn.metrics import mean_absolute_error

class DataQualityControl:
    def __init__(self):
        pass

    def check_data_quality(self, data):
        # Check data quality using mean absolute error
        mae = mean_absolute_error(data['target'], data['prediction'])
        if mae > 0.5:
            print("Data quality is poor!")
        else:
            print("Data quality is good!")
