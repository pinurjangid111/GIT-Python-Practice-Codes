A = [[10, 13, 44],
[11, 2, 3],
[5, 3, 1]]

B = [[7, 16,-6],
[9, 20, -4],
[-1, 3 , 27]]

C = [[0,0,0],
     [0,0,0],
     [0,0,0]]
matrix_length = len(A)

for i in range(len(A)):
    for k in range(len(B)):
        C[i][k] = A[i][k] + B[i][k]

print("The sum of Matrix :  ")
for i in C:
    print (i)
