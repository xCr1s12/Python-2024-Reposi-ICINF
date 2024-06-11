def random(X):
    return X % 2 == 0 
def cubo(X):
   return X **3
A = [1,2,3,4,5]
B = [3,4,5,6,]

A_B = list(map(cubo , A))
print(A_B)

B_A = list(filter(random,B))
print(B_A)