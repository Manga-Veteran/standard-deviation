import csv

with open('c105csv-main/class1.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

#To remove headers from CSV
file_data.pop(0)

total_marks = 0
total_entries = len(file_data)

for marks in file_data:
    total_marks += float(marks[1])

mean = total_marks / total_entries
print("Mean (Average) is -> "+str(mean))

import pandas as pd
import plotly.express as px

df = pd.read_csv("c105csv-main/class1.csv")

fig = px.scatter(df,    x="student number",
                        y="marks"
            )
fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= mean, y1= mean,
      x0= 0, x1= total_entries
    )
])

fig.update_yaxes(rangemode="tozero")

fig.show()

##################################################

import csv

with open('c105csv-main/class2.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

#To remove headers from CSV
file_data.pop(0)

total_marks = 0
total_entries = len(file_data)

for marks in file_data:
    total_marks += float(marks[1])

mean = total_marks / total_entries
print("Mean (Average) is -> "+str(mean))

import pandas as pd
import plotly.express as px

df = pd.read_csv("c105csv-main/class2.csv")

fig = px.scatter(df,    x="student name",
                        y="marks"
            )
fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= mean, y1= mean,
      x0= 0, x1= total_entries
    )
])

fig.update_yaxes(rangemode="tozero")

fig.show()

import math

import csv
with open("c105csv-main/data.csv", newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
    data = file_data[0]

def mean(data):
    n =len(data)
    total =0
    for x in data:
        total += int(x)
    mean = total/n
    return mean

squared_list= []
for number in data:
    a = int(number) - mean(data)
    a = a**2
    squared_list.append(a)

sum = 0
for i in squared_list:
    sum = sum + i

result = sum/ (len(data)-1)

std_deviation = math.sqrt(result)
print(std_deviation)