import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from flask import Flask, request, jsonify
import joblib

# Load and preprocess data
def load_data():
    file_path = "PhiUSIIL_Phishing_URL_Dataset.csv"
    df = pd.read_csv(file_path)
    
    # Drop unnecessary columns
    df.drop(columns=['FILENAME', 'URL', 'Domain', 'TLD', 'Title'], inplace=True)
    
    # Split features and target
    X = df.drop(columns=['label'])
    y = df['label']
    
    return X, y

# Train and save model
def train_model():
    X, y = load_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {acc:.4f}")
    
    # Save model
    joblib.dump(model, "phishing_model.pkl")

# Check if model exists, otherwise train a new one
if os.path.exists("phishing_model.pkl"):
    model = joblib.load("phishing_model.pkl")
else:
    print("Model not found! Training a new model...")
    train_model()
    model = joblib.load("phishing_model.pkl")

# Initialize Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_data = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(input_data)[0]
    return jsonify({"phishing": bool(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
