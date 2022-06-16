import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import pickle

from sklearn.datasets import load_boston
boston = load_boston()

df_x = pd.DataFrame(boston.data, columns=boston.feature_names)
df_y = pd.DataFrame(boston.target)

reg = linear_model.LinearRegression()

x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size = 0.33, random_state = 9)

reg.fit(x_train, y_train)

pickle.dump(reg, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))

print(model.predict(x_test))