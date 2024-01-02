import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import keras
from keras.models import Sequential
from keras.layers import Dense, LSTM, Activation, Dropout
from sklearn.preprocessing import MinMaxScaler

class MyLSTM:
    sc_in = MinMaxScaler(feature_range=(0, 1))
    sc_out = MinMaxScaler(feature_range=(0, 1))

    def __init__(self, args):
        self.model = Sequential()
        self.is_model_created = False
        self.hidden_dim = args.hidden_dim
        self.epochs = args.epochs
        self.history = None  # To store training history

    def create_model(self, shape_):
        self.model.add(LSTM(self.hidden_dim, return_sequences=True, input_shape=(1, shape_)))
        self.model.add(LSTM(self.hidden_dim))
        self.model.add(Dense(1))
        self.model.compile(loss='mean_squared_error', optimizer='adam')

    def fit(self, data_x):
        data_x = np.array(data_x)
        train_x = data_x[:, 1:-1]
        train_y = data_x[:, -1]

        if not self.is_model_created:
            self.create_model(train_x.shape[1])
            self.is_model_created = True

        train_x = self.sc_in.fit_transform(train_x)
        train_y = train_y.reshape(-1, 1)
        train_y = self.sc_out.fit_transform(train_y)
        train_x = np.array(train_x, dtype=float)
        train_y = np.array(train_y, dtype=float)
        train_x = np.reshape(train_x, (train_x.shape[0], 1, train_x.shape[1]))
        self.history = self.model.fit(train_x, train_y, epochs=self.epochs, verbose=1, shuffle=False, batch_size=50)

        # Plot training history
        self.plot_training_history()

    def predict(self, test_x):
        test_x = np.array(test_x.iloc[:, 1:], dtype=float)
        test_x = self.sc_in.transform(test_x)
        test_x = np.reshape(test_x, (test_x.shape[0], 1, test_x.shape[1]))
        pred_y = self.model.predict(test_x)
        pred_y = pred_y.reshape(-1, 1)
        pred_y = self.sc_out.inverse_transform(pred_y)
        return pred_y

    def plot_training_history(self):
        if self.history is not None:
            plt.plot(self.history.history['loss'])
            plt.title('Model Loss')
            plt.ylabel('Loss')
            plt.xlabel('Epoch')
            plt.legend(['Train'], loc='upper left')
            plt.show()

# Assuming you have your data loaded into 'data'
# Initialize MyLSTM with appropriate arguments
args = {'hidden_dim': 64, 'epochs': 50}  # Update with your desired values
lstm_model = MyLSTM(args)

# Train the model (pass your data to the fit method)
# lstm_model.fit(your_training_data)
# Example: lstm_model.fit(your_data)

# After training, to plot the graphs, call plot_training_history
# lstm_model.plot_training_history()
