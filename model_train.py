import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import pickle

# Load dataset
df = pd.read_csv('house_cost.csv')

# Encode 'material' (normal=0, premium=1)
le = LabelEncoder()
df['material'] = le.fit_transform(df['material'])

# Features and target
X = df.drop('total_cost', axis=1)
y = df['total_cost']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
with open('house_cost_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("✅ Model trained and saved as house_cost_model.pkl")
