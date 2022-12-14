import pandas as pd

data = pd.read_csv('gpascore.csv')


# print(data.isnull().sum()) 
data = data.dropna()
data.fillna(100) # 빈칸을 (값) 만큼 채워줌 fillna(값)


exit()


import tensorflow as tf

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='tanh'),
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid'), # sigmoid는 0과 1사이 확률
])

model.compile(optimizer='adam', loss ='binary_crossentropy', metrics=['accuracy'])

model.fit( epochs=10 )