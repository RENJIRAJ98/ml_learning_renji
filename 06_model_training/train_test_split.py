from sklearn.model_selection import train_test_split
import numpy as np

# Example dataset
X = np.arange(100).reshape((50,2))
y = np.arange(50)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))
