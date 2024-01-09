# IITkhg

Authors: Sarvesh Shimpi
         Piyush Motwani
         Rahul Metre
         Shivam Upadhyay

<div align="center">

|          | accuracy_score | f1_score | recall_score | precision_score | MAE    | RMSE     | MAPE   | SMAPE   | MASE   | MSLE    |
|----------|----------------|----------|--------------|-----------------|--------|----------|--------|---------|--------|---------|
| prophet  | 0.7111         | 0.7307   | 0.7358       | 0.7257          | 83.24  | 116.41   | 0.3995 | 0.4006  | 1.71   | 0.0000  |
| xgboost  | 0.5583         | 0.5781   | 0.5686       | 0.5880          | 796.73 | 1115.22  | 3.60   | 3.76    | 15.02  | 0.0035  |
| gru      | 0.5508         | 0.5629   | 0.5595       | 0.5671          | 1140.66| 1424.51  | 5.60   | 5.82    | 25.17  | 0.0080  |
| sarimax  | 0.6981         | 0.7031   | 0.6931       | 0.7135          | 1119.21| 1391.28  | 5.48   | 5.74    | 24.69  | 0.0085  |
| orbit    | 0.6796         | 0.6972   | 0.6936       | 0.7012          | 137.56 | 184.77   | 0.6508 | 0.6551  | 2.78   | 0.0001  |
| random_forest | 0.5769    | 0.5931   | 0.5798       | 0.6076          | 787.25 | 1098.95  | 3.55   | 3.71    | 14.80  | 0.0035  |
| lstm     | 0.5410         | 0.5441   | 0.5289       | 0.5608          | 1140.39| 1434.98  | 5.56   | 5.81    | 25.08  | 0.0082  |

</div>



![Project Image](Output\Capture.JPG)
![Project Image](Output\233840105-ed0ce7bf-8102-4685-a527-d95f032865fd.png)
![Project Image](Output\218425368-6761a215-04f8-43c3-96eb-d2df0468455f.png)
![Project Image](Output\218426854-e6cf9f39-8424-4f56-bc89-7d618e0bb384.png)
![Project Image](Output\233839145-38098f13-ea4d-4b2e-9729-8e399bd883cd.png)

![Project Image](Output\233839167-89c89021-54ce-45d8-9efe-8ce4ad8e88b4.png)
![Project Image](Output\233839178-2bc10b6d-5893-437b-8e03-8a151c4653fa.png)
![Project Image](Output\233839182-04e96f9d-e704-4391-803a-fe1702471d1c.png)
![Project Image](Output\233839189-a66b1f1a-8fc6-4ecd-94ce-19ef75978588.png)
![Project Image](Output\233839202-75b148eb-8204-4603-a3d0-445f1c66dd60.png)
![Project Image](Output\233839221-a937b620-e813-4e2e-bbdc-fa7385bc726d.png)

![Project Image](Output\233840047-686c6ab8-426b-4ce5-aef4-683ab827698e.png)
![Project Image](Output\233840052-ca1cb7fd-a900-4b94-943a-32f85d5a2a95.png)
![Project Image](Output\233840059-c0b4e9c2-c104-4fd4-b5fc-86e790c8a23e.png)
![Project Image](Output\233840067-ada4cc27-af4b-47d8-b1f5-91357e8bccd6.png)
![Project Image](Output\233840072-b06faba5-09a7-4920-95ff-12c6f4f23628.png)
![Project Image](Output\233840080-c7c727a8-87aa-4501-916d-72f8973d1d2e.png)
![Project Image](Output\233840093-6be9522e-b60a-4045-b61c-2cd672b6b9bf.png)

# Dataset

You can use more than 15 cryptocurrencies data by giving the symbol of the selected cryptocurrency to the config files. Moreover, the csv files of these cryptocurrencies could be found in ./data .

<div align="center">

|  Name	     | Symbol |  Name	      | Symbol |  Name	 | Symbol |
| :---:      |  :---: |  :---:      | :---:  | :---:   | :---:  |
| Bitcoin    | XBTUSD | Ethereum    | ETHUSD | BNB     | BNBUSD |
| Cardano    | ADAUSD | Dogecoin    | DOGEUSD| Solana  | SOLUSD |
| Polkadot   | DOTUSD | Litecoin    | LTCUSD | TRON    | TRXUSD |
|Avalanche   | AVAXUSD|Chainlink    | LINKUSD| Aptos   | APTUSD |
|Bitcoin Cash| BCHUSD |NEAR Protocol| NEARUSD| ApeCoin | APEUSD |
|Cronos      | CROUSD |Axie Infinity| AXSUSD | EOS     | EOSUSD |

</div>

# Indicators

In order to have a richer dataset, library provides you with more than 30 indicators. You could select the indicators you want to have in your dataset and the library will calculate them and add them to the dataset.

The list of of available indicators supported by the library is as follow:

<div align="center">

|  Name	                                | Symbol          |  Name	                            | Symbol          |  Name	                            | Symbol   |
| :---:                                 |  :---:          |  :---:                            | :---:           | :---:                             | :---:    |
| Simple Moving Average                 | sma             |  Weighted Moving Average          | wma             | Cumulative Moving Average         | cma      |
| Exponential Moving Average            | ema             |  Double Exponential Moving Average| dema            | Triple Exponential Moving Average | trix     |
| Moving Average Convergence Divergence | macd            |  Stochastic                       | stoch           | KDJ                               | kdj      |
| William %R                            | wpr             |  Relative Strengh Index           | rsi             | Stochastic Relative Strengh Index | srsi     |
|  Chande Momentum Oscillator           | cmo             |  Bollinger Bands                  | bollinger       | Keltner Channel                   | kc       |
| Donchian Channel                      | dc              |  Heiken Ashi                      | heiken          | Ichimoku                          | ichi     |
| Volume Profile                        | vp              |  True Range                       | tr              | Average True Range                | atr      |
| Average Directionnal Index            | adx             |  On Balance Volume                | obv             | Momentum                          | mmt      |
| Rate Of Change                        | roc             |  Aroon                            | aroon           | Chaikin Money Flow                | cmf      |
| Volatility Index                      | vix             | Chopiness Index                   | chop            | Center Of Gravity                 | cog      |


</div>

# Metrics

The essential step in any machine learning model is to evaluate the accuracy of the model. The list of of available metrics supported by the library is as follow:


* accuracy_score: Number of correct predictions/Total number of predictions
* precision_score:  the proportion of positively predicted labels that are actually correct
* recall_score: the model's ability to correctly predict the positives out of actual positives
* f1_score: 2.Precision.Recall/(Precision+Recall)
* MAE: Mean Absolute Error
* MAPE: Mean Absolute Percentage Error
* MASE: Mean Absolute Scaled Error
* RMSE: Root Mean Square Error
* SMAPE: Symmetric Mean Absolute Percentage Error
* Stochastic: the possibility that the outcome is not that expected, given that both the model and parameters are correct 

# To Execute
To execute a prediction, you need a virtual env with python3.7