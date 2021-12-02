import csv
from random import choices

countries = ["Finland", "Germany", "South Korea", "Nepal", "United States"]

population = {
    "Finland": 5528737,
    "Germany": 83240000,
    "South Korea": 51780000,
    "Nepal": 29140000,
    "United States": 329500000,
}

our_data = {}


with open("cumulative-covid-vaccinations.csv", newline="") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=",")
    for row in spamreader:
        if row[0] in countries:
            if row[0] in our_data:
                our_data[row[0]].append(row[3])
            else:
                our_data[row[0]] = [row[3]]


# cleaning our data so it has the  same length
m = 100000000000
for c in our_data:
    m = min(m, len(c))

for i in range(len(our_data)):
    temp = choices(our_data[countries[i]], k = m)
    temp.sort()
    our_data[countries[i]] = temp


for c in countries:
    with open(c + "_output.csv", "w") as outputfile:
        spamwriter = csv.writer(outputfile, delimiter=",")
        size = len(our_data[c])
        i = 0
        for x in our_data[c]:
            r = [c, i / size, int(x) / (2 * population[c])]
            spamwriter.writerow(r)
            i = i + 1
