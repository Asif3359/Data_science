import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# data wrangling libraries
import pandas as pd
import numpy as np
import scipy.stats
from scipy.stats import norm
import math

df = pd.DataFrame({
    'A': [1, 2],
    'B': [3, 4]
})
print("DataSet frame : \n", df)
arr = np.array([1, 2, 3])
print("Numpy mean : \n", np.mean(arr))
print("State cdf : \n", norm.cdf(0))
print("Math sqrt : \n", math.sqrt(16))

# data preprocessing libraries
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import scale
from sklearn.metrics.pairwise import cosine_similarity

le = LabelEncoder()
y = le.fit_transform(['dog', 'cat', 'cat'])
print("LabelEncoder : \n", y)

scaler = StandardScaler()
scaled_data = scaler.fit_transform([
    [1, 2],
    [3, 4],
    [5, 6]
])
print("StandardScaler : \n", scaled_data)

lb = LabelBinarizer()
y = lb.fit_transform([1, 2, 3])
print("LabelBinarizer : \n", y)

scaler = MinMaxScaler()
scaled_data = scaler.fit_transform([
    [1, 2],
    [3, 4]
])
print("MinMaxScaler: \n", scaled_data)

scaled_data = scale([1, 2, 3, 4])
print("scale : \n", scaled_data)

sim = cosine_similarity([
    [1, 0],
    [0, 1]
])
print("cosine_similarity : \n", sim)

# ML model libraries
import statsmodels.api as sm

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier

from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import BaggingRegressor
from sklearn.ensemble import BaggingClassifier

from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import GradientBoostingClassifier

from xgboost import XGBRegressor
from xgboost import XGBClassifier

from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans

X = sm.add_constant(list(range(1, 21)))
Y = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]
model = sm.OLS(Y, X).fit()
print("statsmodels.api : \n", model.summary())

model = LinearRegression()
model.fit([
    [1],
    [2],
    [3]
], [1, 2, 3])
print("LinearRegression :\n", model.predict([[4]]))

model = LogisticRegression()
model.fit([[1], [2], [3]], [0, 1, 0])
print("LogisticRegression :\n", model.predict([[4]]))

model = DecisionTreeRegressor()
model.fit([[1], [2], [3]], [1, 2, 3])
print("DecisionTreeRegressor :\n", model.predict([[4]]))

model = KNeighborsRegressor(n_neighbors=3)
model.fit([[1], [2], [3]], [1, 2, 3])
print("KNeighborsRegressor :\n", model.predict([[4]]))

model = BaggingRegressor()
model.fit([[1], [2], [3]], [1, 2, 3])
print("BaggingRegressor :\n", model.predict([[4]]))

model = RandomForestRegressor()
model.fit([[1], [2], [3]], [1, 2, 3])
print("RandomForestRegressor :\n", model.predict([[4]]))

model = GradientBoostingRegressor()
model.fit([[1], [2], [3]], [1, 2, 3])
print("GradientBoostingRegressor :\n", model.predict([[4]]))

model = XGBRegressor()
model.fit([[1], [2], [3]], [1, 2, 3])
print("XGBRegressor :\n", model.predict([[4]]))

model = DBSCAN()
labels = model.fit_predict([[1, 2], [2, 3], [8, 9], [4, 5]])  # Including a new point directly
print("Cluster labels:", labels)

model = KMeans(n_clusters=2)
model.fit([[1, 2], [2, 3], [8, 9]])
print("KMeans :\n", model.predict([[4, 5]]))

# model tuning and performance libraries
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.metrics import roc_auc_score

# data visualization libraries
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# NLP libraries
import re
import string
from nltk.corpus import stopwords
from nltk import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import WordNetLemmatizer

# # Deep Learning libraries
# from keras import Sequential
# from keras.src.layers import LSTM
# from keras.src.layers import Dense
# from keras.src.layers import Dropout
# from sklearn.neural_network import MLPClassifier
# from sklearn.neural_network import MLPRegressor
