
import  numpy as np

# Two matrices
mx1 = np.array([[5, 10], [15, 20]])
mx2 = np.array([[25, 30], [35, 40]])

print("Matrix1 =\n",mx1)
print("\nMatrix2 =\n",mx2)

# The addition() is used to add matrices
print ("\nAddition of two matrices: ")
print (np.add(mx1,mx2))

# The subtract() is used to subtract matrices
print ("\nSubtraction of two matrices: ")
print (np.subtract(mx1,mx2))

# The divide() is used to divide matrices
print ("\nMatrix Division: ")
print (np.divide(mx1,mx2))

# The multiply()is used to multiply matrices
print ("\nMultiplication of two matrices: ")
print (np.multiply(mx1,mx2))
