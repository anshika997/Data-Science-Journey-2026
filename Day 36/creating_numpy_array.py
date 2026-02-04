# creating_numpy_array.py
# Topic: Creating NumPy Arrays

import numpy as np

# 1. Create array using array()
arr1 = np.array([1, 2, 3, 4])
print("Array using array():", arr1)

# 2. Create 2D array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("2D Array:\n", arr2)

# 3. Create array of zeros
zeros_1d = np.zeros(5)
zeros_2d = np.zeros((2, 3))
print("Zeros 1D:", zeros_1d)
print("Zeros 2D:\n", zeros_2d)

# 4. Create array of ones
ones_1d = np.ones(4)
ones_2d = np.ones((3, 2))
print("Ones 1D:", ones_1d)
print("Ones 2D:\n", ones_2d)

# 5. Create array using arange()
range_arr = np.arange(1, 10)
step_arr = np.arange(0, 10, 2)
print("Arange:", range_arr)
print("Arange with step:", step_arr)

# 6. Create array using linspace()
lin_arr = np.linspace(1, 10, 5)
print("Linspace:", lin_arr)

# 7. Identity matrix
identity = np.eye(3)
print("Identity Matrix:\n", identity)

# 8. Random arrays
rand_arr = np.random.rand(3)
rand_int = np.random.randint(1, 10, size=(2, 3))
print("Random floats:", rand_arr)
print("Random integers:\n", rand_int)
