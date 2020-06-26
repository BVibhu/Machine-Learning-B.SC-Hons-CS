import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix

#dataset is separated by tab, so we use seperator='\t'
data = pd.read_csv("./SMSSpamData", sep='\t', names=['label', 'message'])

#use '1' for spam and '0' for not spam
data['label'] = data.label.map({'ham':0, 'spam':1})

# split into training and testing sets
# USE from sklearn.model_selection import train_test_split to avoid seeing deprecation warning.
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(data['message'], 
                                                    data['label'], 
                                                    test_size =0.2, 
                                                    random_state=1)


print('Number of rows in the total set: {}'.format(data.shape[0]))
print('Number of rows in the training set: {}'.format(X_train.shape[0]))
print('Number of rows in the test set: {}'.format(X_test.shape[0]))

from sklearn.feature_extraction.text import CountVectorizer
count_vector = CountVectorizer()

# Fit the training data and then return the matrix
training_data = count_vector.fit_transform(X_train).toarray()

# Transform testing data and return the matrix. Note we are not fitting the testing data into the CountVectorizer()
testing_data = count_vector.transform(X_test).toarray()


# ************************Ridge************************
from sklearn.linear_model import Ridge
clf = Ridge(alpha=1.0)
clf.fit(training_data, y_train)

#predict the value
predictions = clf.predict(testing_data)
print(predictions)
