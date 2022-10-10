import matplotlib.pyplot as plt
import numpy as np

file = open("avr", "r")
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


plt.xlabel("Individuals of population")
plt.ylabel("Average fitness value of population")
plt.title("GA with Ackley Fitness Function")
plt.show()