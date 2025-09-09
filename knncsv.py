import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
df=pd.read_csv('knntable.csv')
x=df.iloc[:,:-1]
y=df.iloc[:,-1]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
c_knn=KNeighborsClassifier(n_neighbors=3)
c_knn.fit(x_train,y_train)
y_pred=c_knn.predict(x_test)
print("Accuracy:",metrics.accuracy_score(y_test,y_pred))
print("Enter sample data")
a=int(input("Enter the height in cm:"))
b=int(input("Enter the weight in cm:"))
sample = pd.DataFrame({'Height': [a], 'Weight': [b]})
pred = c_knn.predict(sample)
print("Predicted T-shirt size:", pred[0])
