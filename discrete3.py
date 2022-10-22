import numpy as np

# Creating two 2D numpy arrays using the array() method

# Consider the system of equations x0 + 2 * x1 = 1 and 3 * x0 + 5 * x1 = 2
arr1 = np.array([[1, 2], [3, 5]])
arr2 = np.array([1, 2])

# Display the arrays
print("Array1...\n",arr1)
print("\nArray2...\n",arr2)

# Check the Dimensions of both the arrays
print("\nDimensions of Array1...\n",arr1.ndim)
print("\nDimensions of Array2...\n",arr2.ndim)

# Check the Shape of both the arrays
print("\nShape of Array1...\n",arr1.shape)
print("\nShape of Array2...\n",arr2.shape)

# To solve a linear matrix equation, use the numpy.linalg.solve() method in Python.
print("\nResult...\n",np.linalg.solve(arr1, arr2))