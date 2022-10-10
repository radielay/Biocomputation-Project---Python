import math
import random

# f(x) = 10n + sigma(x^2) - 10 x cos(2pi * x)
# n = 10, 20      -5.12 < x < 5.12

n = 10
gene = []
sigma = 0

for i in range(0, n):
    x = random.uniform(-5.12, 5.12)  # Create population
    x = "%.1f" % x
    x = float(x)
    gene.append(x)
print(gene)

for i in range(0, n):
    x = gene[i]
    power = x * x
    multi = 2 * math.pi * x
    cosine = math.cos(multi)     # in radians
    cosine *= 10
    total = power - cosine
    sigma += total

sigma += 10*n



