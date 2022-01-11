
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.datasets import cifar100


# 1. 데이터
(x_train, y_train), (x_test, y_test) = cifar100.load_data()





# 2. 전처리
# reshape 할 필요 없이 x_train = x_train/255. 만 해도 가능
# 4차원이 안되면 2차원으로 바꿔서 전처리
x_train = x_train.reshape(50000, 32 * 32 * 3)
x_test = x_test.reshape(10000, 32 * 32 * 3)       

from sklearn.preprocessing import MinMaxScaler, StandardScaler, MaxAbsScaler, RobustScaler, PowerTransformer
scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)         # fit과 transfrom 같이 (train에서만)
x_test = scaler.transform(x_test)

# 2차원으로 스케일링 하고 다시 4차원으로 원위치
x_train = x_train.reshape(50000, 32, 32, 3)
x_test = x_test.reshape(10000, 32, 32, 3)

'''
from sklearn.preprocessing import OneHotEncoder
one_hot = OneHotEncoder()
y_train = y_train.reshape(-1,1)             # -1 은 전체 (가장 끝값)
y_test = y_test.reshape(-1,1)
one_hot.fit(y_train)
y_train = one_hot.transform(y_train).toarray()     
y_test = one_hot.transform(y_test).toarray()  
'''

from tensorflow.keras.utils import to_categorical
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)







# 3. 모델
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPool2D, Dropout, GlobalAveragePooling2D
from tensorflow.python.keras.layers.core import Flatten

model = Sequential()
model.add(Conv2D(filters=128, kernel_size=(2, 2), padding='valid', activation='relu' ,input_shape=(32, 32, 3))) 
model.add(Dropout(0.2))
model.add(Conv2D(128, (2,2),padding='same', activation='relu'))                     
model.add(MaxPool2D()) 

model.add(Conv2D(128, (2,2),padding='valid', activation='relu')) 
model.add(Dropout(0.2))  
model.add(Conv2D(128, (2,2),padding='same', activation='relu'))  
model.add(MaxPool2D()) 

model.add(Conv2D(64, (2,2), activation='relu')) 
model.add(Dropout(0.2))
model.add(Conv2D(64, (2,2),padding='same', activation='relu')) 
model.add(MaxPool2D()) 

# model.add(Flatten())                                              
# model.add(Dense(128, activation='relu'))
# model.add(Dropout(0.2))
# model.add(Dense(128, activation='relu'))
# model.add(Dropout(0.2))
# model.add(Dense(128, activation='relu'))
model.add(GlobalAveragePooling2D())
model.add(Dense(100, activation='softmax'))




# 4. 컴파일, 훈련       metrics=['acc']
from tensorflow.keras.optimizers import Adam
optimizer = Adam(lr=0.1)

model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['acc'])

from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
es = EarlyStopping(monitor='val_loss', patience=10, mode='min', verbose=1)
reduce_lr = ReduceLROnPlateau(monitor='val_loss', patience=5, mode='auto', verbose=1, factor=0.5)

# 시간 걸어주기
import time
start_time = time.time()

# 메모리 터지면 batch_size 줄이기
hist = model.fit(x_train, y_train, epochs=300, batch_size=512, verbose=1,
    validation_split=0.2, callbacks=[es, reduce_lr])

end_time = time.time() - start_time






# 5. 평가, 예측      
loss = model.evaluate(x_test, y_test)
print("걸린시간: ", end_time)
print('loss[category] : ', loss[0])
print('loss[accuracy] : ', loss[1])


# 배치 줄이고 발리데이션 늘리기 ( 256, 0.2)
'''
걸린시간:  1211.0673971176147
loss[category] :  2.123988628387451
loss[accuracy] :  0.4442000091075897
'''




'''
optimizer 적용
Epoch 00046: early stopping
313/313 [==============================] - 1s 4ms/step - loss: 4.6055 - acc: 0.0100
걸린시간:  808.0456793308258
loss[category] :  4.605523586273193
loss[accuracy] :  0.009999999776482582
'''