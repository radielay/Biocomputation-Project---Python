import copy
import random
import matplotlib.pyplot as plt

N = 50
P = 50

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
        fitness = 0.0
        for n in range(0, N):
            r = random.uniform(0.0, 1.0)  # Random float with 1 number after decimal point (0.0 to 1.0)
            r = "%.1f" % r
            r = float(r)
            temp_gene.append(r)     # Create a gene of the float values
            fitness += r         # Evaluate initial population

        new_ind = Individual()
        new_ind.gene = temp_gene.copy()
        new_ind.fitness = fitness
        pop.append(new_ind)

    return pop


population = initialise_population()


def average_fitness(pop):

    total_fitness = 0
    av_fitness = []

    for i in range(0, P):
        ind = pop[i]
        total_fitness += ind.fitness        # Find the total fitness of a population

    av = total_fitness / P               # Calculate the average fitness (for plotting)
    av_fitness.append(av)

    return av_fitness


def selection(pop):
    offspring = []

    for i in range(0, P):
        parent1 = random.randint(0, P-1)    # Choose 2 individuals at random
        off1 = pop[parent1]
        parent2 = random.randint(0, P-1)
        off2 = pop[parent2]
        if off1.fitness < off2.fitness:      # Save the better one
            offspring.append(off1)
        else:
            offspring.append(off2)

    return offspring


def crossover(pop):
    offs = []

    ind1 = Individual()
    ind2 = Individual()
    temp = Individual()
    for i in range(0, P, 2):
        ind1 = copy.deepcopy(pop[i])
        ind2 = copy.deepcopy(pop[i+1])      # Get every 2 individuals of the population
        temp = copy.deepcopy(pop[i])
        cross_point = random.randint(1, N)    # Get random crossing point

        for j in range(cross_point, N):     # Exchange the individuals' tails (after the crossing point)
            ind1.gene[j] = ind2.gene[j]
            ind2.gene[j] = temp.gene[j]

        offs1 = copy.deepcopy(ind1)
        offs2 = copy.deepcopy(ind2)
        offs.append(offs1)
        offs.append(offs2)

    return offs


def mutation(pop):
    mut_rate = 0.05
    mut_step = 0.1
    mutated = []

    for i in range(0, P):
        new_ind = Individual()
        new_ind.gene = []
        for j in range(0, N):
            gene = pop[i].gene[j]
            mut_prob = random.random()
            if mut_prob < mut_rate:       # Mutation function
                alter = random.uniform(0.0, mut_step)
                alter = "%.1f" % alter
                alter = float(alter)
                if gene < 1:
                    gene += alter      # Add float from a defined range, if the gene is smaller than 1.0
                    if gene > 1:
                        gene = 1.0
                else:
                    gene -= alter    # Subtract float from a defined range, if the gene is bigger than 1.0
                    if gene < 0:
                        gene = 0

            new_ind.gene.append(gene)
        mutated.append(new_ind)

    return mutated


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


def fitness_value(pop):

    for ind in pop:
        gene = ind.gene
        fitness = 0            # Give fitness value to a chosen population
        for i in range(0, N):
            fitness += gene[i]
        ind.fitness = fitness


def main():
    global population
    global worst_individuals     # For plotting
    global average              # For plotting

    ind_small = worst_ind(population)
    smallest = copy.deepcopy(population[ind_small])  # Get the smallest individual of each population
    worst_individuals.append(smallest.fitness)

    av = average_fitness(population)              # Get the average fitness of each population
    average.append(av)

    offspring = selection(population)

    recombined = crossover(offspring)

    new_generation = mutation(recombined)
    fitness_value(new_generation)          # Evaluate each new generation

    index = best_ind(new_generation)    # Find the biggest individual in the new generation
    new_generation[index] = copy.deepcopy(smallest)    # Replace it with the smallest individual of the original pop

    population = copy.deepcopy(new_generation)


for m in range(0, 50):
    main()


plt.plot(average)
# plt.plot(worst_individuals)
plt.show()
