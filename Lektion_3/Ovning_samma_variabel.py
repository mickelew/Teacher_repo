A = "Hej"
B = "Hallå"
C = A
A = B
B = C
print(A)
print(B)
A = "Hej"
B = "Hallå"
A, B = B, A
print(A)
print(B)
# Multipel tilldelning. Alla variabler får samma värde.
X = Y = Z = 75
print(X)
print(Y)
print(Z)