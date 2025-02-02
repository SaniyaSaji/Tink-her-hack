import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from flask import Flask, request, jsonify
import joblib
from urllib.parse import urlparse
import re
from flask_cors import CORS  # Import CORS for cross-origin requests

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for all routes and origins
CORS(app)  # This allows all domains to make requests to this Flask app

from urllib.parse import urlparse
import re
import numpy as np

def extract_features(url):
    try:
        parsed_url = urlparse(url)

        # Extract core URL features
        features = [
            len(url),  # URL Length
            len(parsed_url.netloc),  # Domain Length
            1 if re.match(r"\d+\.\d+\.\d+\.\d+", parsed_url.netloc) else 0,  # IsDomainIP
            0,  # TLD (We need to encode this later)
            url.count("/") / len(url),  # URLSimilarityIndex (approximation)
            url.count(".") / len(url),  # CharContinuationRate
            1 if "https" in parsed_url.scheme else 0,  # IsHTTPS
            url.count("?"),  # NoOfQMarkInURL
            url.count("="),  # NoOfEqualsInURL
            url.count("&"),  # NoOfAmpersandInURL
            sum(map(url.count, "!@#$%^*()[]{}|;:'\",<>")),  # NoOfOtherSpecialCharsInURL
            len(re.findall(r"[a-zA-Z]", url)),  # NoOfLettersInURL
            len(re.findall(r"\d", url)),  # NoOfDigitsInURL
            len(re.findall(r"\d", url)) / len(url),  # DigitRatioInURL
            url.count("%"),  # NoOfObfuscatedChar
            url.count("favicon"),  # HasFavicon
            1 if "submit" in url.lower() else 0,  # HasSubmitButton
            1 if "password" in url.lower() else 0,  # HasPasswordField
            1 if "bank" in url.lower() else 0,  # Bank keyword presence
            1 if "crypto" in url.lower() else 0,  # Crypto keyword presence
            1 if "paypal" in url.lower() else 0,  # Pay keyword presence
            1 if "facebook.com" in url or "twitter.com" in url else 0,  # HasSocialNet
            1 if "copyright" in url.lower() else 0,  # HasCopyrightInfo
            url.count("<iframe"),  # NoOfiFrame
            url.count("window.open"),  # NoOfPopup
            url.count("<script"),  # NoOfJS
            url.count("<img"),  # NoOfImage
            url.count("<link"),  # NoOfCSS
            url.count("self"),  # NoOfSelfRef
            url.count("external"),  # NoOfExternalRef
        ]

        # Padding if features < 50 (to match training)
        while len(features) < 50:
            features.append(0)

        print(f"Extracted Features: {features}")
        return np.array(features).reshape(1, -1)

    except Exception as e:
        print(f"Error in feature extraction: {e}")
        raise
from urllib.parse import urlparse
import re
import numpy as np

def extract_features(url):
    try:
        parsed_url = urlparse(url)

        # Extract core URL features
        features = [
            len(url),  # URL Length
            len(parsed_url.netloc),  # Domain Length
            1 if re.match(r"\d+\.\d+\.\d+\.\d+", parsed_url.netloc) else 0,  # IsDomainIP
            0,  # TLD (We need to encode this later)
            url.count("/") / len(url),  # URLSimilarityIndex (approximation)
            url.count(".") / len(url),  # CharContinuationRate
            1 if "https" in parsed_url.scheme else 0,  # IsHTTPS
            url.count("?"),  # NoOfQMarkInURL
            url.count("="),  # NoOfEqualsInURL
            url.count("&"),  # NoOfAmpersandInURL
            sum(map(url.count, "!@#$%^*()[]{}|;:'\",<>")),  # NoOfOtherSpecialCharsInURL
            len(re.findall(r"[a-zA-Z]", url)),  # NoOfLettersInURL
            len(re.findall(r"\d", url)),  # NoOfDigitsInURL
            len(re.findall(r"\d", url)) / len(url),  # DigitRatioInURL
            url.count("%"),  # NoOfObfuscatedChar
            url.count("favicon"),  # HasFavicon
            1 if "submit" in url.lower() else 0,  # HasSubmitButton
            1 if "password" in url.lower() else 0,  # HasPasswordField
            1 if "bank" in url.lower() else 0,  # Bank keyword presence
            1 if "crypto" in url.lower() else 0,  # Crypto keyword presence
            1 if "paypal" in url.lower() else 0,  # Pay keyword presence
            1 if "facebook.com" in url or "twitter.com" in url else 0,  # HasSocialNet
            1 if "copyright" in url.lower() else 0,  # HasCopyrightInfo
            url.count("<iframe"),  # NoOfiFrame
            url.count("window.open"),  # NoOfPopup
            url.count("<script"),  # NoOfJS
            url.count("<img"),  # NoOfImage
            url.count("<link"),  # NoOfCSS
            url.count("self"),  # NoOfSelfRef
            url.count("external"),  # NoOfExternalRef
        ]

        # Padding if features < 50 (to match training)
        while len(features) < 50:
            features.append(0)

        print(f"Extracted Features: {features}")
        return np.array(features).reshape(1, -1)

    except Exception as e:
        print(f"Error in feature extraction: {e}")
        raise


# Check if the model exists, otherwise train a new one
def load_or_train_model():
    if os.path.exists("phishing_model.pkl"):
        print("Loading existing model...")
        return joblib.load("phishing_model.pkl")
    else:
        print("Model not found! Training a new model...")
        train_model()
        return joblib.load("phishing_model.pkl")

# Initialize model
model = load_or_train_model()

@app.route('/', methods=['GET'])
def home():
    return "Phishing Detection API is running!", 200

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        if 'url' not in data:
            return jsonify({"error": "'url' key is missing in the request"}), 400

        # Extract features with correct 50 columns
        features_df = extract_features(data['url'])

        # Make prediction
        prediction = model.predict(features_df)[0]

        return jsonify({"phishing": bool(prediction)})

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True)
