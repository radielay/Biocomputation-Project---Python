import matplotlib.pyplot as plt
import numpy as np

file = open("graph", "r")
list = []

for line in file:
    stripped = line.strip()
    line_list = stripped.split(",")

    list.append(line_list)

file.close()

for num in range(0, len(list)):
    for fl in range(0, len(list[num])):
        list[num][fl] = float(list[num][fl])
    plt.plot(list[num])

s = 0
for n in range(0, len(list)):
    range = len(list[n])
    s += list[n][range-1]
s /= len(list)

print(s)

plt.xlabel("Individuals of population")
# plt.ylabel("Average fitness value of population")
plt.ylabel("The best individual in population")
plt.title("GA with Ackley Fitness Function")
plt.show()
