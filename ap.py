import csv
import matplotlib.pyplot as plt

def read_country(file):
	x = []
	y = []

	with open(file) as data_file:
		reader = csv.reader(data_file)
		for row in reader:
			x.append(row[4])
			y.append(row[3])

	del x[0]
	del y[0]

	x = [int(i) for i in x]
	y = [float(i) for i in y]

	return x,y

cnX, cnY = read_country("cn.csv")
usX, usY = read_country("us.csv")
brX, brY = read_country("br.csv")
frX, frY = read_country("fr.csv")
jpX, jpY = read_country("jp.csv")

#plt.style.use('seaborn')

plt.plot(cnX, cnY, label="China")
plt.plot(usX, usY, label="USA")
plt.plot(brX, brY, label="Brazil")
plt.plot(frX, frY, label="France")
plt.plot(jpX, jpY, label="Japan")

plt.xlabel('Year')
plt.ylabel('GDP per capita')
plt.title('Countries')
plt.legend(loc='upper left', numpoints = 1 )
# Show the major grid lines with dark grey lines
plt.grid(b=True, which='major', color='#666666', linestyle='-')

# Show the minor grid lines with very faint and almost transparent grey lines
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
plt.show()