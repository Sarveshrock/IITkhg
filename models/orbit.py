from orbit.orbit.models import DLT
import numpy as np
from sklearn.preprocessing import MaxAbsScaler
import matplotlib as plt


class Orbit:
    model = None
    sc_in = MaxAbsScaler()
    sc_out = MaxAbsScaler()

    def __init__(self, args):
        self.response_col = args.response_col
        self.date_col = args.date_col
        self.estimator = args.estimator
        self.seasonality = args.seasonality
        self.seed = args.seed
        self.global_trend_option = args.global_trend_option
        self.n_bootstrap_draws = args.n_bootstrap_draws

    def fit(self, data_x):
        print(data_x.shape)
        regressors = []
        for col in data_x.columns:
            if col != self.response_col and col != self.date_col:
                regressors.append(col)
        data_x[regressors] = data_x[regressors].astype(float)
        data_x[self.response_col] = data_x[self.response_col].astype(float)

        data_x.loc[:, regressors] = self.sc_in.fit_transform(data_x.loc[:, regressors])
        data_x.loc[:, self.response_col] = self.sc_out.fit_transform(
            data_x.loc[:, self.response_col].values.reshape(-1, 1))

        self.model = DLT(
            response_col=self.response_col,
            date_col=self.date_col,
            regressor_col=regressors,
            estimator=self.estimator,
            seasonality=self.seasonality,
            seed=self.seed,
            global_trend_option=self.global_trend_option,
            # for prediction uncertainty
            n_bootstrap_draws=self.n_bootstrap_draws,
        )

        self.model.fit(data_x, point_method="mean")

    def predict(self, test_x):
        regressors = []
        for col in test_x.columns:
            if col != self.response_col and col != self.date_col:
                regressors.append(col)
        test_x[regressors] = test_x[regressors].astype(float)

        test_x.loc[:, regressors] = self.sc_in.transform(test_x.loc[:, regressors])
        # test_x[self.response_col] = test_x[self.response_col].astype(float)
        predicted_df = self.model.predict(df=test_x)
        predicted_df.loc[:, 'prediction'] = self.sc_out.inverse_transform(
            predicted_df.loc[:, 'prediction'].values.reshape(-1, 1))
        return np.array(predicted_df.prediction)
    def fit(self, data_x):
        self.model.fit(data_x, point_method="mean")
        loss_history = []
        predicted_values = []
        loss_history.append(self.model._optimizer._trace)
        predicted_values.append(self.model.predict(df=data_x))
        for i, loss_trace in enumerate(loss_history):
                plt.plot(loss_trace, label=f'Iteration {i+1}')
        plt.title('Training Loss History')
        plt.xlabel('Iterations')
        plt.ylabel('Loss')
        plt.legend()
        plt.show()

        # Plot predicted vs. actual values
        actual_values = data_x[self.response_col].values
        for i, pred_values in enumerate(predicted_values):
            plt.plot(actual_values, label='Actual Values')
            plt.plot(pred_values, label=f'Predicted Values (Iteration {i+1})')
            plt.title('Predicted vs. Actual Values')
            plt.xlabel('Time')
            plt.ylabel('Value')
            plt.legend()
            plt.show()

