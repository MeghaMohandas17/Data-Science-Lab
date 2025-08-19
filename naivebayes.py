from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
iris=load_iris()
x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
c_gnb=GaussianNB()
c_gnb.fit(x_train,y_train)
y_pred=c_gnb.predict(x_test)
print("Accuracy:",metrics.accuracy_score(y_test,y_pred))
print("Enter the sample data")
a=int(input("Enter sepal length in cm="))
b=int(input("Enter sepal width in cm="))
c=int(input("Enter petal length in cm="))
d=int(input("Enter petal width in cm="))
sample=[[a,b,c,d]]
pred=c_gnb.predict(sample)
pred_v=[iris.target_names[p] for p in pred]
print(pred_v)
