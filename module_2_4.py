numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    if numbers[i] >= 2:
        is_prime = True
        for k in range(2, numbers[i]):
            if numbers[i] % k == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(numbers[i])
        else:
            not_primes.append(numbers[1])
print(f'Primes: ', primes)
print(f'Non primes: ', not_primes)