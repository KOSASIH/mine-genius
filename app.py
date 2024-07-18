import os
import sys
from ai_models.predictive_model import PredictiveModel
from ai_models.deep_learning_model import DeepLearningModel
from optimization.mining_process_optimizer import MiningProcessOptimizer
from optimization.energy_efficiency_optimizer import EnergyEfficiencyOptimizer
from optimization.genetic_algorithm_optimizer import GeneticAlgorithmOptimizer
from models.ensemble_model import EnsembleModel
from utils.data_loader import DataLoader
from utils.data_visualization import DataVisualization

def main():
    # Load market data
    data_loader = DataLoader()
    market_data = data_loader.load_data()

    # Extract features
    feature_engineering = FeatureEngineering()
    features = feature_engineering.extract_features(market_data)

    # Scale features
    scaled_features = feature_engineering.scale_features(features)

    # Train predictive model
    predictive_model = PredictiveModel()
    predictive_model.train(scaled_features, market_data['target'])

    # Train deep learning model
    deep_learning_model = DeepLearningModel()
    deep_learning_model.train(scaled_features, market_data['target'])

    # Train ensemble model
    ensemble_model = EnsembleModel()
    ensemble_model.train(scaled_features, market_data['target'])

    # Optimize mining process
    mining_optimizer = MiningProcessOptimizer()
    optimized_mining_process = mining_optimizer.optimize(predictive_model.predict(scaled_features))

    # Optimize energy efficiency
    energy_optimizer = EnergyEfficiencyOptimizer()
    optimized_energy_efficiency = energy_optimizer.optimize(predictive_model.predict(scaled_features))

    # Optimize using genetic algorithm
    genetic_optimizer = GeneticAlgorithmOptimizer()
    optimized_genetic_algorithm = genetic_optimizer.optimize(predictive_model.predict(scaled_features))

    # Visualize data
    data_visualization = DataVisualization()
    data_visualization.plot_correlation_matrix(market_data)
    data_visualization.plot_feature_importances(predictive_model.feature_importances_)

if __name__ == '__main__':
    main()
