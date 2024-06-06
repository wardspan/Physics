import matplotlib.pyplot as plt

# Define the displacement in the x-direction
delta_x = -70  # in km

# Create a figure and axis
fig, ax = plt.subplots()

# Draw the coordinate system
ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)
ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

# Plot the displacement vector
ax.arrow(0, 0, delta_x, 0, head_width=1, head_length=2, fc='blue', ec='blue')

# Set the limits of the plot
ax.set_xlim(-10, delta_x - 10)
ax.set_ylim(-10, 10)

# Add labels
ax.set_xlabel('X (km)')
ax.set_ylabel('Y (km)')
ax.set_title('Displacement Vector with ∆x = -70 km')

# Annotate the vector
ax.text(delta_x/2, 1, '∆x = -70 km', fontsize=12, color='blue')

# Set equal scaling
ax.set_aspect('equal')

# Show the plot
plt.show()