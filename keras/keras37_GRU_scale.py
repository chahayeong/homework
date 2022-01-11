import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, SimpleRNN, LSTM, GRU

# 1. 데이터
x = np.array([[1,2,3], [2,3,4], [3,4,5], [4,5,6], 
            [5,6,7], [6,7,8], [7,8,9], [8,9,10],
            [9,10,11],[10,11,12],
            [20,30,40],[30,40,50],[40,50,60]])
y = np.array([4,5,6,7,8,9,10,11,12,13,50,60,70])
x_predict = np.array([50,60,70])

print(x.shape, y.shape)         #(13, 3) (13,)

x = x.reshape(13, 3, 1)          # (batch_size, timesteps, feature)
x_predict = x_predict.reshape(1,3,1)


# 2. 모델구성
model = Sequential()
# model.add(SimpleRNN(units=10, activation='relu', input_shape=(3, 1)))
model.add(GRU(units=32, activation='relu', input_shape=(3,1)))
model.add(Dense(16, activation='relu', input_shape=(3,1)))
model.add(Dense(16, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1))  

model.summary()

'''
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
gru (GRU)                    (None, 64)                12864
_________________________________________________________________
dense (Dense)                (None, 32)                2080
_________________________________________________________________
dense_1 (Dense)              (None, 32)                1056
_________________________________________________________________
dense_2 (Dense)              (None, 16)                528
_________________________________________________________________
dense_3 (Dense)              (None, 1)                 17
=================================================================
Total params: 16,545
Trainable params: 16,545
Non-trainable params: 0

'''




# 3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')
model.fit(x, y, epochs=100, batch_size=1)

# 4. 평가, 예측
# x_input = np.array([5,6,7]).reshape(1,3,1)

results = model.predict(x_predict)
print(results)             # [[80.84466]]