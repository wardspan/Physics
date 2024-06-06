import matplotlib.pyplot as plt

# Create figure and axes
fig, ax = plt.subplots()

# Plot the displacement vector
ax.arrow(0, 0, -70, 0, head_width=5, head_length=5, fc='blue', ec='blue')

# Set the limits of the plot
ax.set_xlim(-80, 10)
ax.set_ylim(-10, 10)

# Adding labels and title
ax.set_xlabel('x (km)')
ax.set_ylabel('y (km)')
ax.set_title('Displacement Vector with ∆x = -70 km')

# Adding grid
ax.grid(True)

# Mark the origin and the end point
plt.plot(0, 0, 'go')  # Green dot at the origin
plt.text(0, 0.5, '(0, 0)', fontsize=12, ha='center')
plt.plot(-70, 0, 'ro')  # Red dot at the end of the vector
plt.text(-70, 0.5, '(-70, 0)', fontsize=12, ha='center')

# Show plot
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()

