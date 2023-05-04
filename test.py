"""
Project 3: Wind loading on a building
Take the first derivative of the data using both the difference method and the gradient method.
Compare the results by plotting both results with height on the x axis and the derivative on the y
axis.

"""

import statistics
import numpy as np
import scipy.integrate as int
import matplotlib.pyplot as plt

# Define constants
total_H = 425     # Height of the building in meters
I = 1805          # Moment of inertia of the building in meters^4
E = 2e11          # Young's modulus of building material (steel) in Pascals

# Data for height (H) in meters and force/length (w) in Newtons/meter
H = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, \
    400, 425]
w = [8.7, 7.8, 8.2, 9.3, 9.0, 7.5, 7.4, 8.6, 9.1, 8.9, 7.5, 6.9, 7.3, 8.0, \
    8.5, 7.9, 8.1]

# Convert lists to arrays
H = np.asarray(H)
w = 1e5*np.asarray(w)

# Part 1: Find average value of w and calculate deflection and total force
w_avg = statistics.mean(w)
total_F1 = w_avg*total_H
d = w_avg*total_H**4/(8*E*I)
print("Total force using average value of w =", total_F1, "Newtons")
print("Deflection using average value of w =", d, "meters")

# Part 2: Integrate data to find total force and w
total_F_trap = int.trapz(w, H)
w_trap = total_F_trap/total_H
d_trap = w_trap*total_H**4/(8*E*I)
total_F_simps = int.simps(w, H)
w_simps = total_F_simps/total_H
d_simps = w_simps*total_H**4/(8*E*I)
print("Total force using trapezoid integration =", total_F_trap, "Newtons")
print("Deflection using trapezoid integration =", d_trap, "meters")
print("Total force using Simpson's integration =", total_F_simps, "Newtons")
print("Deflection using Simpson's integration =", d_simps, "meters")

# Part 3: Differentiate the data (dw/dh) to get changes in force
# Difference method
val = []




# Plot curve of analytically derived first derivative
x_plot = np.linspace(0, 500, 50)
y_plot = derDiff(x_plot)
fig = plt.figure()
plt.plot(x_plot, y_plot)
plt.title("First Derivatives")
plt.xlabel("x")
plt.ylabel("dy/dx")
plt.plot(H, val, 'bo', label="Diff")
plt.plot(H, grad, 'ro', label="Gradient")
plt.legend()
fig.savefig("proj3graph.png")
