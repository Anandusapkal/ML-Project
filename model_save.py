# Import necessary libraries
import pickle
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import os

# Load dataset (Iris dataset as an example)
data = load_iris()
X = data.data  # Features
y = data.target  # Labels

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define and train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save the model to a file using joblib
joblib.dump(model, 'model.pkl')
# Alternatively, you can use pickle instead of joblib:
# with open('model.pkl', 'wb') as file:
#     pickle.dump(model, file)

print("Model saved successfully as model.pkl")

# Print current working directory for troubleshooting
print("Current working directory:", os.getcwd())
