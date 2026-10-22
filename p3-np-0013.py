import numpy as np
# Meredith Aguirre NC = 0013 Fecha 22/10/2026

n = np.array([10, 20, 30, 40, 50])
print(n)
print(n[0])
print(n[3])
print(n[-1])
print(n[-2])
print("------------------------------")
n = np.array([
    [10, 20, 30],
    [ 40, 50, 60]
])
print(n)
print(n[0, 0])
print(n[1, 2])
print(n[-1, -1])
print(n[-2, -2])
print("------------------------------")
# 3D array 2x(2x3)
n = np.array([
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
print(n)
print(n[0, 0, 0])
print(n[1, 1, 2])
print(n[-1, -1, -2])
print("Meredith Aguirre NC = 0013")