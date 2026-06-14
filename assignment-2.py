#Title: Handwritten Digit Classification Using Machine Learning
#Description:This project uses the Digits Dataset from Scikit-learn to train a machine learning model that recognizes handwritten digits from 0 to 9.

# Basic Classification Model using Digit Dataset
# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Load the dataset
digits = load_digits()

plt.imshow(digits.images[0], cmap='gray')
plt.title(f"Digit: {digits.target[0]}")
plt.show()

# Create a DataFrame
df = pd.DataFrame(digits.data, columns=digits.feature_names)
df['target'] = digits.target

# Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

 # (rows, columns)
print(df.shape)  

# summary of dataset
print(df.info())

# statistics
print(df.describe())

# Dataset information
print("\nDataset Shape:", df.shape)
print("Target Classes:", digits.target_names)

# Step 2: Define features (X) and target (y)
X = digits.data
y = digits.target

# Step 3: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# Step 4: Train a classification model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Step 5: Make predictions
y_pred = model.predict(X_test)

# Step 6: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")
print("\nClassification Report:")
print(classification_report(
    y_test, 
    y_pred,
    target_names=[str(i) for i in digits.target_names]
    ))

