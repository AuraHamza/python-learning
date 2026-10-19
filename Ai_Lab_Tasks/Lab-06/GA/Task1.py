import random
def fitness(chromosome):
    score = 0
    for i in range(7):
        for j in range(i + 1, 7):
            if abs(chromosome[i] - chromosome[j]) != abs(i - j):
                score += 1
    return score

def selection(population):
    parents = random.sample(population, 3)
    parents.sort(key=fitness, reverse=True)
    return parents[0]

def crossover(p1, p2):
    start, end = sorted(random.sample(range(7), 2))
    child = [-1] * 7
    child[start:end] = p1[start:end]
    remaining = [x for x in p2 if x not in child]
    index = 0
    for i in range(7):
        if child[i] == -1:
            child[i] = remaining[index]
            index += 1
    return child

def mutation(chromosome):
    chromosome = chromosome.copy()
    if random.random() < 0.2:
        i, j = random.sample(range(7), 2)
        chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome

population = [random.sample(range(7), 7) for i in range(20)]
for generation in range(1000):
    population.sort(key=fitness, reverse=True)
    best = population[0]
    if fitness(best) == 28:
        break

    new_population = [best]
    while len(new_population) < 20:
        p1 = selection(population)
        p2 = selection(population)
        child = crossover(p1, p2)
        child = mutation(child)
        new_population.append(child)

    population = new_population
print("Camera Placement:", best)
print("Fitness:", fitness(best))
print("Generation:", generation + 1)
