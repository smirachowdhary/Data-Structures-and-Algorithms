def value(r):
    if r == 'I':
        return 1
    if r == 'V':
        return 5
    if r == 'X':
        return 10
    if r == 'L':
        return 50
    if r == 'C':
        return 100
    if r == 'D':
        return 500
    if r == 'M':
        return 1000
    else:
        return False
 
def romanToDecimal(number):
    answer = 0
    i=0

    while i<len(number):
        one = number[i]

        if i+1 != len(number):
            two = number[i+1]
        else:
            answer+=int(value(one))
            i+=1
            continue

        
        condition2 = value(two) == 5 or value(two) == 10
        if value(one) == 1 and condition2 == True:
            to_add = value(two) - value(one)
            answer+=int(to_add)
            break
        
        condition2 = value(two) == 50 or value(two) == 100
        if value(one) == 10 and condition2 == True:
            to_add = value(two) - value(one)
            answer+=int(to_add)
            i+=2
            continue
        
        condition2 = value(two) == 500 or value(two) == 1000
        if value(one) == 100 and condition2 == True:
            to_add = value(two) - value(one)
            answer+=int(to_add)
            i+=2
            continue
        else:
            answer = 'is not a Numeral. Sorry.'

        to_add = value(one)
        answer+=int(to_add)
        i+=1

    return answer
    
Test_case_userinput=romanToDecimal(input("Enter a roman numeral here:"))
print(f"Integer form of Roman Numeral is {Test_case_userinput}.")
Test_case_digits_increase=romanToDecimal(input('MCDLXVII'))
print(f"Integer form of Roman Numeral is {Test_case_digits_increase}.")
Test_case_digits_decrease=romanToDecimal(input("VIIIDXLII"))
print(f"Integer form of Roman Numeral is {Test_case_digits_decrease}.")
Test_case_all_values=romanToDecimal(input("MCDXLVI"))
print(f"Integer form of Roman Numeral is {Test_case_all_values}.")
Test_case_false=romanToDecimal(input("fgmd"))
print(f"Integer form of Roman Numeral is {Test_case_false}.")