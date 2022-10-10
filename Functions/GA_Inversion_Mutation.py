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
print(" ")


def inversion(temp):
    inverse = []

    index = len(temp) - 1
    while index >= 0:
        inverse.append(temp[index])
        index -= 1
    print("Inverse: ", inverse)

    return inverse


def mutation_inversion(pop):
    mut_rate = 0.5
    mutated = []
    new_ind = Individual()

    for i in range(0, P):
        temp = []
        mut_prob = random.random()
        if mut_prob < mut_rate:  # Mutation function
            swap1 = random.randint(1, int(N / 2) - 1)
            swap2 = random.randint(int(N / 2) + 1, N - 2)

            for n in range(swap1, swap2 + 1):
                temp.append(pop[i].gene[n])
            print("temp: ", temp)

            inv = copy.deepcopy(inversion(temp))

            num = 0
            for n in range(swap1, swap2 + 1):
                pop[i].gene[n] = inv[num]
                num += 1
            new_ind.gene = pop[i].gene
            mutated.append(new_ind)
        else:
            mutated.append(pop[i])

    return mutated


offspring = mutation_inversion(population)

print(" ")
for obj in offspring:
    print(obj.gene)
