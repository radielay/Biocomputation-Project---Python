import copy
import random
import math
import matplotlib.pyplot as plt

N = 10
P = 5000

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


# population = initialise_population100()


def initialise_population32():
    pop = []

    for x in range(0, P):
        temp_gene = []
        for n in range(0, N):
            r = random.uniform(-32, 32)
            r = int(r)
            temp_gene.append(r)     # Create a gene of the float values

        new_ind = Individual()
        new_ind.gene = temp_gene.copy()
        pop.append(new_ind)

    return pop


population = initialise_population32()


def fitness_value_rast(pop):

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


# fitness_value_rast(population)


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


# fitness_value_st(population)


def fitness_value_ack(pop):

    for ind in pop:
        gene = ind.gene         # Give fitness value to a chosen population
        sigma = 0
        for i in range(0, N):
            x = gene[i]
            power = x * x
            sigma += power

        fraction = 1 / N
        sigma *= fraction
        sq = math.sqrt(sigma)
        sq *= -0.2

        sigma = 0
        for i in range(0, N):
            x = gene[i]
            mul = 2 * math.pi * x
            cosine = math.cos(mul)
            sigma += cosine

        sigma *= fraction
        e = math.exp(sigma)

        total = sq - e
        fitness = math.exp(total)
        fitness *= -20
        ind.fitness = fitness


fitness_value_ack(population)


def average_fitness(pop):

    total_fitness = 0
    # av_fitness = []

    for i in range(0, P):
        ind = pop[i]
        total_fitness += ind.fitness        # Find the total fitness of a population

    av = total_fitness / P               # Calculate the average fitness (for plotting)
    # av_fitness.append(av)

    # return av_fitness
    return av


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


def crossover_one_point(pop):
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


def crossover_multi_point(pop):
    offs = []

    for i in range(0, P, 2):
        temp1 = []
        temp2 = []

        parent1 = copy.deepcopy(pop[i])        # Get every 2 individuals
        parent2 = copy.deepcopy(pop[i+1])

        r1 = random.randint(1, 5)       # Choose random points to swap
        r2 = random.randint(5, 8)

        for n in range(r1, r2):
            temp1.append(parent1.gene[n])        # Get the values in range (sw.p.1 - sw.p.2)
            temp2.append(parent2.gene[n])

        t = 0
        for n in range(r1, r2):
            parent1.gene[n] = copy.deepcopy(temp2[t])     # Swap the values
            parent2.gene[n] = copy.deepcopy(temp1[t])
            t += 1

        offs1 = copy.deepcopy(parent1)
        offs2 = copy.deepcopy(parent2)
        offs.append(offs1)
        offs.append(offs2)

    return offs


def crossover_arithmetic(pop):
    # a = 0.6
    a = 0.6
    offs = []

    for i in range(0, P, 2):
        parent1 = copy.deepcopy(pop[i])   # Get every 2 individuals as parents
        parent2 = copy.deepcopy(pop[i+1])

        ind1 = Individual()
        ind2 = Individual()

        for n in range(0, N):
            temp1 = a * parent1.gene[n]
            tail = a - 1                   # Calculate Child1 = a.x + (1-a).y
            tail *= parent2.gene[n]
            temp1 += tail

            temp2 = a * parent2.gene[n]
            tail2 = a - 1                  # Calculate Child 2 = a.y + (1-a).x
            tail2 *= parent1.gene[n]
            temp2 += tail2

            ind1.gene[n] = temp1
            ind2.gene[n] = temp2

            offs.append(ind1)
            offs.append(ind2)

    return offs


def mutation_rand_resetting(pop):
    mut_rate = 0.075
    mut_step = 6.0

    """mut_rate = 0.03
    mut_step = 6"""

    mutated = []

    for i in range(0, P):
        new_ind = Individual()
        new_ind.gene = []
        for j in range(0, N):
            gene = pop[i].gene[j]
            mut_prob = random.random()
            if mut_prob < mut_rate:       # Mutation function
                alter = random.uniform(0, mut_step)
                if gene < 100:
                    gene += alter
                    if gene > 100:
                        gene = 100
                else:
                    gene -= alter
                    if gene < -100:
                        gene = -100

            new_ind.gene.append(gene)
        mutated.append(new_ind)

    return mutated


def mutation_gaussian(pop):
    mut_rate = 0.0335
    mut_step = 1.0
    mutated = []

    for i in range(0, P):
        new_ind = Individual()
        new_ind.gene = []
        for j in range(0, N):
            gene = pop[i].gene[j]
            mut_prob = random.random()
            if mut_prob < mut_rate:  # Mutation function
                alter = random.gauss(0, mut_step)
                gene *= alter

                if gene > 100:
                    gene = 100
                elif gene < -100:
                    gene = -100

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


def main():
    global population
    global worst_individuals     # For plotting
    global average              # For plotting

    index_small = worst_ind(population)
    smallest = copy.deepcopy(population[index_small])  # Get the smallest individual of each population
    worst_individuals.append(smallest.fitness)

    av = average_fitness(population)              # Get the average fitness of each population
    average.append(av)

    # offspring = selection(population)
    offspring = selection(population)

    recombined = crossover_one_point(offspring)

    new_generation = mutation_rand_resetting(recombined)
    fitness_value_ack(new_generation)          # Evaluate each new generation

    index = best_ind(new_generation)    # Find the biggest individual in the new generation
    if smallest.fitness < new_generation[index].fitness:
        new_generation[index] = copy.deepcopy(smallest)    # Replace it with the smallest individual of the original pop

    population = copy.deepcopy(new_generation)


for m in range(0, 500):
    main()

print(worst_individuals)
print(" ")
# print(average)

str_floats1 = [str(fl) for fl in average]

str1 = ", ".join(str_floats1)
file = open("avr", "a")       # for average fitness plotting
file.write(str1 + '\n')
file.close()

str_floats2 = [str(fl) for fl in worst_individuals]

str2 = ", ".join(str_floats2)
file2 = open("graph", "a")      # for worst ind plotting
file2.write(str2 + '\n')
file2.close()

plt.plot(average, label="Mean")
# plt.draw()
plt.plot(worst_individuals, label="Best")
plt.legend(loc="best")
plt.xlabel("Individuals of population")
# plt.ylabel("Average fitness value of population")
plt.ylabel("The best individual in population")
plt.title("GA Original")
plt.show()

# random = random.norma instead of uniform
