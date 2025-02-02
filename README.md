
PHISHING URL DETECTOR 🎯


Basic Details

Team Name: Tannies

Team Members

Member 1: Bhanumathy T S - Mar Athanasius College of Engineering

Member 2: Saniya Saji - Mar Athanasius College of Engineering

Member 3: Neethu Shankar - Mar Athanasius College of Engineering



Hosted Project Link

https://github.com/SaniyaSaji/Tink-her-hack.git

Project Description

Our project is a Phishing Detection System that identifies malicious URLs using Machine Learning. It helps users verify whether a given URL is legitimate or a phishing attempt, providing a security layer against online threats.

The Problem statement


Phishing is a cyber-attack where malicious actors deceive users by creating fraudulent websites to steal sensitive information such as passwords, credit card details, or personal information. Traditional blacklist-based detection methods fail to catch newly generated phishing URLs, necessitating intelligent, real-time detection mechanisms.


The Solution
Solution Approach
To address this issue, we developed an AI-powered phishing URL detection system using machine learning. The system is implemented as a Flask-based API that:

Extracts URL Features:

Analyzes various characteristics of the URL, including length, domain attributes, special character usage, and keyword presence.
Uses a custom feature extraction function to generate a 50-dimensional feature vector.
Trains a Machine Learning Model:

Uses a Random Forest Classifier for classification.
If a trained model is unavailable, the system automatically trains a new one.
Deploys as an API:

The Flask API accepts a URL input via a POST request.
The extracted features are passed to the trained model for prediction.
Returns a binary classification result indicating whether the URL is phishing (1) or legitimate (0).


Technical Details

Technologies/Components Used

For Software:

Languages Used: Python, HTML, CSS, JavaScript

Frameworks Used: Flask (for backend), Bootstrap (for frontend UI)

Libraries Used: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, BeautifulSoup (for web scraping)

Tools Used: VS Code, GitHub, Postman (for API testing)

For Hardware:

Standard PC or Server for deployment

Hosting (e.g., local server)


Implementation
For Software:

Installation

Run the following commands to set up the project:
# Clone the repository
git clone [repository link]
cd phishing-detection-url

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

Run
Start the Flask server:
python app.py
Access the web app at http://127.0.0.1:5000/

Project Documentation
For Software:

Screenshots (Add at least 3)
[![Screenshot1](https://github.com/SaniyaSaji/Tink-her-hack/blob/463f15d4ca5c0491417bd45335436d33097fcfcd/IMAGE.jpg)
We are giving the input to verify the url.

![Screenshot2](https://github.com/SaniyaSaji/Tink-her-hack/blob/3cab596b6da05b3e0f2d1bc89f5ef124015ae611/image2.jpg)
The output is displayed

![Screenshot3](https://github.com/SaniyaSaji/Tink-her-hack/blob/9e044759485f2c52b2ba334233caeac950157fff/image3.jpg)

Diagrams


![image](https://github.com/SaniyaSaji/Tink-her-hack/blob/fd4d63b2be33d294663b8cb0246b2e0331b9f5b0/image4.png)
Our project is a Phishing Detection System that identifies malicious URLs using Machine Learning. It helps users verify whether a given URL is legitimate or a phishing attempt, providing a security layer against online threats.


Project Demo
Video
https://www.loom.com/share/ef0c4a0a59dd4deb9b15da93c4c3cd41
This is the user interface of a Phishing URL Detector web application. The design features a gradient background with a clean, centered input box.

🔍 Functionality:

Users can enter a URL into the text box.
Clicking the "Check Legitimacy" button will analyze the URL to determine whether it's safe or a phishing attempt.
🎨 Design:

A soft pink-blue gradient gives a modern look.
A rounded input field ensures a smooth user experience.
The button is styled in orange for visibility.
🛡️ Purpose:
This tool helps users stay safe online by detecting suspicious links before clicking on them!

Team Contributions
Bhanumathy T S - ai model 
Saniya Saji - Frontend
Neethu Shankar -Backend

