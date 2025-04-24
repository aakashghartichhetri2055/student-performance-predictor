import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
import joblib

# Load dataset
df = pd.read_csv('student-mat.csv', sep=';')

# Use only selected numeric features
features = ['studytime', 'failures', 'absences', 'G1', 'G2']
X = df[features]
y = df['G3']  # target: final grade

# Split and scale
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Train model
ridge = Ridge()
params = {'alpha': [0.1, 1, 10, 100]}
grid = GridSearchCV(ridge, params, cv=5)
grid.fit(X_train_scaled, y_train)

# Save model and scaler
joblib.dump(grid.best_estimator_, 'ridge_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

print("Model and scaler saved with features:", features)
