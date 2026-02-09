# ❤️ Heart Disease Prediction System

A Machine Learning--based web application that predicts the risk of
heart disease using clinical parameters. The application provides an
easy-to-use interface where users can input health-related data and
receive predictions instantly.

------------------------------------------------------------------------

## 📌 Overview

The **Heart Disease Prediction System** is designed to assist in early
detection of heart disease risk by analyzing medical parameters such as:

-   Age
-   Cholesterol Level
-   Blood Pressure
-   ECG Results
-   Exercise-Induced Angina
-   Other clinical features

The system uses a trained Machine Learning model to analyze user input
and provide predictions through a web interface.

------------------------------------------------------------------------

## 🚀 Features

✅ User-friendly web interface\
✅ Machine Learning-based prediction\
✅ Real-time results\
✅ Docker support for easy deployment\
✅ Production-ready server configuration using Gunicorn\
✅ Deployment support using Render

------------------------------------------------------------------------

## 🛠️ Tech Stack

### 👨‍💻 Backend

-   Python
-   Flask / Web Framework
-   Scikit-learn (Machine Learning)

### 🎨 Frontend

-   HTML
-   CSS
-   Jinja Templates

### ⚙️ Deployment & DevOps

-   Docker
-   Gunicorn
-   Render Cloud Deployment

------------------------------------------------------------------------

## 📂 Project Structure

    heart-disease-app/
    │
    ├── templates/                 # HTML Templates
    ├── app.py                     # Main application file
    ├── heart_disease_model.pkl    # Trained ML model
    ├── requirements.txt           # Dependencies
    ├── dockerfile                 # Docker configuration
    ├── docker-compose.yml         # Docker compose setup
    ├── gunicorn_config.py         # Gunicorn configuration
    ├── render.yaml                # Render deployment config
    └── README.md                  # Project documentation

------------------------------------------------------------------------

## 🧠 Machine Learning Model

The system uses a pre-trained classification model stored as:

    heart_disease_model.pkl

The model predicts whether a person is at risk of heart disease based on
input health parameters.

------------------------------------------------------------------------

## ⚡ Installation & Setup

### 🔹 Clone Repository

``` bash
git clone https://github.com/OmDhamal-08/heart-disease-app.git
cd heart-disease-app
```

------------------------------------------------------------------------

### 🔹 Create Virtual Environment

``` bash
python -m venv venv
```

Activate environment:

#### Windows

``` bash
venv\Scripts\activate
```

#### Linux / Mac

``` bash
source venv/bin/activate
```

------------------------------------------------------------------------

### 🔹 Install Dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

### 🔹 Run Application

``` bash
python app.py
```

Open browser and go to:

    http://127.0.0.1:5000

------------------------------------------------------------------------

## 🐳 Docker Setup

### Build Docker Image

``` bash
docker build -t heart-disease-app .
```

### Run Container

``` bash
docker run -p 5000:5000 heart-disease-app
```

------------------------------------------------------------------------

## 🌐 Deployment

This project supports deployment on **Render** using:

    render.yaml

------------------------------------------------------------------------

## 📊 Input Parameters

The model uses various clinical parameters such as:

-   Age
-   Sex
-   Chest Pain Type
-   Resting Blood Pressure
-   Cholesterol
-   Fasting Blood Sugar
-   Resting ECG Results
-   Maximum Heart Rate
-   Exercise Induced Angina
-   ST Depression
-   Slope
-   Number of Major Vessels
-   Thalassemia

------------------------------------------------------------------------

## ⚠️ Disclaimer

This project is intended for **educational and research purposes
only**.\
It should **not** be used as a replacement for professional medical
diagnosis.

------------------------------------------------------------------------

## 🤝 Contributing

Contributions are welcome!

Steps:

1.  Fork the repository\
2.  Create a new branch\
3.  Make your changes\
4.  Submit a Pull Request

------------------------------------------------------------------------

## 📜 License

This project is licensed under the MIT License.

------------------------------------------------------------------------

## 👨‍💻 Author

**Om Dhamal**\
🔗 GitHub: https://github.com/OmDhamal-08
