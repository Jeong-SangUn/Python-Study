#http://ihongss.com/csv/exam5.csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sb
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

#키 몸무게를 입력하면 성별을 알려줌
df_boy = pd.read_csv('c:/data/exam5.csv', skiprows=3, usecols=[2,4],names=['height', 'weight'])
df_girl = pd.read_csv('c:/data/exam5.csv', skiprows=3, usecols=[3,5],names=['height', 'weight'])
df_boy['sex'] = 0
df_girl['sex'] = 1

df= pd.concat([df_boy,df_girl] ,axis=0 ,ignore_index=True)
print(df)

# sb.lmplot('weight','height', data=df, fit_reg=False, scatter_kws={"s":50}, hue='sex')
# plt.title('wight_height_sex plot')
# plt.show()

model = LogisticRegression(solver='lbfgs')
x= df[['height','weight']]
y= df['sex']
# model.fit(x ,y)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)
model.fit(x_train, y_train)

y_prod = model.predict(x_test)
print(y_prod.tolist()) #예측값
print(y_test.tolist()) #실제값

#모델 저장
joblib.dump(model, "c:/data/model1.pkl")
#모델 읽기
load_model = joblib.load("c:/data/model1.pkl")
y_prod = load_model.predict(x_test)
print(y_prod.tolist()) #예측값
print(y_test.tolist()) #실제값
# predict_test = pd.DataFrame(
#     data={'height':[140,150,160],'weight':[35,44,70]},
#     columns=['height','weight'])
# print(model.predict(predict_test))
