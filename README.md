# Student Performance Predictor

A Django-based web app that predicts a student's final grade (G3) based on features like study time, absences, and previous grades (G1 & G2) using Ridge Regression. Includes personalized feedback and performance visualization with Matplotlib.

## Technologies Used

- Django
- Scikit-learn
- Pandas
- Matplotlib
- Bootstrap 5

## Features

- Predicts final student grade (G3)
- Visualizes G1, G2, and G3 in a bar chart
- Provides performance-based motivational messages

## Project Structure

- `predictor_web/`: Main Django project
- `predictor_app/`: Contains views, templates, ML model, etc.
- `static/`: CSS styling
- `ridge_model.pkl` & `scaler.pkl`: Pre-trained ML model and scaler

## Run Locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
