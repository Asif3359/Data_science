import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


# data wrangling libraries
import pandas as pd
import numpy as np
import scipy.stats
from scipy.stats import norm
import math
df = pd.DataFrame({
    'A':[1,2],
    'B':[3,4]
})
print(df)
arr = np.array([1,2,3])
print(np.mean(arr))
print(norm.cdf(0))
print(math.sqrt(16))


# data preprocessing libraries
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import scale
from sklearn.metrics.pairwise import cosine_similarity
le = LabelEncoder()
y = le.fit_transform(['dog', 'cat','cat'])
print(y)
scaler = StandardScaler()
scaled_data = scaler.fit_transform([
    [1,2],
    [3,4],
    [5,6]
])
print(scaled_data)
lb = LabelBinarizer()
y = lb.fit_transform([1,2,3])
print(y)


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

# Deep Learning libraries
from keras import Sequential
from keras.src.layers import LSTM
from keras.src.layers import Dense
from keras.src.layers import Dropout
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor





