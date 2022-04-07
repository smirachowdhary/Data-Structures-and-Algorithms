def fizzBuzz(n):
    fizzbuzz = []
    if n < 1  or n > 10**4:
        return f"{n} is greater then or equal to 10,000 or is less than 1."
        
    i=0
    while i < n:
        if (i+1)%15 == 0:
                fizzbuzz.append("FizzBuzz")
        elif (i+1)%5 == 0:
                fizzbuzz.append("Buzz")
        elif (i+1)%3 == 0:
            fizzbuzz.append("Fizz")
        else:
            fizzbuzz.append(f"{i+1}")
        i+=1
    return fizzbuzz
    
    #Space complexity = O(n)
    #Time complexity = O(n)

testcase = fizzBuzz(15)
print(testcase)