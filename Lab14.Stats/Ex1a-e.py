import matplotlib.pyplot as plt

# First set of x and y values
x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 1, 6, 9]

# Second set of x and y values
x2 = [1, 2, 3, 4, 5]
y2 = [1, 5, 3, 7, 9]

# Plot first set as line graph
plt.plot(x1, y1, label='Line 1', color='blue')

# Plot first set as scatter plot
plt.scatter(x1, y1, label='Scatter 1', color='red')

# Plot second set as line graph
plt.plot(x2, y2, label='Line 2', linestyle='--', color='green')

# Add title and labels
plt.title('Line and Scatter Plot Example')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Add legend
plt.legend()

# Show plot
plt.show()
