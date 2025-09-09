import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
df = pd.read_csv('food.csv')
X = df[['Sweetness', 'Crunchiness']]
y = df['Food']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
sweetness = int(input("Enter Sweetness value: "))
crunchiness = int(input("Enter Crunchiness value: "))
sample = pd.DataFrame({'Sweetness': [sweetness], 'Crunchiness': [crunchiness]})

predicted_food = knn.predict(sample)
print("Predicted Food type:", predicted_food[0])

