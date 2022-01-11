import numpy as np
from sklearn.model_selection import train_test_split 
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from sklearn.metrics import r2_score
from sklearn.datasets import load_breast_cancer


# 이진분류 모델


datasets = load_breast_cancer()

# print(datasets.DESCR)
# print(datasets.feature_names)


# 1. 데이터 분석
x = datasets.data
y = datasets.target

# print(x.shape, y.shape)             # (569, 30) (569,)

# print(y[:20])
# print(np.unique(y))                 # 특이한 부분 있는지 (종류 출력)


x_train, x_test, y_train, y_test = train_test_split(x,y, shuffle=True, \
    random_state=66, test_size=0.7)

# print(x.shape)                        # (569, 30)
# print(x_train.shape)                  # (113, 30)
# print(x_test.shape)                   # (456, 30)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x_train) 
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)   



# 2. 모델 구성
model = Sequential()                       
model.add(Dense(108, activation='relu', input_shape=(30,)))
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))           # sigmoid 0과 1사이 값 (y값이 0아니면 1이기때문)



# 3. 컴파일 훈련
model.compile(loss='binary_crossentropy', optimizer='adam', \
    metrics=['mse', 'accuracy'])                                             # binary

from tensorflow.keras.callbacks import EarlyStopping
es = EarlyStopping(monitor='loss', patience=20, mode='min', verbose=1)       # petience 최저점 나오면 5번까지 참다가 멈춘다 

hist = model.fit(x_train, y_train, epochs=100, batch_size=8, \
    validation_split=0.2, callbacks=[es])


# 4. 평가, 예측
loss = model.evaluate(x_test, y_test)
print('loss : ', loss[0])
print('accuracy : ', loss[1])

print("============== 예측 ===============")            
print(y_test[-5:-1])                               
y_predict = model.predict(x_test[:5])               # 최종결과 5개 볼 수 있음
print(y_predict)

'''
y_predict = model.predict(x_test)
r2 = r2_score(y_test, y_predict)

print("r2 score : ", r2)



# 5. 그래프
import matplotlib.pyplot as plt

plt.plot(hist.history['loss'])          # x: epoch / y: hist.history['loss']
plt.plot(hist.history['val_loss'])

plt.title("loss, val_loss")
plt.xlabel('epochs')
plt.ylabel('loss, val_loss')
plt.legend(['train loss', 'val_loss'])
plt.show()


'''