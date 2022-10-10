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


def mutation_swap(pop):
    mut_rate = 0.3
    mutated = []

    for i in range(0, P):
        mut_prob = random.random()
        if mut_prob < mut_rate:  # Mutation function
            swap1 = random.randint(0, int(N/2))
            swap2 = random.randint(int(N/2)-1, N-1)
            print("Swap: ", swap1+1, swap2+1)

            temp = copy.deepcopy(pop[i].gene[swap1])
            pop[i].gene[swap1] = copy.deepcopy(pop[i].gene[swap2])
            pop[i].gene[swap2] = copy.deepcopy(temp)

        new_ind = Individual()
        new_ind.gene = pop[i].gene
        mutated.append(new_ind)

    return mutated


offspring = mutation_swap(population)

print(" ")
for obj in offspring:
    print(obj.gene)
