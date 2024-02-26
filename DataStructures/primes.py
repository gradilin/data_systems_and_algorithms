def print_primes():
    for i in range(2, 10000):  # Start from 2, since 1 is not a prime number
        total = i
        prime = True
        for x in range(2, int(total**0.5) + 1):  # Check for factors up to the square root of total
            if total % x == 0:
                prime = False
                break
        if prime:
            print(total)

print_primes()
