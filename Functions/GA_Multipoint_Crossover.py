import copy
import random
import matplotlib.pyplot as plt

N = 10
P = 2

worst_individuals = []
average = []


class Individual:
    def __init__(self):
        self.gene = [0]*N
        self.fitness = 0


def initialise_population():
    pop = []

    for x in range(0, P):
        temp_gene = []
        for n in range(0, N):
            r = random.uniform(1, 10)
            r = int(r)
            temp_gene.append(r)     # Create a gene of the float values

        new_ind = Individual()
        new_ind.gene = temp_gene.copy()
        pop.append(new_ind)

    return pop


population = initialise_population()

for obj in population:
    print(obj.gene)


def crossover_multi_point(pop):
    offs = []
    temp1 = []
    temp2 = []

    for i in range(0, P, 2):

        parent1 = copy.deepcopy(pop[i])
        parent2 = copy.deepcopy(pop[i+1])

        r1 = random.randint(1, 5)
        r2 = random.randint(5, 8)
        print("Random: ", r1, r2)

        for n in range(r1, r2):
            temp1.append(parent1.gene[n])
            temp2.append(parent2.gene[n])

        t = 0
        for n in range(r1, r2):
            parent1.gene[n] = copy.deepcopy(temp2[t])
            parent2.gene[n] = copy.deepcopy(temp1[t])
            t += 1

        offs1 = copy.deepcopy(parent1)
        offs2 = copy.deepcopy(parent2)
        offs.append(offs1)
        offs.append(offs2)

    return offs


offspring = crossover_multi_point(population)
print(" ")
for obj in offspring:
    print(obj.gene)
