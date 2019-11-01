import matplotlib.pyplot as plt
import csv

file = 'cn.csv'

x = []
y = []

with open(file) as data_file:
	reader = csv.reader(data_file)
	for row in reader:
		y.append(row[3])
		x.append(row[4])

del x[0]
del y[0]

x = [int(i) for i in x]
y = [float(i) for i in y]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x, y, s=200)

ax.set_title("China", fontsize=24)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("GDP per capita", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()