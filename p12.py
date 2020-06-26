import numpy as np
import seaborn as sns
import pandas as pd

from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split

from sklearn import metrics
from sklearn.metrics import r2_score

from sklearn.datasets import load_boston 
boston_data = load_boston()
# splitting data to training and testing dataset

# Input Data 
data = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)
x = data[['INDUS']]
print(x)

# Output Data 
y = boston_data.target 

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size =0.2, 
                                                    random_state = 0) 
   
print("xtrain shape : ", xtrain.shape) 
print("xtest shape  : ", xtest.shape) 
print("ytrain shape : ", ytrain.shape) 
print("ytest shape  : ", ytest.shape)



# Fitting Multi Linear regression model to training model 
lr = LinearRegression() 
lr.fit(xtrain, ytrain)

# predicting the test set results 
y_pred = lr.predict(xtest)


print('Mean Absolute Error : ', metrics.mean_absolute_error(ytest, y_pred))
print('Mean Square Error : ', metrics.mean_squared_error(ytest, y_pred))
print('RMSE', np.sqrt(metrics.mean_squared_error(ytest, y_pred)))
print('R squared error', r2_score(ytest, y_pred))