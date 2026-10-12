# ============================================================
# NUMPY CHEAT SHEET
# ============================================================

import numpy as np


# ============================================================
# 1. CREATE ARRAYS
# ============================================================

# np.array() → create an array
a = np.array([1, 2, 3, 4])
print("Array:", a)

# 2D array
b = np.array([[1, 2], [3, 4]])
print("2D Array:\n", b)

# np.zeros() → array filled with 0
print("Zeros:", np.zeros(5))

# np.ones() → array filled with 1
print("Ones:", np.ones(5))

# zeros((rows, columns))
print("2x3 Zeros:\n", np.zeros((2, 3)))

# ones((rows, columns))
print("2x3 Ones:\n", np.ones((2, 3)))

# np.arange(start, stop, step)
# stop value is NOT included
print("Arange:", np.arange(0, 10, 2))

# np.linspace(start, stop, number_of_values)
# stop value IS included
print("Linspace:", np.linspace(0, 1, 5))

# np.eye(n) → identity matrix
print("Identity Matrix:\n", np.eye(3))


# ============================================================
# 2. INSPECT ARRAY
# ============================================================

a = np.array([[1, 2, 3],
              [4, 5, 6]])

# ndim → number of dimensions
print("Dimensions:", a.ndim)

# shape → (rows, columns)
print("Shape:", a.shape)

# size → total number of elements
print("Size:", a.size)

# dtype → data type of elements
print("Data Type:", a.dtype)


# ============================================================
# 3. INDEXING
# ============================================================

a = np.array([10, 20, 30, 40, 50])

print("First element:", a[0])
print("Third element:", a[2])
print("Last element:", a[-1])


# 2D indexing
b = np.array([[1, 2, 3],
              [4, 5, 6]])

# b[row, column]
print("Element at row 0, column 1:", b[0, 1])
print("Element at row 1, column 2:", b[1, 2])


# ============================================================
# 4. SLICING
# ============================================================

a = np.array([10, 20, 30, 40, 50])

# [start : stop]
# stop is NOT included
print("a[1:4]:", a[1:4])

# First 3 elements
print("a[:3]:", a[:3])

# From index 2 to end
print("a[2:]:", a[2:])

# Reverse array
print("Reverse:", a[::-1])


# 2D slicing
b = np.array([[1, 2, 3],
              [4, 5, 6]])

# All rows, column 1 → second column
print("Second column:", b[:, 1])

# Row 0, all columns → first row
print("First row:", b[0, :])


# ============================================================
# 5. CALCULATE / MATHEMATICAL OPERATIONS
# ============================================================

a = np.array([1, 2, 3])

# Operations are performed element-by-element
print("a + 2:", a + 2)
print("a - 2:", a - 2)
print("a * 2:", a * 2)
print("a / 2:", a / 2)
print("a ** 2:", a ** 2)


# Array + Array
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("a + b:", a + b)
print("a * b:", a * b)


# ============================================================
# 6. STATISTICS
# ============================================================

a = np.array([10, 20, 30, 40, 50])

print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Median:", np.median(a))
print("Minimum:", np.min(a))
print("Maximum:", np.max(a))
print("Standard Deviation:", np.std(a))
print("Variance:", np.var(a))


# ============================================================
# 7. RESHAPE
# ============================================================

a = np.arange(6)

print("Original:", a)

# reshape → change dimensions
print("Reshaped:\n", a.reshape(2, 3))

# flatten → convert to 1D
b = np.array([[1, 2], [3, 4]])
print("Flatten:", b.flatten())

# transpose → rows become columns
print("Transpose:\n", b.T)


# ============================================================
# 8. FILTER / WHERE
# ============================================================

a = np.array([10, 20, 30, 40, 50])

# Condition produces True/False values
print("a > 25:", a > 25)

# Boolean filtering
print("Values > 25:", a[a > 25])

# np.where() → find indices satisfying condition
print("Indices where a > 25:", np.where(a > 25))


# ============================================================
# 9. COMBINE ARRAYS
# ============================================================

a = np.array([1, 2])
b = np.array([3, 4])

# concatenate → join arrays
print("Concatenate:", np.concatenate([a, b]))

# vstack → vertical stacking
print("Vertical Stack:\n", np.vstack([a, b]))

# hstack → horizontal stacking
print("Horizontal Stack:", np.hstack([a, b]))


# ============================================================
# 10. RANDOM
# ============================================================

# Random numbers between 0 and 1
print("Random:", np.random.rand(3))

# Random integers
# randint(low, high, size)
# high is NOT included
print("Random Integers:", np.random.randint(1, 10, 5))

# seed → same random results every time
np.random.seed(42)
print("Fixed Random:", np.random.rand(3))


# ============================================================
# 11. LINEAR ALGEBRA
# ============================================================

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Dot product
print("Dot Product:", np.dot(a, b))

# @ → matrix multiplication
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix Multiplication:\n", A @ B)

# Transpose
print("Transpose:\n", A.T)

# Inverse
print("Inverse:\n", np.linalg.inv(A))

# Determinant
print("Determinant:", np.linalg.det(A))