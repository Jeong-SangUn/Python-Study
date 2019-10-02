from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
# print(iris)
# print(iris.feature_names)

x= iris['data']
y= iris['target']
# print(x)
# print(y)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.3)
model = DecisionTreeClassifier(max_depth=2)
model.fit(x_train,y_train)

y_prod = model.predict(x_test)

print('정확도:',accuracy_score(y_test,y_prod))
# print(y_prod)
# print(y_test)

