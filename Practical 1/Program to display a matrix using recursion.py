#Practical 1.2
# Program to display a matrix using recursion
def display(matrix, rows, cols, i, j):
  if i == rows:
      return
  print(matrix[i][j], end=" ")
  if j == cols - 1:
      print()
      display(matrix, rows, cols, i + 1, 0)
  else:
      display(matrix, rows, cols, i, j + 1)
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []
print("Enter matrix elements:")
for i in range(rows):
  row = []
  for j in range(cols):
      row.append(int(input()))
  matrix.append(row)
print("\nMatrix:")
display(matrix, rows, cols, 0, 0)




