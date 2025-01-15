import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# step no 2
data = {'Age':[30,25,35,20,40,55,32,28],
        'MonthlyCharge':[50,60,80,40,100,120,70,55],
         'churn':[0,1,0,1,0,1,0,1]}
df = pd.DataFrame(data)
print(df)
x = df[['Age','MonthlyCharge']]
y = df['churn']

# Step no 3
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)

# step no 4
svc_model = SVC(kernel='linear', C=1.0) #default regularization
svc_model.fit(x_train,y_train)

# step no 5
y_pred = svc_model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)
report = classification_report(y_test, y_pred)
print(report)

# step no 6
user_age = float(input("Enter Customer age: "))
user_monthly_charge = float(input("Enter Customer monthly charges: "))
user_input = np.array([[user_age, user_monthly_charge]])
prediction = svc_model.predict(user_input)
if prediction[0] == 0:
    print("The customer is likely to stay. ")
else:
    print("The customer is at risk of churning")