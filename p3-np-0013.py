import numpy as np
# Meredith Aguirre NC = 0013 Fecha 22/10/2026

n0013 = np.array([10, 20, 30, 40, 50])
print(n0013)
print(n0013[0])
print(n0013[3])
print(n0013[-1])
print(n0013[-2])
print("------------------------------")
n0013 = np.array([
    [10, 20, 30],
    [ 40, 50, 60]
])
print(n0013)
print(n0013[0, 0])
print(n0013[1, 2])
print(n0013[-1, -1])
print(n0013[-2, -2])
print("------------------------------")
# 3D array 2x(2x3)
n0013 = np.array([
    [
        [10, 20, 30],
        [ 40, 50, 60]
    ],
    # 1 -1 
    [
        [70, 80, 90],
        [100, 110, 120]
    ]            
])
print(n0013)
print(n0013[0, 0, 0])
print(n0013[1, 1, 2])
print(n0013[-1, -1, -2])
print("Meredith Aguirre NC = 0013")