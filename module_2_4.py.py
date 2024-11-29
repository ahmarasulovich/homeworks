def is_prime(value):
    if value <= 1:
        return False
    for i in range(2, int(value ** 0.5) + 1):
        if value % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for i in numbers:
    if is_prime(i):
        primes.append(i)
    else:
        not_primes.append(i)

print("Простые числа:", primes)
print("Непростые числа:", not_primes)
