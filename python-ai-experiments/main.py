import numpy as np
import matplotlib.pyplot as plt
from random import randint, choice

def factorizer(x):
    """Function to find factors of a number."""
    return [factor for factor in range(1, x + 1) if x % factor == 0]

def phenotype(factor):
    """Function to generate offspring based on a factor."""
    while True:
        offspring = randint(100, 999)
        if offspring % factor == 0:
            return offspring

def reproduce(rFactor, currentGen):
    """Function to create the next generation."""
    nextGen = dict()
    count = 0
    for s in currentGen.values():
        for _ in range(choice(rFactor)):
            x = choice(s)
            structure = phenotype(x)
            nextGen[structure] = factorizer(structure)
            count += 1
            if count >= 50:
                break
        if count >= 50:
            break
    return nextGen

def eliminate(factor, currentGen):
    """Function to eliminate structures not divisible by a factor."""
    eGen = {s: factors for s, factors in currentGen.items() if factor in factors}
    return eGen

def factorCount(factor, num_list):
    """Function to count elements divisible by a factor."""
    return sum(1 for element in num_list if element % factor == 0)

# Store data for plotting
gen_data = []
factor_count_data = []
population_size_data = []

currentGen = {randint(100, 999): factorizer(randint(100, 999)) for _ in range(100)}

# Initial data points
gen_data.append(0)
factor_count_data.append(factorCount(5, list(currentGen.keys())))
population_size_data.append(len(currentGen))

for gen in range(1, 1001, 1):
    currentGen = eliminate(10, currentGen)
    currentGen = reproduce([1, 2, 3, 4], currentGen)
    gen_data.append(gen)
    factor_count_data.append(factorCount(10, list(currentGen.keys())))
    population_size_data.append(len(currentGen))

# Convert lists to NumPy arrays
gen_array = np.array(gen_data)
factor_count_array = np.array(factor_count_data)
population_size_array = np.array(population_size_data)

# Plotting the graph
plt.figure(figsize=(8, 6))
plt.plot(gen_array, factor_count_array, marker='o', label='Factor Count for 10')
plt.plot(gen_array, population_size_array, marker='o', color='yellow', label='Population Size')
plt.title('Generation vs Factor Count and Population Size')
plt.xlabel('Generation')
plt.grid(True)
plt.legend()
plt.show()