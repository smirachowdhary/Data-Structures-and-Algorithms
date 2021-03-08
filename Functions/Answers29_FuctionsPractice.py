def is_prime(n):
    end = n//2
    for i in range(2, end+1):
        if n % i == 0:
            return "Number is prime"
    return "Number is composite"

print(is_prime(21))
print(is_prime(23))