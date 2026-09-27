#Practical 4
# array using numpy
import numpy as np
numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("Array:", numbers)
print("Original array:", numbers)
print("Addition:", numbers + 5)
print("Subtraction:", numbers - 5)
print("Multiplication:", numbers * 2)
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))
print("Original array:", numbers)
print("First five elements:", numbers[0:5])


numberse = np.array([20, 45, 60, 75, 30, 90])
result = numbers[numbers > 50]
print("Values greater than 50:", result)


