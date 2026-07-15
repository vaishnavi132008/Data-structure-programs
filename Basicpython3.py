from itertools import combinations

list = [1, -2, 3, 4, -7]

print("Positive Combinations")

for r in range(len(list) + 1):
    for combo in combinations(list, r):
        if all(num > 0 for num in combo):
            print(combo)
