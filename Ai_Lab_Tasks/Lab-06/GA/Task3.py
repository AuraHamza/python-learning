import random
parent1 = [1, 3, 5, 0, 6, 4, 2]
parent2 = [2, 5, 1, 6, 0, 3, 4]

def one_point_crossover(p1, p2):
    point = random.randint(1, 6)
    child = p1[:point] + p2[point:]
    return child
def two_point_crossover(p1, p2):
    a, b = sorted(random.sample(range(1, 7), 2))
    child = p1[:a] + p2[a:b] + p1[b:]
    return child
def order_crossover(p1, p2):
    a, b = sorted(random.sample(range(7), 2))
    child = [-1] * 7
    child[a:b+1] = p1[a:b+1]
    remaining = [x for x in p2 if x not in child]
    j = 0

    for i in range(7):
        if child[i] == -1:
            child[i] = remaining[j]
            j += 1
    return child

print("One-Point Crossover:", one_point_crossover(parent1, parent2))
print("Two-Point Crossover:", two_point_crossover(parent1, parent2))
print("Order Crossover:", order_crossover(parent1, parent2))