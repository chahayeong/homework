import numpy as np
from sklearn.model_selection import train_test_split 
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from sklearn.metrics import r2_score
from sklearn.datasets import load_breast_cancer



from sklearn.model_selection import GridSearchCV, KFold
from sklearn.ensemble import RandomForestClassifier


# 이진분류 모델

datasets = load_breast_cancer()

# 1. 데이터 분석
x = datasets.data
y = datasets.target

x_train, x_test, y_train, y_test = train_test_split(x, y, shuffle=True, random_state=66, \
    test_size=0.7)


from sklearn.preprocessing import MinMaxScaler, StandardScaler  
from sklearn.metrics import accuracy_score                      


# 2. 모델 구성


from sklearn.svm import LinearSVC, SVC
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

from sklearn.pipeline import make_pipeline, Pipeline

model = make_pipeline(MinMaxScaler(), RandomForestClassifier())        # model + scaling



# 3. 컴파일, 훈련


model.fit(x_train, y_train)


#

# 4. 예측 및 평가


print("model.score : ", model.score(x_test, y_test))

y_predict = model.predict(x_test)
print("accuracy_score : ", accuracy_score(y_test, y_predict))


'''
model.score :  0.949874686716792   
accuracy_score :  0.949874686716792
'''