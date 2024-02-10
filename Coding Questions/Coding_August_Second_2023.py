# 1: Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
# 2: Given two strings needle and haystack, return the index of the occurrence of needle in haystack.
# 3: Given a string s, return true if it is a palindrome, or false otherwise.

def atoi_prompt(string):
    number = 0

    sign='+'    
    for element in string: # starting signs
        if element == "-":
            sign='-'
            break

    i=0
    while i<len(string):
        x=type(i)==int
        if x==True: # checks to see if string(i) is int
            if x==0: # checks to see if string(i) is 0
                j=0
                while j<i: # checks to see if other ints before
                    int_before=False
                    x=type(i)==int
                    if x==True:
                        int_before=True
                        break
                    j+=1
                if int_before == False: # skipping the zero
                    i+=1
                    break
                else:
                    number+=string[i] # adding the number to the answer
        i+=1
    
    almost_done = string[1:] # deletes forward zero

    if sign == '-': # for the signs
        return -almost_done
    else:
        return almost_done
    
def needle_in_a_haystack(needle, haystack):

    # this code takes that needle is just one charcter and that needle is present in haystack and that there is only one needle in haystack

    i=0
    while i<len(haystack):
        if haystack[i] == needle:
            return i
        i+=1

def is_palindrone(string):

    x=len(string)
    if x%2 == 0:
        x=x/2
    else:
        x=x/2-0.5
    
    output = True
    i=0
    while i<=x:
        if string[i] != string[-i-1]:
            output = False
            break
        i+=1
    
    return output
