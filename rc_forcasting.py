# import libraries
import os
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
reciept_data['# Date'] = pd.to_datetime(reciept_data['# Date'],format='%Y-%m-%d')
reciept_data.set_index('# Date', inplace=True)

# Train-Test Split
train =  reciept_data[reciept_data.index <= "2021-10-19"]
test = reciept_data[reciept_data.index > "2021-10-19"]

"""
# Plot
plt.plot(train,color = 'yellowgreen', label = 'Train Data')
plt.plot(test, color = 'crimson', label = 'Test Data')
plt.title('Reciept Count')
plt.xlabel('Date')
plt.ylabel('Reciet Count')
plt.xticks(rotation=45)
plt.title("Reciept Count Data")
plt.show()
"""

# Generate Forcasting Model
reciept_model = SARIMAX(train['Receipt_Count'], order = (1, 0, 1))
reciept_model = reciept_model.fit()

# Generate Predictions
y_predict = reciept_model.get_forecast(len(test.index))
y_predict_df = y_predict.conf_int(alpha = 0.05)
y_predict_df['Predictions'] = y_predict_df
y_predict_df.index = test.index
