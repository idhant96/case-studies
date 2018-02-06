import numpy as np
import pandas as pd
_
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston

writer = pd.ExcelWriter('boston_data.xlsx')
# lm = LinearRegression()
boston = load_boston()
bos = pd.DataFrame(boston.data)
bos.columns = boston.feature_names
bos['city'] = 'mumbai'
bos.to_excel(writer, 'sheet1')
writer.save()

bos['PRICE'] = boston.target
X = bos.drop('PRICE', axis=1)
# lm.fit(X, bos['PRICE'])
X_train, X_test, Y_train, Y_test = train_test_split(X, bos['PRICE'], test_size=0.33, random_state=5)
lm = LinearRegression()
lm.fit(X_train, Y_train)
pred = lm.predict(X_test)
print(pred)