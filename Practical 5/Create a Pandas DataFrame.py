# Practical 5
#Create a Pandas DataFrame
import pandas as pd
data = {
  "Name": ["Rahul", "Priya", "Amit", "Sneha"],
  "Marks": [75, 85, 65, 90]
}
df = pd.DataFrame(data)
print(df)
print("\nStatistical Information:")
print(df["Marks"].describe())


#Create_Pandas_Series_from_Dictionary
marks = {
  "Rahul": 75,
  "Priya": 85,
  "Amit": 65,
  "Sneha": 90
}
series = pd.Series(marks)
print(series)


#filter_pandas_series
marks = pd.Series([55, 75, 80, 60, 90])
result = marks[marks > 70]
print("Marks greater than 70:")
print(result)


#Simple Student Data Analysis
data = {
  "Name": ["Rahul", "Priya", "Amit", "Sneha", "Kiran"],
  "Marks": [75, 85, 60, 90, 65],
  "Attendance": [80, 90, 75, 95, 70]


}
df = pd.DataFrame(data)
print("Student Data:")
print(df)
print("\nStudents scoring more than 70:")
print(df[df["Marks"] > 70])






