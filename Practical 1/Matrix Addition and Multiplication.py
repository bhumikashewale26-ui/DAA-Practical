#Practical1.3
# Matrix Addition and Multiplication
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
A = []
B = []
print("Enter elements of Matrix A")
for i in range(rows):
  row = []
  for j in range(cols):
      row.append(int(input()))
  A.append(row)
print("Enter elements of Matrix B")
for i in range(rows):
  row = []
  for j in range(cols):
      row.append(int(input()))
  B.append(row)
print("\nAddition of Matrices")
for i in range(rows):
  for j in range(cols):
      print(A[i][j] + B[i][j], end=" ")
  print()
print("\nMultiplication of Matrices")
result = []
for i in range(rows):
  row = []
  for j in range(cols):
      total = 0
      for k in range(cols):
          total = total + A[i][k] * B[k][j]
      row.append(total)
  result.append(row)
for i in range(rows):
  for j in range(cols):
      print(result[i][j], end=" ")
  print()










