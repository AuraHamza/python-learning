import random
chromosomes = ['C1', 'C2', 'C3', 'C4', 'C5']
fitnesses = [12, 20, 15, 8, 25]

def roulette_wheel_selection():
    return random.choices(chromosomes, weights=fitnesses, k=1)[0]

def tournament_selection():
    selected = random.sample(list(zip(chromosomes, fitnesses)), 3)
    return max(selected, key=lambda x: x[1])[0]

def rank_selection():
    ranked = sorted(zip(chromosomes, fitnesses), key=lambda x: x[1])
    names = [x[0] for x in ranked]
    return random.choices(names, weights=[1, 2, 3, 4, 5], k=1)[0]

for i in range(5):
    print("Run", i + 1)
    print("Roulette:", roulette_wheel_selection())
    print("Tournament:", tournament_selection())
    print("Rank:", rank_selection())
    print()