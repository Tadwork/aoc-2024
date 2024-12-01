import os
from collections import Counter

def read_input_into_lists():
    list_1 = []
    list_2 = []
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        lines = f.read().splitlines()
        for line in lines:
            a, b = line.split()
            list_1.append(int(a))
            list_2.append(int(b))
    return list_1, list_2

def compute_min_distance_between_lists(list_1, list_2):
    dist = 0
    list_1.sort()
    list_2.sort()
    for i,_ in enumerate(list_1):
        dist = dist + abs(list_1[i] - list_2[i])
    return dist

def calc_total_similarity_score(list_1, list_2):
    total = 0
    counts = Counter(list_2)
    for item in list_1:
        total = total + (counts[item] * item)
    return total
    

if __name__ == '__main__':
    list_1, list_2 = read_input_into_lists()
    dist = compute_min_distance_between_lists(list_1, list_2)
    similarity_score = calc_total_similarity_score(list_1, list_2)
    print(dist)
    print(similarity_score)