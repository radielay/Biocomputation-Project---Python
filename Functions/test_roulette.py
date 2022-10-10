import copy
import random
import math
import numpy as np
import matplotlib.pyplot as plt

N = 20
P = 50

worst_individuals = []
average = []


class Individual:
    def __init__(self):
        self.gene = [0]*N
        self.fitness = 0
        self.prob = 0


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


def fitness_value_rose(pop):

    for ind in pop:
        gene = ind.gene
        fitness = 0            # Give fitness value to a chosen population
        for i in range(0, N-1):
            x = gene[i]
            power = x * x
            num = x + 1
            num -= power
            power2 = num * num
            sigma = 100 * power2
            sub = 1 - x
            power3 = sub * sub
            sigma += power3

            fitness += sigma
        ind.fitness = fitness


# fitness_value_rose(population)

def fitness_value(pop):

    for ind in pop:
        gene = ind.gene
        fitness = 0            # Give fitness value to a chosen population
        for i in range(0, N):
            x = gene[i]
            power = x * x
            multi = 2 * math.pi * x
            cosine = math.cos(multi)  # in radians
            cosine *= 10
            sigma = power - cosine
            fitness += sigma

        fitness += 10 * N
        ind.fitness = fitness


fitness_value(population)


def roulette_wheel2(pop):
    offs = []
    total_fitness = 0

    for i in range(0, P):
        ind = pop[i]
        total_fitness += ind.fitness  # Find the total fitness of a population

    for i in range(0, P):
        selected = random.uniform(0, total_fitness)
        running_total = total_fitness
        n = 0
        while running_total >= selected:
            running_total -= pop[n].fitness
            n += 1

            if n == len(pop):
                offs.append(pop[n - 1])
                break

        offs.append(pop[n - 1])

    return offs


def roulette_wheel3(pop):
    offs = []
    total_fitness = 0

    for i in range(0, P):
        ind = pop[i]
        total_fitness += ind.fitness  # Find the total fitness of a population
    print("TOTAL: ", total_fitness)

    for i in range(0, P):
        ind = pop[i]
        probability = pop[i].fitness / total_fitness
        probability = 1 - probability
        ind.prob = probability
        offs.append(ind)

    return offs


def roulette_wheel(pop):
    offs = []
    total_fitness = 0

    for i in range(0, P):
        ind = pop[i]
        total_fitness += ind.fitness  # Find the total fitness of a population

    while len(offs) < P:
        for i in range(0, P):
            ind = pop[i]
            probability = ind.fitness / total_fitness
            probability = 1 - probability
            selected = random.uniform(0.96, 1.0)
            ind.prob = probability
            if probability >= selected:
                offs.append(ind)

    return offs


def best_ind(pop):

    index = 0
    best = pop[0].fitness
    for i in range(1, P):
        ind = pop[i].fitness  # Find the best individual of the given pop
        if ind > best:
            best = ind
            index = i   # return the index of the best individual

    return index


def worst_ind(pop):

    index = 0
    worst = pop[0].fitness
    for i in range(1, P):
        ind = pop[i].fitness       # Find the worst individual in a population
        if ind < worst:
            worst = ind
            index = i     # Return the index of that individual

    return index


def main():

    offspring = roulette_wheel(population)
    for obj in offspring:
        print(obj.fitness)
        # print(obj.prob)

    print("Length: ", len(offspring))

    """index_small = worst_ind(population)
    smallest = copy.deepcopy(population[index_small])

    index = best_ind(population)  # Find the biggest individual in the new generation
    population[index] = copy.deepcopy(smallest)"""


main()

"""for m in range(0, 50):
    main()"""

print("POPULATION")
for m in range(0, P):
    print(population[m].fitness)

