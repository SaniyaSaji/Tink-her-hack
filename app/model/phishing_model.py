import numpy as np
import pandas as pd
from urllib.parse import urlparse
import re

# Load the original dataset to get feature names
df = pd.read_csv(r"C:\Users\91924\Downloads\PhiUSIIL_Phishing_URL_Dataset.csv")

# Function to extract all 50 features
def extract_features(url):
    parsed_url = urlparse(url)

    # Extracting URL-based features (example)
    features = [
        len(url),  # URL Length
        len(parsed_url.netloc),  # Domain length
        1 if re.match(r"\d+\.\d+\.\d+\.\d+", parsed_url.netloc) else 0,  # IP address check
        parsed_url.netloc.count("."),  # Number of dots in domain
        1 if parsed_url.scheme == "https" else 0,  # HTTPS check
        url.count("?"),  # Number of query parameters
        url.count("&"),  # Number of '&' symbols
        sum(map(url.count, "!@#$%^*()[]{}|;:'\",<>"))  # Special character count
    ]

    # Add placeholder values (0) for missing features
    while len(features) < 50:
        features.append(0)  # Adjust this based on your dataset
    
    # Convert to DataFrame with correct feature names
    features_df = pd.DataFrame([features], columns=feature_names)

    return features_df
