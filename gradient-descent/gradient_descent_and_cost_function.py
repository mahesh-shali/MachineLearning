# -*- coding: utf-8 -*-
"""Gradient Descent and Cost Function.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12KoYSa1ey-LtwwJQByp3wgFAWAPStLrZ
"""

import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def compute_cost(x, y, m, b):
    n = len(x)
    return (1/n) * sum((y - (m*x + b))**2)

def gradient_descent_3d(x, y):
    m_curr = b_curr = 0
    rate = 0.01
    n = len(x)

    # Storing values to plot 3D surface
    m_vals = np.linspace(-10, 20, 100)
    b_vals = np.linspace(-10, 20, 100)
    M, B = np.meshgrid(m_vals, b_vals)
    cost_vals = np.zeros(M.shape)

    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            cost_vals[i, j] = compute_cost(x, y, M[i, j], B[i, j])

    # Perform gradient descent and collect the path
    m_history, b_history = [], []

    for i in range(1000):
        y_predicted = m_curr * x + b_curr

        # Gradient calculation
        md = -(2/n) * sum(x * (y - y_predicted))
        bd = -(2/n) * sum(y - y_predicted)

        # Update m and b values
        m_curr = m_curr - rate * md
        b_curr = b_curr - rate * bd

        # Save current m and b
        m_history.append(m_curr)
        b_history.append(b_curr)

    # Plotting the 3D cost function
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(M, B, cost_vals, cmap='viridis', alpha=0.6)
    ax.set_xlabel('m')
    ax.set_ylabel('b')
    ax.set_zlabel('Cost')

    # Plotting the gradient descent path
    cost_history = [compute_cost(x, y, m, b) for m, b in zip(m_history, b_history)]
    ax.plot(m_history, b_history, cost_history, color='r', marker='o', markersize=3)

    plt.title('Gradient Descent Path on Cost Function')
    plt.show()

# Input data for x and y
x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([5, 7, 9, 11, 13], dtype=float)

# Call the function to visualize gradient descent in 3D
gradient_descent_3d(x, y)

import numpy as np
import matplotlib.pyplot as plt

def compute_cost(x, y, m, b):
    n = len(x)
    return (1/n) * sum((y - (m*x + b))**2)

def gradient_descent_visual(x, y):
    m_curr = b_curr = 0  # Initial values for slope and intercept
    rate = 0.08  # Learning rate
    n = len(x)

    iterations = 1000
    cost_history = []

    # Plot the data points
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='red', marker='+', s=100, label='Data Points')

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = compute_cost(x, y, m_curr, b_curr)
        cost_history.append(cost)

        # Gradient calculation
        md = -(2/n) * sum(x * (y - y_predicted))
        bd = -(2/n) * sum(y - y_predicted)

        # Update m and b values
        m_curr = m_curr - rate * md
        b_curr = b_curr - rate * bd

        # Plot the regression line for every 100th iteration
        if i % 100 == 0:
            plt.plot(x, y_predicted, label=f'Iteration {i}')

    # Final regression line
    plt.plot(x, m_curr * x + b_curr, color='green', label='Final Regression Line', linewidth=2)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Gradient Descent: Regression Line Updates')
    plt.legend()
    plt.show()

    # Plot cost function over iterations
    plt.figure(figsize=(10, 6))
    plt.plot(range(iterations), cost_history, color='blue', label='Cost History')
    plt.xlabel('Iterations')
    plt.ylabel('Cost')
    plt.title('Cost Function During Gradient Descent')
    plt.legend()
    plt.show()

# Input data for x and y
x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([5, 7, 9, 11, 13], dtype=float)

# Call the function to visualize gradient descent in 2D
gradient_descent_visual(x, y)

"""# Excercise"""

import numpy as np
import matplotlib.pyplot as plt

def compute_cost(x, y, m, b):
    n = len(x)
    return (1/n) * sum((y - (m*x + b))**2)

def gradient_descent_visual(x, y):
    m_curr = b_curr = 0  # Initial values for slope and intercept
    rate = 0.01  # Learning rate
    n = len(x)

    iterations = 1000
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='red', marker='+', s=100, label='Data Points')  # Plot the data points

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = compute_cost(x, y, m_curr, b_curr)

        # Gradient calculation
        md = -(2/n) * sum(x * (y - y_predicted))
        bd = -(2/n) * sum(y - y_predicted)

        # Update m and b values
        m_curr = m_curr - rate * md
        b_curr = b_curr - rate * bd

        # Plot the regression line for specific iterations to show progression
        if i % 100 == 0 or i == (iterations - 1):
            plt.plot(x, y_predicted, alpha=0.5, lw=2, label=f'Iteration {i}')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Gradient Descent: Regression Line Progression')
    plt.legend()
    plt.show()

# Input data for x and y
x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([5, 7, 9, 11, 13], dtype=float)

# Call the function to visualize gradient descent in 2D
gradient_descent_visual(x, y)

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import math

def predict_using_sklean():
    df = pd.read_csv("test_scores.csv")
    r = LinearRegression()
    r.fit(df[['math']],df.cs)
    return r.coef_, r.intercept_

def gradient_descent(x,y):
    m_curr = 0
    b_curr = 0
    iterations = 1000000
    n = len(x)
    learning_rate = 0.0002

    cost_previous = 0

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n)*sum([value**2 for value in (y-y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        if math.isclose(cost, cost_previous, rel_tol=1e-20):
            break
        cost_previous = cost
        print ("m {}, b {}, cost {}, iteration {}".format(m_curr,b_curr,cost, i))

    return m_curr, b_curr

if __name__ == "__main__":
    df = pd.read_csv("test_scores.csv")
    x = np.array(df.math)
    y = np.array(df.cs)

    m, b = gradient_descent(x,y)
    print("Using gradient descent function: Coef {} Intercept {}".format(m, b))

    m_sklearn, b_sklearn = predict_using_sklean()
    print("Using sklearn: Coef {} Intercept {}".format(m_sklearn,b_sklearn))