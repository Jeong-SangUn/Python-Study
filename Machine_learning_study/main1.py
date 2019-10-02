import pandas as pd     #데이터 프레임
import matplotlib.pyplot as plt #그래프 출력
from sklearn.linear_model import LinearRegression

#키와 몸무게를 학습시켜서 키를 입력하면 몸무게를 예측하겠음.
height = [[1.6],[1.65],[1.7],[1.73],[1.8]] #단위 meter
weight = [[60],[65],[72.3],[75],[80]] #단위 kg

model = LinearRegression() #선형회귀 모델 생성

model.fit(X=height, y=weight) #모델에 값 적용

print(model.predict([[1.8]])[0][0])

plt.title('graph')
plt.xlabel('height')
plt.ylabel('weight')
plt.plot(height,weight,'ro')    #'ro'는 점의 종류
plt.axis([1.5,1.85,50,90])
plt.plot(height,model.predict(height),color='b')
plt.show()




"""
df = pd.read_csv('c:/data/exam2.csv')
# print(df.columns) #컬럼출력
# print(df) #내용출력
#Country를 기준으로 오름차순 정렬
print(df.sort_values(["Country"], ascending=True))W
#Country가 'Norway' 인것만 출력
print(df[df['Country']=='Norway'])
# print( df.loc[ df['Country'] == 'Norway'] )
#Country별 수 출력
print(df['Country'].value_counts()) # print(df['StockCode'].groupby(df['Country']).count())
#Country별 UnitPrice 합 출력
print(df['UnitPrice'].groupby(df['Country']).sum())
"""