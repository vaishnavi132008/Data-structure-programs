tup = [(10, 20, 30), (5, 15, 25), (1, 2, 3, 4)]

for t in tup:
    total = sum(t)
    avg = total / len(t)
    print(f"Tuple: {t} -> Sum = {total}, Average = {avg:.2f}")
