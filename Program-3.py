def generate_conditional_odd_series(n: int):
    length = n if n % 2 != 0 else n - 1
    series = []
    for i in range(length):
        series.append(2 * i + 1)
    return series

user_input = int(input("Enter the number (a): "))

result = generate_conditional_odd_series(user_input)

print("Output:", ", ".join(map(str, result)))
