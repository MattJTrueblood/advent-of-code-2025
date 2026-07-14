import os
import math
from itertools import combinations

def parseCoords(lines):
    coords = []
    for line in lines:
        if len(line) > 0:
            coords.append(tuple(map(int, line.split(','))))
    return coords

def getEuclidDistance(coord_a, coord_b):
    return math.sqrt(((coord_a[0] -coord_b[0]) * (coord_a[0] -coord_b[0])) +
                                              ((coord_a[1] -coord_b[1]) * (coord_a[1] -coord_b[1])) +
                                              ((coord_a[2] -coord_b[2]) * (coord_a[2] -coord_b[2])))

def generateShortestDistances(coords, n):
    all_distances = []
    all_pairs = list(combinations(coords, 2))
    for p in all_pairs:
        all_distances.append([p, getEuclidDistance(p[0], p[1])])
    sorted_distances = sorted(all_distances, key=lambda k: k[1])
    return sorted_distances[:n]

def generateCircuits(shortest_distances):
    """connect all the pairs in the list"""
    circuits = dict()
    circuit_num_idx = 0
    for n in shortest_distances:
        p = n[0]
        if p[0] not in circuits and p[1] not in circuits:
            circuits[p[0]] = circuit_num_idx
            circuits[p[1]] = circuit_num_idx
            circuit_num_idx += 1
        elif p[0] in circuits and p[1] not in circuits:
            circuits[p[1]] = circuits[p[0]]
        elif p[0] not in circuits and p[1] in circuits:
            circuits[p[0]] = circuits[p[1]]
        elif p[0] in circuits and p[1] in circuits and circuits[p[0]] != circuits[p[1]]:
            shared_circuit_idx = circuits[p[0]]
            circuit_idx_to_replace = circuits[p[1]]
            for k, v in circuits.items():
                if v == circuit_idx_to_replace:
                    circuits[k] = shared_circuit_idx
        # else they're already on the same circuit, so nothing happens
    
    # find the circuits' sizes and sort them by size largest to smallest
    circuit_sizes = dict()
    for k, v in circuits.items():
        if v in circuit_sizes:
            circuit_sizes[v] = circuit_sizes[v] + 1
        else:
            circuit_sizes[v] = 1
    circuit_sizes_sorted = sorted(circuit_sizes.values(), reverse=True)

    return circuit_sizes_sorted

solution = 0
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as f:
    allLines = f.read().split('\n')
    coords = parseCoords(allLines)
    shortest_distances = generateShortestDistances(coords, 1000)
    circuit_sizes_sorted = generateCircuits(shortest_distances)
    solution = circuit_sizes_sorted[0] * circuit_sizes_sorted[1] * circuit_sizes_sorted[2]

print(solution)