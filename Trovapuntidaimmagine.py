import numpy as np
import matplotlib.pyplot as plt

def find_points_on_plot(x, y, threshold=0.1):
    points = []
    
    # Calculate the first derivative (slope) of the line
    slopes = np.diff(y) / np.diff(x)
    
    # Find points where the slope changes sign
    sign_changes = np.where(np.diff(np.sign(slopes)))[0]
    
    for idx in sign_changes:
        # Add points on either side of the sign change to the result
        x_point = (x[idx] + x[idx + 1]) / 2
        y_point = (y[idx] + y[idx + 1]) / 2
        
        # Ensure the difference between consecutive points is significant
        if np.abs(y[idx + 1] - y[idx]) > threshold:
            points.append((x_point, y_point))
    
    return points

# Example usage
x_data = np.linspace(0, 10, 100)
y_data = np.sin(x_data)  # Replace this with your actual data

# Add some noise to the data to make it more realistic
y_data += np.random.normal(0, 0.1, size=len(x_data))

plt.plot(x_data, y_data, label='Continuous Line')
plt.scatter(*zip(*find_points_on_plot(x_data, y_data)), color='red', label='Detected Points')
plt.legend()
plt.show()