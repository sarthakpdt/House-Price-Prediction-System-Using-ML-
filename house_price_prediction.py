#A simple yet challenging project, to predict the housing price based on certain factors like house area, bedrooms, furnished, nearness to mainroad, etc. The dataset is small yet, it's complexity arises due to the fact that it has strong multicollinearity. Can you overcome these obstacles & build a decent predictive model?
#Objective:
#Understand the Dataset & cleanup (if required).
#Build Regression models to predict the sales w.r.t a single & multiple feature.
#Also evaluate the models & compare thier respective scores like R2, RMSE, etc
import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
#load and read the file 
df=pd.read_csv("Housing.csv")
#making a list of the colomns having yes or no 
binarycolomn=["mainroad","guestroom","basement","hotwaterheating","airconditioning","prefarea"]
#replacing the yes and no value by 1 and 0 respectively by for loop 
for i in binarycolomn:
    df[i]=df[i].map({"yes":1,"no":0})
#replacing fursnishing status colomn by numbers 
df["furnishingstatus"]=df["furnishingstatus"].map({"unfurnished":0,"furnished":2,"semi-furnished":1})
#prints all the missing value in each colomn 
print("missing value:",df.isnull().sum())
#making the list of all the features in dataset
features=['area','bedrooms','bathrooms','stories','mainroad','guestroom', 'basement', 'hotwaterheating','airconditioning', 'parking', 'prefarea', 'furnishingstatus']
#taking target as the colomn whcih is to be predicted here i have taken price as the colomn to be predicted 
target='price'
x=df[features]
y=df[target]
#splitting the dataset into 80 20 ratio 
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
#creates a regression model 
area=LinearRegression()
#trains the area colomn to predict the price 
area.fit(x_train[["area"]],y_train)
#predicts the price 
pred_area=area.predict(x_test[["area"]])
#printing all the errors 
print("R2 Score:",r2_score(y_test,pred_area))
print("RMSE:",np.sqrt(mean_squared_error(y_test,pred_area)))
print("MAE:",mean_absolute_error(y_test,pred_area))
#same thing done 
all=LinearRegression()
all.fit(x_train,y_train)
pred_all=all.predict(x_test)
print("R2 Score:",r2_score(y_test,pred_all))
print("RMSE:",np.sqrt(mean_squared_error(y_test,pred_all)))
print("MAE:",mean_absolute_error(y_test,pred_all))
