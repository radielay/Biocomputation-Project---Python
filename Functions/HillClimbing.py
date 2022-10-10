import random

N = 10
graph_list = []


class Solution:

    variable = [0]*N
    utility = 0


def test_function(ind):

    utility = 0
    for n in range(N):
        utility = utility + ind.variable[n]
    return utility


individual = Solution()

for j in range(N):
    individual.variable[j] = random.randint(0, 100)
individual.utility = 0

individual.utility = test_function(individual)
print(individual.utility)

new_ind = Solution()

for x in range(1000):
    for i in range(N):
        new_ind.variable[i] = individual.variable[i]
        change_point = random.randint(0, N - 1)
        new_ind.variable[change_point] = random.randint(0, 100)
        new_ind.utility = test_function(new_ind)

        if individual.utility <= new_ind.utility:
            individual.variable[change_point] = new_ind.variable[change_point]
            individual.utility = new_ind.utility

        graph_list.append(individual.utility)
        print(individual.utility)


