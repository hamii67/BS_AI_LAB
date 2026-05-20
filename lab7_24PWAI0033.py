import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# 1 Line Graph
days = ["Mon","Tue","Wed","Thu","Fri"]
temp = [30,32,31,35,33]

plt.plot(days,temp)
plt.title("Temperature")
plt.xlabel("Days")
plt.ylabel("Temp")
plt.grid()
plt.show()

# 2 Bar Chart
students = ["Ali","Sara","Ahmed","Ayesha"]
marks = [78,85,90,72]

plt.bar(students,marks,color=["red","blue","green","orange"])
plt.title("Student Marks")

for i in range(len(marks)):
    plt.text(i,marks[i],marks[i])

plt.show()

# 3 Histogram
data = np.random.randint(0,100,500)

plt.hist(data,bins=10,color="skyblue")
plt.title("Histogram")
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.show()

# 4 Scatter Plot
hours = [1,2,3,4,5,6,7]
marks = [40,45,50,60,70,80,90]

plt.scatter(hours,marks,color="red")
plt.title("Study Hours vs Marks")
plt.show()

# 5 Seaborn Lineplot
x = [1,2,3,4,5]
y = [10,20,25,30,40]

sns.lineplot(x=x,y=y)
plt.title("Seaborn Line")
plt.show()

plt.plot(x,y)
plt.title("Matplotlib Line")
plt.show()

# 6 Heatmap
a = np.random.rand(5,5)

sns.heatmap(a,annot=True)
plt.title("Heatmap")
plt.show()

# 7 Scatter using both

x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.scatter(x,y)
plt.title("Matplotlib Scatter")
plt.show()

sns.scatterplot(x=x,y=y)
plt.title("Seaborn Scatter")
plt.show()

print("Seaborn looks more beautiful")
print("Because colors and style are better")

# 8 Mini Dataset

names = ["Ali","Sara","Ahmed","Ayesha","Usman"]
marks = [78,85,90,72,88]
att = [80,90,95,70,85]

df = pd.DataFrame({
    "Marks":marks,
    "Attendance":att
})

# Bar chart
plt.bar(names,marks)
plt.title("Class Marks")
plt.show()

# Line chart
plt.plot(names,att)
plt.title("Attendance")
plt.show()

# Heatmap
sns.heatmap(df.corr(),annot=True)
plt.title("Marks and Attendance")
plt.show()