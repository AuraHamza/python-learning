import random
chromosome = [1, 3, 5, 0, 6, 4, 2]
def swap_mutation(chromo):
    i, j = random.sample(range(7), 2)
    chromo[i], chromo[j] = chromo[j], chromo[i]
    return chromo

def scramble_mutation(chromo):
    i, j = sorted(random.sample(range(7), 2))
    part = chromo[i:j+1]
    random.shuffle(part)
    chromo[i:j+1] = part
    return chromo

def inversion_mutation(chromo):
    i, j = sorted(random.sample(range(7), 2))
    chromo[i:j+1] = chromo[i:j+1][::-1]
    return chromo

print("Swap Mutation:", swap_mutation(chromosome.copy()))
print("Scramble Mutation:", scramble_mutation(chromosome.copy()))
print("Inversion Mutation:", inversion_mutation(chromosome.copy()))