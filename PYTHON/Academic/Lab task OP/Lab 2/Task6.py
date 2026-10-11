def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1

    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b

    return fibonacci_sequence

num_terms = 6

fib_sequence = generate_fibonacci(num_terms)

for term in fib_sequence:
    print(term)
