from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np

# True values
y_true = np.array([3, -0.5, 2, 7])

# Predicted values
y_pred = np.array([2.5, 0.0, 2, 8])

# Calculate evaluation metrics
mse = mean_squared_error(y_true, y_pred)
mae = mean_absolute_error(y_true, y_pred)

print("Mean Squared Error:", mse)
print("Mean Absolute Error:", mae)
