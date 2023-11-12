import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(count):
    primes = []
    num = 2
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def plot_primes_with_regression(count):
    primes = generate_primes(count)
    
    X = np.array(range(1, count+1)).reshape(-1, 1)
    y = np.array(primes)

    # Perform linear regression
    model = LinearRegression().fit(X, y)
    slope = model.coef_[0]
    angle_rad = np.arctan(slope)
    angle_deg = np.degrees(angle_rad)

    # Convert angle to terms of π
    angle_pi = angle_rad / np.pi

    # Calculate the deviations
    deviations = y - model.predict(X)
    min_deviation = np.min(deviations)
    max_deviation = np.max(deviations)
    avg_deviation = np.mean(deviations)

    # Plot prime numbers
    plt.plot(X, y, 'o-', label='Prime Numbers')

    # Plot linear regression line
    plt.plot(X, model.predict(X), label=f'Linear Regression (Angle: {angle_pi:.2f}π radians)')

    # Annotate deviations on the plot
    plt.annotate(f'Min Deviation: {min_deviation:.2f}', xy=(0.5, 0.9), xycoords='axes fraction', color='red')
    plt.annotate(f'Max Deviation: {max_deviation:.2f}', xy=(0.5, 0.85), xycoords='axes fraction', color='red')
    plt.annotate(f'Avg Deviation: {avg_deviation:.2f}', xy=(0.5, 0.8), xycoords='axes fraction', color='red')

    plt.title(f'First {count} Prime Numbers with Linear Regression')
    plt.xlabel('Index')
    plt.ylabel('Prime Number')
    plt.legend()
    plt.show()

# Example: Plot the first 10 prime numbers with linear regression
plot_primes_with_regression(100000)
