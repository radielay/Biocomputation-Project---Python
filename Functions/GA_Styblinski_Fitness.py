import copy
import random
import math
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


def fitness_value_st(pop):

    for ind in pop:
        gene = copy.deepcopy(ind.gene)
        fitness = 0            # Give fitness value to a chosen population

        for i in range(0, N):
            x = gene[i]
            sigma = x * x * x * x
            multiply = x * x
            multiply *= 16
            sigma -= multiply
            multiply = 5 * x
            sigma += multiply

            fitness += sigma

        fitness /= 2
        ind.fitness = fitness


fitness_value_st(population)
for obj in population:
    print(obj.gene, obj.fitness)