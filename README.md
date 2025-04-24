# 🎓 Student Performance Predictor
A Django-based web app that predicts a student's final grade (G3) using Ridge Regression based on features like study time, absences, and previous grades (G1 & G2). The app includes personalized feedback and visualizes grade progression using Matplotlib.

---

## 🚀 Technologies Used
- **Python**
- **Django**
- **Scikit-learn**
- **Pandas**
- **Matplotlib**
- **Bootstrap 5**

---

## 📊 Features
- Predicts final student grade (G3) using Ridge Regression
- Visualizes G1, G2, and G3 in a bar chart using Matplotlib
- Provides smart feedback messages based on predicted performance
- Clean and responsive UI with Bootstrap 5

---

## 📁 Project Structure
student-performance-predictor/
├── predictor_web/
│   ├── predictor_app/
│   │   ├── templates/
│   │   │   └── predictor_app/
│   │   │       ├── index.html
│   │   │       └── result.html
│   │   ├── static/
│   │   │   └── predictor_app/
│   │   │       └── styles.css
│   │   ├── views.py
│   │   └── ...
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── ridge_model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
