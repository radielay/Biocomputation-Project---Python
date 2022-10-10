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


def crossover_arithmetic(pop):
    # a = 0.6
    a = 0.1
    offs = []

    for i in range(0, P, 2):
        parent1 = copy.deepcopy(pop[i])
        parent2 = copy.deepcopy(pop[i+1])

        offs1 = []
        offs2 = []

        for n in range(0, N):
            temp1 = a * parent1.gene[n]
            tail = a - 1
            tail *= parent2.gene[n]
            temp1 += tail
            # ind1.gene = temp1
            offs1.append(temp1)

            temp2 = a * parent2.gene[n]
            tail2 = a - 1
            tail2 *= parent1.gene[n]
            temp2 += tail2
            # ind2.gene = temp2
            offs2.append(temp2)

        offs.append(offs1)
        offs.append(offs2)

    return offs


offspring = crossover_arithmetic(population)
for obj in offspring:
    print(obj)
