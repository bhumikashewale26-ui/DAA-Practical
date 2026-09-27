#Practical 1.1
#Program to insert an element in an array
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
  num = int(input("Enter element: "))
  arr.append(num)
print("Original Array:", arr)
position = int(input("Enter position to insert (1 to {}): ".format(n + 1)))
element = int(input("Enter element to insert: "))
arr.insert(position - 1, element)
print("Array after insertion:")
print(arr)


