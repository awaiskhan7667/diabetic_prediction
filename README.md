Diabetes Prediction باستخدام Machine Learning
📌 Overview

This project focuses on predicting whether a person is likely to have diabetes based on medical attributes using Machine Learning algorithms. It helps in early detection and can assist healthcare professionals in decision-making.

📊 Dataset

The dataset used in this project is the Pima Indians Diabetes Dataset, which includes features like:

Pregnancies
Glucose Level
Blood Pressure
Skin Thickness
Insulin Level
BMI (Body Mass Index)
Diabetes Pedigree Function
Age
⚙️ Technologies Used
Python 🐍
NumPy
Pandas
Matplotlib / Seaborn (for visualization)
Scikit-learn (for ML models)
🧠 Machine Learning Models

The following algorithms were used:

Logistic Regression
Decision Tree
Random Forest
Support Vector Machine (SVM)
🚀 Features
Data preprocessing (handling missing values, scaling)
Exploratory Data Analysis (EDA)
Model training and evaluation
Accuracy comparison of different models
Predictive system for new input data
📈 Model Performance
Model	Accuracy
Logistic Regression	XX%
Decision Tree	XX%
Random Forest	XX%
SVM	XX%

(Replace XX with your actual results)

🛠️ Installation
Clone the repository:
git clone https://github.com/your-username/diabetes-prediction.git
Navigate to the project directory:
cd diabetes-prediction
Install dependencies:
pip install -r requirements.txt
▶️ Usage

Run the main script:

python main.py

Or open the Jupyter Notebook:

jupyter notebook
📌 Project Workflow
Data Collection
Data Cleaning
Exploratory Data Analysis
Feature Engineering
Model Training
Model Evaluation
Prediction System
🔍 Example Prediction
input_data = (2,120,70,20,79,25.0,0.5,33)

prediction = model.predict([input_data])

if prediction[0] == 1:
    print("Diabetic")
else:
    print("Not Diabetic")
📁 Project Structure
diabetes-prediction/
│
├── data/
│   └── diabetes.csv
├── notebooks/
│   └── analysis.ipynb
├── models/
│   └── trained_model.pkl
├── main.py
├── requirements.txt
└── README.md
🎯 Future Improvements
Hyperparameter tuning
Deployment using Flask/Django
Web-based UI
Integration with real-time health data
🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.
