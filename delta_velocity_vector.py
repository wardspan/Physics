import matplotlib.pyplot as plt
import numpy as np

# Define the initial velocity vectors
v1 = np.array([3, 4])  # Vector v1
v2 = np.array([5, 2])  # Vector v2

# Vector addition: v1 + v2
v_add = v1 + v2

# Vector subtraction: v1 - v2 (which is v1 + (-v2))
v_sub = v1 - v2

# Create a figure and axis
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plotting the vector addition
ax1.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', label='v1')
ax1.quiver(v1[0], v1[1], v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='g', label='v2')
ax1.quiver(0, 0, v_add[0], v_add[1], angles='xy', scale_units='xy', scale=1, color='b', label='v1 + v2')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.set_aspect('equal')
ax1.grid()
ax1.set_title('Vector Addition: v1 + v2')
ax1.legend()

# Plotting the vector subtraction
ax2.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', label='v1')
ax2.quiver(v1[0], v1[1], -v2[0], -v2[1], angles='xy', scale_units='xy', scale=1, color='g', label='-v2')
ax2.quiver(0, 0, v_sub[0], v_sub[1], angles='xy', scale_units='xy', scale=1, color='b', label='v1 - v2')
ax2.set_xlim(-5, 10)
ax2.set_ylim(-5, 10)
ax2.set_aspect('equal')
ax2.grid()
ax2.set_title('Vector Subtraction: v1 - v2')
ax2.legend()

# Show the plot
plt.show()
