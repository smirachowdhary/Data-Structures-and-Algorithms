def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    if len(s) < 1 or len(s) > 10**5:
            return f"Sorry, your array doesn't make the requierments."
        
    x = len(s)//2
    
    i=0
    while i < x:
        n = s[i]
        s[i] = s[-1-i]
        s[-1-i] = n
        i+=1
    
    return s

testcase = reverseString(["h","e","l","l","o"])
print(testcase)