
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

T = [[0,0,0],
    [0,0,0],
    [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        T[j][i] = X[i][j]
for t in T: print(t)

