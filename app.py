import os
import sys
from ai_models.predictive_model import PredictiveModel
from optimization.mining_process_optimizer import MiningProcessOptimizer

def main():
    # Load market data
    market_data = pd.read_csv('data/market_data.csv')

    # Initialize predictive model
    predictive_model = PredictiveModel()
    predictions = predictive_model.predict(market_data)

    # Initialize mining process optimizer
    mining_optimizer = MiningProcessOptimizer()
    optimized_mining_process = mining_optimizer.optimize(predictions)

    # Save optimized mining process to file
    with open('optimized_mining_process.json', 'w') as f:
        json.dump(optimized_mining_process, f)

if __name__ == '__main__':
    main()
