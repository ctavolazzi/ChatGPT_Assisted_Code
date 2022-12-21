import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load the Iris dataset
data = pd.read_csv('iris.csv')

# Split the dataset into features (X) and labels (y)
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train a K-Nearest Neighbors classifier on the training data
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

# Use the trained model to make predictions on the test data
predictions = knn.predict(X_test)

# Evaluate the model's performance
accuracy = knn.score(X_test, y_test)
print(f'Model accuracy: {accuracy:.2f}')

