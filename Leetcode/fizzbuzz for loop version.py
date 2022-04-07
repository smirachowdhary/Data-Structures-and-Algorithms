def fizzBuzz(n):
    if n < 1  or n > 10**4:
            raise Exception("Invalid Value")
    
    fizzbuzz = []
    
    for i in range(1,n+1):
        if (i)%15 == 0:
            fizzbuzz.append("FizzBuzz")
        elif (i)%5 == 0:
            fizzbuzz.append("Buzz")
        elif (i)%3 == 0:
            fizzbuzz.append("Fizz")
        else:
            fizzbuzz.append(f"{i}")
        
    return fizzbuzz
    
    #Space complexity = O(n)
    #Time complexity = O(n)

testcase = fizzBuzz(150)
print(testcase)
# testcase2 = fizzBuzz(0)
# print(testcase2)
# testcase3 = fizzBuzz(10**4+10)
# print(testcase3)