import matplotlib.pyplot as plt
import numpy as np

# Example actual values
actual = np.array([10, 12, 14, 16, 18])

# Example predicted values
predicted = np.array([11, 13, 13, 17, 19])

# Plot results
plt.plot(actual, label="Actual", marker='o')
plt.plot(predicted, label="Predicted", marker='x')

plt.title("Model Prediction vs Actual")
plt.xlabel("Sample")
plt.ylabel("Value")

plt.legend()

plt.show()
