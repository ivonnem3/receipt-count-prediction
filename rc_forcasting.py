# import libraries
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
from math import sqrt

# Local Path Set Up-IGNORE
path = os.getcwd()
os.chdir('receipt-count-prediction')

# Load Reciept Data
reciept_data = pd.read_csv('data\data_daily.csv')
reciept_data = reciept_data.rename(columns={'# Date':'Date'})
reciept_data.index = pd.to_datetime(reciept_data['Date'],format='%Y-%m-%d')
del reciept_data['Date']
print(reciept_data)

# Train-Test Split
train =  reciept_data[reciept_data.index <= pd.to_datetime("2021-10-19", format='%Y-%m-%d')]
test = reciept_data[reciept_data.index > pd.to_datetime("2021-10-19", format='%Y-%m-%d')]

"""
# Plot
plt.plot(train,color = 'yellowgreen', label = 'Train Data')
plt.plot(test, color = 'crimson', label = 'Test Data')
plt.title('Reciept Count')
plt.xlabel('Date')
plt.ylabel('Reciet Count')
plt.xticks(rotation=45)
plt.show()
"""

# Generate Forcasting Model
from statsmodels.tsa.statespace.sarimax import SARIMAX
y = train['Receipt_Count']
SARIMAXmodel = SARIMAX(y, order = (0,1 , 2), seasonal_order=(0,1,1,12))
SARIMAXmodel = SARIMAXmodel.fit()

y_pred = SARIMAXmodel.get_forecast(len(test.index))
y_pred_df = y_pred.conf_int(alpha = 0.05)
y_pred_df["Predictions"] = SARIMAXmodel.predict(start = y_pred_df.index[0], end = y_pred_df.index[-1])
y_pred_df.index = test.index
y_pred_out = y_pred_df["Predictions"]
plt.plot(train,color = 'yellowgreen', label = 'Train Data')
plt.plot(test, color = 'crimson', label = 'Test Data')
plt.title('Reciept Count')
plt.xlabel('Date')
plt.ylabel('Reciet Count')
plt.xticks(rotation=45)
plt.plot(y_pred_out, color='green', label = 'Predictions')
plt.legend()
plt.show()
arma_rmse = np.sqrt(mean_squared_error(test["Receipt_Count"].values, y_pred_df["Predictions"]))
print("RMSE: ",arma_rmse)

#reciept_model = SARIMAX(train['Receipt_Count'])
#reciept_model = reciept_model.fit()

# Generate Predictions
#y_predict = reciept_model.get_forecast(len(test.index))
#y_predict_df = y_predict.conf_int(alpha = 0.05)
#y_predict_df['Predictions'] = y_predict_df
#y_predict_df.index = test.index
