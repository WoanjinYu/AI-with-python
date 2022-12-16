import pandas as pd

data = pd.read_csv('gpascore.csv')


# print(data.isnull().sum()) 
data = data.dropna() # 빈칸 없애기
# data.fillna(100) # 빈칸을 (값) 만큼 채워줌 fillna(값)
# print(data['gpa'].max()) #최대값 구하기

y데이터  = data['admit'].values #'admit' 세로열에 있는 데이터 출력해줌

x데이터 = []

for i, rows in data.iterrows():
    print(rows['gre']) #'gre'세로 옆에 있는 데이터 출력해줌



exit()


import tensorflow as tf

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='tanh'),
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid'), # sigmoid는 0과 1사이 확률
])

model.compile(optimizer='adam', loss ='binary_crossentropy', metrics=['accuracy'])

model.fit( epochs=10 )