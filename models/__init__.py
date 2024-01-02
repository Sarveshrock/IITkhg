import matplotlib.pyplot as plt
from Neural_Prophet import neural_prophet
from neuralprophet import NeuralProphet


MODELS = {
    'random_forest': RandomForest,
    'sarimax': Sarimax,
    'orbit': Orbit,
    'lstm': MyLSTM,
    'gru': MyGRU,
    'arima': MyARIMA,
    'prophet': MyProphet,
    'xgboost': MyXGboost,
    'neural_prophet': Neural_Prophet
}

# Extract model names and their corresponding classes
model_names = list(MODELS.keys())
model_classes = [MODELS[model_name] for model_name in model_names]

plt.figure(figsize=(10, 6))
plt.barh(model_names, [1] * len(model_names), align='center')
plt.xlabel('Models')
plt.title('Available Models')

plt.show()
