import numpy as np
# import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential, load_model
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from tensorflow.python.keras.callbacks import ModelCheckpoint


datasets = load_diabetes()
x = datasets.data
y = datasets.target


x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.85, shuffle=True, random_state=66)

from sklearn.preprocessing import MinMaxScaler, StandardScaler
scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)


#2. 모델 구성
'''
model = Sequential()
model.add(Dense(64, input_dim=10))            
model.add(Dense(64))
model.add(Dense(32))
model.add(Dense(32))
model.add(Dense(16))
model.add(Dense(16))
model.add(Dense(1))


# model.save('./_save/keras46_1_save_model_1.h5')
# model.save_weights('./_save/keras46_1_save_weights_1.h5')


# model = load_model('./_save/keras46_1_save_model_1.h5')
# model = load_model('./_save/keras46_1_save_model_2.h5')
# model = load_model('./_save/keras46_1_save_weights_1.h5')     #weights 는 weights끼리
# model = load_model('./_save/keras46_1_save_weights_2.h5')     # load model로 load 안됨
# model.summary()



#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')

# model.load_weights('./_save/keras46_1_save_weights_1.h5')             # 랜덤 초기화값 loss와 r2
model.load_weights('./_save/keras46_1_save_weights_2.h5')               # 제대로 된 값 loss와 r2

from tensorflow.keras.callbacks import EarlyStopping,ModelCheckpoint
es = EarlyStopping(monitor='val_loss', patience=3, mode='min', verbose=1)
cp = ModelCheckpoint(monitor='val_loss', save_best_only=True, mode='auto',
                    filepath='./_save/ModelCheckPoint/keras47_MCP.hdf5')

import time
start_time = time.time()
model.fit(x_train, y_train, epochs=30, verbose=2, validation_split=0.2, callbacks=[es])       # weights시 필요없음
end_time = time.time() - start_time

# model.save('./_save/keras46_1_save_model_2.h5')
# model.save_weights('./_save/keras46_1_save_weights_2.h5')
'''

model = load_model('./_save/ModelCheckPoint/keras47_MCP.hdf5')

#4. 평가, 예측
# mse, R2 사용

y_predict = model.predict(x_test)
# print("예측값 : ", y_predict)

loss = model.evaluate(x_test, y_test)
# print("경과시간 : ", end_time)
print('loss : ', loss)

r2 = r2_score(y_test, y_predict)
print("r2 score : ", r2)


'''
loss :  3529.268798828125
r2 score :  0.5086280352449034
'''