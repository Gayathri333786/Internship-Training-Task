import numpy as np

# Matrix (Students × Subjects)
marks = np.array([
    [80, 75, 90],
    [85, 70, 88],
    [90, 95, 92]
])

print("Original Matrix:\n", marks)

# 1. Scalar
bonus_marks = 5
updated_marks = marks + bonus_marks
print("\nAfter Bonus Marks (Scalar):\n", updated_marks)

# 2. Vector
attendance = np.array([5, 3, 4])
print("\nAttendance Vector:", attendance)

# 3. Matrix Addition
extra_test = np.array([
    [2, 3, 1],
    [1, 2, 2],
    [3, 1, 2]
])

total_marks = marks + extra_test
print("\nMatrix Addition:\n", total_marks)

# 4. Matrix Multiplication
weights = np.array([
    [0.4],
    [0.3],
    [0.3]
])

weighted_score = marks @ weights
print("\nWeighted Scores:\n", weighted_score)

# 5. Transpose
print("\nTranspose Matrix:\n", marks.T)

# 6. Identity Matrix
I = np.eye(3)
print("\nIdentity Matrix:\n", I)

print("\nMarks × Identity Matrix:\n", marks @ I)

# 7. Determinant
sample = np.array([
    [2, 3],
    [1, 4]
])

det = np.linalg.det(sample)
print("\nDeterminant:", det)

# 8. Inverse Matrix
inverse = np.linalg.inv(sample)
print("\nInverse Matrix:\n", inverse)

# 9. Eigenvalues & Eigenvectors
eig_values, eig_vectors = np.linalg.eig(sample)

print("\nEigenvalues:\n", eig_values)
print("\nEigenvectors:\n", eig_vectors)
