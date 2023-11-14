# Receipt Count Prediction


## Intro
Receipt scanning apps are mobile application that allow users to capture and digitize receipts using their mobile smartphone in exchange for some reward. Many of these apps make their money by doing affiliate marketing or forming partnerships with brands.  

One of the most popular receipt scanning apps is Fetch. One of Fetch KPIs focuses on monitoring the number of scanned receipts to the app on a daily bases. This project focuses on being able to predict the possible number of scanned receipts for a given future month.


## Approach
Given the size of the dataset, we are can expect our models to suffere from overfittinf due to a high variance and a low bias.Some ways to deal with small data sets include:
- **Low model complexity**: A model with high complexity might learn a lot of the noise in our data which would give us inaccurate predictions.
- **Outlier Removal**: More data is always best but we always need to make sure that our outliers are not skewing our predictions.
- **Optimal Feature Enginering**: We can also consuder feature selection and feature creation. This can be used with less complex models.
- **Ensemble Learning**: This method is a good way to reduce the variance of a model without compromissing the complexity.
- **Cross Validation**: This method will healp us see wether the model is learning the data pattern correctly.
- **Transfer Learning**: We can use a pre-exisitng model to 'transfer' to our new solution.

Another simple implementation that we can consider would be using data generating technics such as:
- **Sythetic Data Augmentation**
- **SMOTE**
- **GANS**
- **VAE**
- **Data Poling**

Regardless of what method we use it is important to consider understanding our data deficiencies, statistical deficiences, data source, and buisness limitations and expanding accordingly.

Overview of ML Steps:
1) EDA
2) Base Model
3) Model Selection
4) Hyper Parameter Tunning
5) Final Model Deplorment

For this project we firt started with some very simple data exploritory analysis seen on `data_exploration.ipyn`.


Future Work:
If given the time to work on this further, we could maybe look into scrapping from another dataset to incorporate user shopping data as well as fetch app growth.


## Setup
INSERT INFO

## Docker Deployment
INSERT INFO

## License  
RCP's App code are released under the MIT License. See [here](https://github.com/ivonnem3/receipt-count-prediction/blob/main/LICENSE) for further details.
