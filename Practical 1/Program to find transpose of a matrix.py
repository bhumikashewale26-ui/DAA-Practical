#Practical1.4
# Program to find transpose of a matrix
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []
print("Enter matrix elements")
for i in range(rows):
  row = []
  for j in range(cols):
      row.append(int(input()))
  matrix.append(row)
print("\nOriginal Matrix")
for i in range(rows):
  for j in range(cols):
      print(matrix[i][j], end=" ")
  print()
print("\nTranspose Matrix")
for j in range(cols):
  for i in range(rows):
      print(matrix[i][j], end=" ")
  print()






