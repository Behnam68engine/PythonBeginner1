import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x = np.linspace(-2*np.pi, 2*np.pi, 400)

# Calculate cos(x + π/2)
cos_x_plus_pi_2 = np.cos(x + np.pi/2)

# Calculate cos(x - π/2)
cos_x_minus_pi_2 = np.cos(x - np.pi/2)

# Calculate cos(x)
cos_x = np.cos(x)

# Plot x and cos(x + π/2) with label indicating it's equivalent to -sin(x)
plt.plot(x, cos_x_plus_pi_2, label='cos(x + π/2) = - sin(x)')

# Plot x and cos(x - π/2) with purple color and label indicating it's equivalent to +sin(x)
plt.plot(x, cos_x_minus_pi_2, label='cos(x - π/2) = + sin(x)', color='purple')

# Plot x and cos(x) with green color
plt.plot(x, cos_x, label='cos(x)', color='green')

# Labeling the x-axis and y-axis
plt.xlabel('x')
plt.ylabel('cos(x ± π/2) = ∓sin(x)')

# Set the title of the plot
plt.title('Plot of x and cos(x ± π/2) = ∓sin(x)')

# Display legend
plt.legend()

# Display grid
plt.grid(True)

# Show x-axis and y-axis
plt.axhline(0, color='red', linewidth=3.5)  # Horizontal line at y=0
plt.axvline(0, color='red', linewidth=3.5)  # Vertical line at x=0

# Set x ticks at intervals of π/4
plt.xticks(np.arange(-2*np.pi, 2*np.pi + np.pi/4, np.pi/4), 
           [r'$-2\pi$', r'$-\frac{7\pi}{4}$', r'$-\frac{3\pi}{2}$', r'$-\frac{5\pi}{4}$', r'$-\pi$', r'$-\frac{3\pi}{4}$', r'$-\frac{\pi}{2}$', r'$-\frac{\pi}{4}$', r'$0$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$', r'$\frac{5\pi}{4}$', r'$\frac{3\pi}{2}$', r'$\frac{7\pi}{4}$', r'$2\pi$'])

# Add single-headed arrow and label from (0,1) to (pi/2,1)
plt.annotate('', xy=(np.pi/2, 1), xytext=(0, 1),
             arrowprops=dict(arrowstyle='->', color='purple', linewidth=1.5),
             annotation_clip=False)
plt.text(np.pi/4, 0.92, r'$- \frac{\pi}{2}$', horizontalalignment='center', fontsize=12, color='purple')

# Add another single-headed arrow and label from (-pi/3,0.5) to (-5pi/6,0.5)
plt.annotate('', xy=(-5*np.pi/6, 0.5), xytext=(-np.pi/3, 0.5),
             arrowprops=dict(arrowstyle='->', color='blue', linewidth=1.5),
             annotation_clip=False)
plt.text(-7*np.pi/12, 0.55, r'$+ \frac{\pi}{2}$', horizontalalignment='center', fontsize=12, color='blue')

# Display the plot
plt.show()
