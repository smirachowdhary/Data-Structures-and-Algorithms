def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    if len(s) < 1 or len(s) > 10**5:
        return f"Sorry, your array doesn't make the requierments."
    
    array = []
    
    i=0
    while i < len(s):
        array.append(s[len(s)-1-i])
        i+=1

    s.clear()
    
    i=0
    while i < len(array):
        s.append(array[i])
        i+=1
    
    return s

testcase = reverseString(["h","e","l","l","o"])
print(testcase)