#Practical 6.1
#2Darray using numpy
import numpy as np
arr = np.array([
  [10, 20, 30],
  [40, 50, 60]
])
print(arr)
print("Shape:", arr.shape)
#Reshape an Array
arr = np.array([1, 2, 3, 4, 5, 6])
new_arr = arr.reshape(2, 3)
print(new_arr)
#Generate Random Numbers
numbers = np.random.randint(1, 100, 10)
print(numbers)


#Calculate Mean, Median and Standard Deviation
marks = np.array([60, 70, 80, 90, 75])
print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))






