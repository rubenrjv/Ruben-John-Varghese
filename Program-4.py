def count_multiples(lst):
    counts = {}
    for i in range(1, 10):
        counts[i] = 0
        for num in lst:
            if num % i == 0:
                counts[i] += 1
    return counts

input_list = [1,2,8,9,12,46,76,82,15,20,30]
result = count_multiples(input_list)
print(result)
