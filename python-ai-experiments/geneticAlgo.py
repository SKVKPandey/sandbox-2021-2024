import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

# Generate some synthetic data
np.random.seed(0)
X = np.linspace(-1, 1, 100)
y = 2 * X + 1 + np.random.randn(*X.shape) * 0.3  # Simulating a linear relationship with some noise

# Define a simple neural network using TensorFlow
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])  # Single neuron for a linear model
])
model.compile(optimizer='sgd', loss='mean_squared_error')  # Compile the model

# Train the model
model.fit(X, y, epochs=100, verbose=0)

# Make predictions
predictions = model.predict(X)

# Plot the data and the model predictions
plt.scatter(X, y, label='Actual data')
plt.plot(X, predictions, color='red', label='Model predictions')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Simple Neural Network Fit')
plt.legend()
plt.show()
