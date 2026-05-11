````markdown
# 🏥 PCOS Risk Prediction & Monitoring System

## 📌 Overview
The **PCOS Risk Prediction & Monitoring System** is a Machine Learning-based healthcare application developed to predict the risk of **Polycystic Ovary Syndrome (PCOS)** using patient health parameters.  

The system analyzes medical and lifestyle-related inputs such as BMI, weight, menstrual cycle details, and symptoms to provide:
- PCOS risk prediction
- Risk percentage
- Health recommendations
- Diet suggestions
- Cycle monitoring guidance
- Consultation assistance

This project aims to support **early awareness and preventive healthcare** using Machine Learning.

---

# 🎯 Objectives
- Predict PCOS risk using Machine Learning
- Provide personalized health recommendations
- Promote early awareness and monitoring
- Demonstrate practical healthcare analytics

---

# 🧠 Machine Learning Concepts Used
- Data Cleaning
- Feature Selection
- Feature Scaling
- Train-Test Split
- Classification Algorithms
- Model Evaluation
- Probability Prediction

---

# 🤖 Models Used
## 1. Logistic Regression
Used as a baseline binary classification model.

## 2. Random Forest Classifier (Final Model)
Selected due to:
- Better accuracy
- Reduced overfitting
- Robust prediction performance

---

# 📊 Dataset
Dataset Source: Kaggle PCOS Dataset  

Features include:
- Age
- Weight
- BMI
- Menstrual cycle length
- Hair growth symptoms
- Skin darkening indicators
- Other medical parameters

Target:
- 1 → High Risk / PCOS
- 0 → Low Risk / No PCOS

---

# ⚙️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

---

# 🖥️ User Interface
The project uses **Streamlit** to provide an interactive web interface where users can:
- Enter health details
- Predict PCOS risk
- View recommendations instantly

---

# 📈 Features
✅ PCOS Risk Prediction  
✅ Risk Percentage Display  
✅ Diet Recommendations  
✅ Lifestyle Suggestions  
✅ Cycle Monitoring Guidance  
✅ Consultation Assistant  
✅ Real-time Prediction Interface  

---

# 📂 Project Structure

```bash
PCOS_Risk_prediction/
│
├── data/
│   └── pcos.csv
│
├── model/
│   ├── model.pkl
│   ├── scaler.pkl
│   └── feature_count.pkl
│
├── app.py
├── train.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ▶️ Installation

## Clone Repository
```bash
git clone https://github.com/k-tulasi/PCOS_Risk_prediction.git
```

## Open Project
```bash
cd PCOS_Risk_prediction
```

## Install Dependencies
```bash
pip install -r requirements.txt
```

---

# 🚀 Run Project

## Train Model
```bash
python train.py
```

## Run Streamlit App
```bash
streamlit run app.py
```

---

# 📊 Output
The system predicts:
- High Risk of PCOS
- Low Risk of PCOS

It also provides:
- Risk percentage
- Diet suggestions
- Lifestyle guidance
- Consultation recommendations

---

# ⚠️ Disclaimer
This system is intended for **risk prediction and awareness only** and should not be considered a medical diagnosis.

---

# 🔮 Future Scope
- Mobile application integration
- Hospital database integration
- Online doctor consultation
- Personalized fitness plans
- AI-based health chatbot

---

# 👩‍💻 Author
**Tulasi Kadali**

GitHub:
https://github.com/k-tulasi
````
