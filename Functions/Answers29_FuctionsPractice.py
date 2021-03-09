def is_prime(n):
    for i in range(2,n):
        if(n % i == 0):
            return False
    return True

def get_prime_list(n):
    list_of_primes = []
    for i in range(1,n+1):
        if is_prime(i):
            list_of_primes.append(i)
    return list_of_primes


print(is_prime(23))
print(is_prime(22))
print(get_prime_list(23))