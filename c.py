import csv
import matplotlib.pyplot as plt

scores = []
dates = []

file = 'us.csv'

with open(file) as data_file:
    reader = csv.reader(data_file)
    for row in reader:
        scores.append(row[3])
        dates.append(row[4])

del scores[0]
del dates[0]


## List Comprehensions
dates = [int(i) for i in dates]
scores = [float(i) for i in scores]

plt.plot(dates, scores)
plt.xlabel('Year')
plt.ylabel('GDP per capita')
plt.title('USA')
plt.show()