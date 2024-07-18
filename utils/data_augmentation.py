import pandas as pd
from sklearn.utils import shuffle

class DataAugmentation:
    def __init__(self):
        pass

    def augment_data(self, data):
        # Augment data using random sampling and shuffling
        augmented_data = pd.DataFrame()
        for i in range(10):
            sampled_data = data.sample(frac=0.5, replace=True)
            shuffled_data = shuffle(sampled_data)
            augmented_data = pd.concat([augmented_data, shuffled_data])
        return augmented_data
