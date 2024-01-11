
matrixA = [
           [1,2,3],
           [4,5,6],
           [7,8,9]
         ]

matrixB= [
          [10,5,76],
          [5,71,49],
          [12,32,42]
         ]

print("Matrix addition : ")
for i in range(0,3):
    for j in range(0,3):
        print(matrixA[i][j]+matrixB[i][j], end=" ")
    print("\n")

print("Matrix subtraction : ")
for i in range(0,3):
    for j in range(0,3):
        print(matrixB[i][j]-matrixA[i][j], end=" ")
    print("\n")

print("Matrix multiplication : ")
for i in range(0,3):
    for j in range(0,3):
        print(matrixA[i][j]*matrixB[i][j], end=" ")
    print("\n")

print("Matrix division : ")
for i in range(0,3):
    for j in range(0,3):
        print(matrixB[i][j]/matrixA[i][j], end=" ")
    print("\n")
