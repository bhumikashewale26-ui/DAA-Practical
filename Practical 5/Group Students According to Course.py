#Practical 6.2
#Group Students According to Course
import pandas as pd
data = {


  "Name": ["Rahul", "Priya", "Amit", "Sneha"],


  "Course": ["BSc", "BCA", "BSc", "BCA"],


  "Marks": [80, 90, 70, 85]


}
df = pd.DataFrame(data)
result = df.groupby("Course")["Marks"].mean()
print(result)


#Count Students in Each Course
data = {


  "Name": ["Rahul", "Priya", "Amit", "Sneha"],


  "Course": ["BSc", "BCA", "BSc", "BCA"]


}
df = pd.DataFrame(data)
print(df["Course"].value_counts())


#Find Top 3 Students
data = {


  "Name": ["Rahul", "Priya", "Amit", "Sneha", "Kiran"],


  "Marks": [75, 95, 65, 90, 85]


}
df = pd.DataFrame(data)
result = df.sort_values("Marks", ascending=False)
print(result.head(3))


#Add a Result Column
import pandas as pd
data = {


  "Name": ["Rahul", "Priya", "Amit", "Sneha"],


  "Marks": [75, 35, 65, 90]


}
df = pd.DataFrame(data)
df["Result"] = df["Marks"].apply(


  lambda x: "Pass" if x >= 40 else "Fail"


)
print(df)


#Simple Bar Chart
import matplotlib.pyplot as plt


names = ["Rahul", "Priya", "Amit", "Sneha"]
marks = [75, 90, 65, 85]
plt.bar(names, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()


#Simple Line Graph


months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 150, 130, 180]
plt.plot(months, sales)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.show()


#Simple Histogram


marks = [50, 60, 65, 70, 70, 75, 80, 85, 90, 95]
plt.hist(marks)
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Marks")
plt.show()
