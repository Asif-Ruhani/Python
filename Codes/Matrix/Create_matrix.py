
"""matrix = [ [1,2,3],[4,5,6] ]
print(matrix[1][2])"""





"""matrix = [
           [1,2,3],
           [4,5,6],
           [7,8,9]
         ]
print(matrix[2][1])"""






matrix = [
           [1,2,3],
           [4,5,6],
           [7,8,9]
         ]
for row in matrix:
    for col in row:
       # print(col)
        print(col, end=" ") # end=" " this break automatic end line
    print("\n")

