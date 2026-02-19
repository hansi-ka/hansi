import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Sample dataset (Marks vs Salary example)
X = np.array([[30], [40], [50], [60], [70], [80], [90]])
y = np.array([20000, 30000, 40000, 50000, 60000, 70000, 80000])

# Create model
RandomForestRegModel = RandomForestRegressor(n_estimators=100, random_state=42)

# Train model
RandomForestRegModel.fit(X, y)

# Predict for new value
X_marks = [[70]]
prediction = RandomForestRegModel.predict(X_marks)

print("Predicted value:", prediction[0])
