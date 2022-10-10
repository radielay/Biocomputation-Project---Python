import random
import matplotlib.pyplot as plt

N = 10
P = 10

fitness_list = []  # All 3 used for plotting
fittest_list = []
average = []


class Individual(object):
    def __init__(self):
        self.gene = [0] * N
        self.fitness = 0


def initialise_pop():

    pop = []
    for i in range(0, P):
        temp = []
        fitness = 0
        for x in range(0, N):
            r = random.randint(0, 1)
            temp.append(r)  # Create binary strings chromosomes
            if r == 1:
                fitness += 1      # Give fitness value

        ind = Individual()
        ind.gene = temp.copy()
        ind.fitness = fitness
        pop.append(ind)   # Create a population
    return pop


population = initialise_pop()    # Initial population

print("Initial population")
for obj in population:
    print(obj.gene, obj.fitness)


def plot_value(pop):
    total_fitness = 0
    fittest = 0

    for i in range(0, len(pop)-1):
        ind = pop[i]                      # Get total fitness of the population
        total_fitness += ind.fitness

        if ind.fitness > fittest:           # Get the fittest individual
            fittest = ind.fitness

    av = total_fitness / len(pop)        # Get the average fitness of the population
    average.append(av)
    fitness_list.append(total_fitness)
    fittest_list.append(fittest)

    print("____________________________________________")
    print("Total fitness of the population: ", total_fitness)
    print(" ")
    print("The average fitness of the population: ", av)
    print(" ")
    print("Fittest individual: ", fittest)
    print("____________________________________________")


plot_value(population)     # Initial population values


def selection(pop):
    offs = []

    for n in range(0, len(pop)):
        p1 = random.randint(0, len(pop)-1)
        off1 = pop[p1]

        p2 = random.randint(0, len(pop)-1)
        off2 = pop[p2]

        if off1.fitness > off2.fitness:
            offs.append(off1)  # Selecting the better individuals from the tournament
        else:
            offs.append(off2)

        print(" ")
        print("Selected individuals for tournament: ")
        print(n, off1.gene, off1.fitness)  # Print competing individuals
        print(n+1, off2.gene, off2.fitness)
    print(" ")
    print("Selected parents: ")  # Print the chosen individuals (temporary offsprings)
    for ind in offs:
        print(ind.gene, " Fitness: ", ind.fitness)
        print("____________________________________________")

    return offs

# offspring = selection()


def crossover(pop):
    offs = []

    p = 0
    while p < len(pop):

        parent1 = pop[p]
        p += 1

        parent2 = pop[p]
        p += 1

        n = random.randint(0, N - 1)  # n is the point where cross over will occur
        i = 0
        child1 = []
        child2 = []
        while i < n:
            child1.append(parent1.gene[i])  # Up until n, the child receives the same genes as its parent
            child2.append(parent2.gene[i])
            i += 1

        child1.append(parent2.gene[n])  # The gene under n position is the first gene on each tail (to be swapped)
        child2.append(parent1.gene[n])

        i = n
        while i < N - 1:
            i += 1
            child2.append(parent1.gene[i])  # Tails being swapped (from parent1 to child2 and etc.)
            child1.append(parent2.gene[i])

        ind = Individual()
        ind.gene = child2        # Populate new generation
        ind.fitness = 0
        offs.append(ind)

        ind2 = Individual()
        ind2.gene = child1
        ind.fitness = 0
        offs.append(ind2)

        print(" ")
        print("Individuals to crossover: ")
        print(" ")
        print(parent1.gene, parent1.fitness)
        print(parent2.gene, parent2.fitness)
        print("Crossing point = ", n + 1)
        print("____________________________________________")
        print(" ")
        print("After crossover: ")
        print(" ")
        print(child1)
        print(child2)
        print("____________________________________________")

    return offs

# recombined = crossover()


def mutation(pop):
    mut_rate = 0.04
    new_pop = []

    print("")
    print("Mutation: ")
    print(" ")
    for p in range(0, len(pop)):
        ind = pop[p]
        for i in range(0, N):
            mut_prob = random.randint(0, 100)
            if mut_prob < (100 * mut_rate):  # MUTATION
                print("Mutation occurred on gene ", i + 1)
                if ind.gene[i] == 1:
                    ind.gene[i] = 0
                else:
                    ind.gene[i] = 1
                print(ind.gene)

        new_pop.append(ind)

    return new_pop


# new_generation = mutation()


def fitness_value(pop):

    for ind in pop:
        gene = ind.gene
        fitness = 0            # Give fitness value to a chosen population
        for i in range(0, N):
            if gene[i] == 1:
                fitness += 1
        ind.fitness = fitness


def best_solution(pop):

    fittest = 0
    for ind in pop:
        if ind.fitness > fittest:
            fittest = ind.fitness
            # best = ind.gene
            best = ind

    print("")
    print("Best solution: ", best.gene)

    return best


def worst_solution(pop):

    worst_ind = pop[0]
    for ind in pop:
        if worst_ind.fitness > ind.fitness:
            worst_ind.gene = ind.gene
            worst_ind.fitness = ind.fitness

    print("")
    print("Worst solution", worst_ind.gene, worst_ind.fitness)

    return worst_ind


def main():
    global population

    best = best_solution(population)

    offspring = selection(population)

    print(" Offspring ")
    for obj in offspring:
        print(obj.gene)

    worst = worst_solution(offspring)

    offspring.remove(worst)
    offspring.append(best)

    print(" NEW offspring: ")
    for obj in offspring:
        print(obj.gene)

    recombined = crossover(offspring)

    new_generation = mutation(recombined)

    fitness_value(new_generation)
    plot_value(new_generation)

    print("NEW GENERATION")
    for obj in new_generation:
        print(obj.gene, obj.fitness)

    population = new_generation.copy()


for m in range(0, 3):
    main()


plt.plot(average)  # Blue line
plt.plot(fittest_list)  # Orange line
plt.show()
