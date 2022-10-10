import copy
import random
import math
import matplotlib.pyplot as plt

N = 50
P = 100

worst_individuals = []
average = []


class Individual:
    def __init__(self):
        self.gene = [0]*N
        self.fitness = 0


def initialise_population100():
    pop = []

    for x in range(0, P):
        temp_gene = []
        for n in range(0, N):
            r = random.uniform(-100, 100)
            temp_gene.append(r)     # Create a gene of the float values

        new_ind = Individual()
        new_ind.gene = temp_gene.copy()
        pop.append(new_ind)

    return pop


population = initialise_population100()


def mutation_gaussian(pop):
    mut_rate = 0.06
    mut_step = 1
    mutated = []

    for i in range(0, P):
        new_ind = Individual()
        new_ind.gene = []
        for j in range(0, N):
            gene = pop[i].gene[j]
            mut_prob = random.random()
            if mut_prob < mut_rate:       # Mutation function
                alter = random.gauss(0, mut_step)
                print("alter: ", alter)
                gene *= alter

            new_ind.gene.append(gene)
        mutated.append(new_ind)

    return mutated


mutated = mutation_gaussian(population)
print(" ")

