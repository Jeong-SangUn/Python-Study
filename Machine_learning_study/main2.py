#http://ihongss.com/csv/exam5.csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sb

# a2=[]
# for문 방식 1번
# for i in range(len(a1)):
#     a2.append([a1[i]])
# print(a2)
# for문 방식 2번
# a3 = [[a1[i]] for i in range(len(a1))]
# numpy.reshape 방식
a1=[3,4,5,1,3,5,61,23,251,35]
a4 = np.reshape(a1,(-1,1)).tolist()

df = pd.DataFrame(columns=('x','y'))
df.loc[0] = [7,1]
df.loc[1] = [2,1]
df.loc[2] = [4,2]
df.loc[3] = [9,4]
df.loc[4] = [10,5]
print(df)

df1 = pd.DataFrame(data={'x':[7,2,4,9,10,6,7,2,4,5],'y':[1,1,2,4,5,7,4,6,3,8]}, columns=['x','y'])
# print(df1)
# print(df1.values)
# print(df1['x'])

kmeans = KMeans(n_clusters=3)   #모델생성
kmeans.fit(df1.values)          #모델적용

df1['c_id'] = kmeans.labels_    #결과값을 df1에 저장
# print(df1)
sb.lmplot('x','y', data=df1, fit_reg=False, scatter_kws={"s":50}, hue='c_id')

plt.title('kmeans plot')
plt.axis([-3,12,-3,11])
# plt.xlabel('x')
# plt.ylabel('y')
# plt.plot(df1['x'],df1['y'],'^')
plt.show()