from django.shortcuts import render
import joblib
import numpy as np
import os
from django.conf import settings
import matplotlib.pyplot as plt
import io
import urllib, base64

# Loading model and scaler
model_path = os.path.join(settings.BASE_DIR, 'predictor_app', 'ridge_model.pkl')
scaler_path = os.path.join(settings.BASE_DIR, 'predictor_app', 'scaler.pkl')
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

def home(request):
    if request.method == 'POST':
        study_time = float(request.POST['study_time'])
        failures = int(request.POST['failures'])
        absences = int(request.POST['absences'])
        G1 = float(request.POST['G1'])
        G2 = float(request.POST['G2'])

        data = np.array([[study_time, failures, absences, G1, G2]])
        data_scaled = scaler.transform(data)
        prediction = model.predict(data_scaled)[0]
        prediction = round(prediction, 2)

        # Smart message based on prediction
        if prediction >= 15:
            message = "🎉 Excellent! You're on track for a high final grade. Keep up the great work!"
        elif 10 <= prediction < 15:
            message = "📘 You're doing okay, but there's room to improve. Stay focused!"
        else:
            message = "⚠️ Your predicted grade is low. Consider seeking help or adjusting your study habits."

        # For creating the chart 
        plt.switch_backend('Agg')
        fig, ax = plt.subplots()
        ax.bar(['G1', 'G2', 'Predicted G3'], [G1, G2, prediction], color=['#2196f3', '#03a9f4', '#00796b'])
        ax.set_ylim(0, 20)
        ax.set_ylabel("Grade")
        ax.set_title("Student Grade Progression")

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        chart = base64.b64encode(image_png).decode('utf-8')
        chart_uri = 'data:image/png;base64,' + chart

        return render(request, 'predictor_app/result.html', {
            'prediction': prediction,
            'chart': chart_uri,
            'message': message
        })

    return render(request, 'predictor_app/index.html')
