import numpy as np

data = np.array([10, 20, 30, 40, 50])

# Min-Max normalization
normalized = (data - np.min(data)) / (np.max(data) - np.min(data))

print("Original Data:")
print(data)

print("\nNormalized Data:")
print(normalized)
