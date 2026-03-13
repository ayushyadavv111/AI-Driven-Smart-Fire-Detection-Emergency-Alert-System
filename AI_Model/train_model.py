
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("fire_dataset.csv")

# Features
X = data[['temperature','smoke','gas','flame']]

# Label
y = data['fire']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(n_estimators=100)

# Train
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)

# Test prediction
sample = [[60,500,300,1]]

result = model.predict(sample)

if result[0] == 1:
    print("🔥 FIRE RISK")
else:
    print("SAFE")
