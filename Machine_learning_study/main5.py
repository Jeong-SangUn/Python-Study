import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import joblib
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

titanic_data = pd.read_excel('C:/data/titanic3.xls')
print(titanic_data.columns)
# 'pclass', 'survived', 'name', 'sex', 'age', 'sibsp', 'parch', 'ticket',
#        'fare', 'cabin', 'embarked', 'boat', 'body', 'home.dest'
# pclass sex age (sibsp,parch,embarked,fare)
# survived (label)
age_range=[0,11,21,31,41,51,61,71,81]
titanic_data= titanic_data.dropna(subset=['pclass','sex','age','embarked','parch','sibsp'])

titanic_data['sex'] = titanic_data['sex'].map({'male':0,'female':1})
titanic_data['age'] = pd.cut(titanic_data['age'].tolist(),age_range).codes
titanic_data['embarked'] = titanic_data['embarked'].map({'S':0,'C':1,'Q':2})
x= titanic_data[['pclass','sex','age','embarked','parch','sibsp']]
y= titanic_data['survived']

model = DecisionTreeClassifier(max_depth=4)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.3, random_state=0)

model.fit(x_train, y_train)

# df = pd.DataFrame(data={'pclass':[1],'sex':[0],'age':[80]}, columns=['pclass','sex','age'])
# df_prod = model.predict(df)
y_prod = model.predict(x_test)
print('정확도:',accuracy_score(y_test,y_prod))
# print(df_prod)


# joblib.dump(model, "c:/data/titanic_model.pkl")







