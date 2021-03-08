is_or_is_not_prime = []

def is_prime(n):
    i=2
    while i < n:
        end = i//2
        j=2
        while j <= end:
            if i % j == 0:
                break
            j+=1
        else:
            is_or_is_not_prime.append(i)
        i+=1

is_prime(8)
print(is_or_is_not_prime)

is_or_is_not_prime_2 = []

def is_prime_2(n):
    for i in range(2,n):
        end=i//2
        for j in range(2, end+1):
            if i%j == 0:
                break
        else:
            is_or_is_not_prime_2.append(i)

print(is_prime_2(8))
print(is_or_is_not_prime_2)