def count_occurrences():
    lst = [1, 2, 2, 3, 3, 3]
    occurrences = {}
    for num in lst:
        occurrences[num] = occurrences.get(num, 0) + 1
    return occurrences

print(count_occurrences())  # Output: {1: 1, 2: 2, 3: 3}