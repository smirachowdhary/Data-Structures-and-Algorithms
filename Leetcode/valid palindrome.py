def isPalindrome(s: str) -> bool:
    if 1 > len(s) or len(s)> 2 * (10 ** 5):
        return f"Sorry, your array doesn't make the requierments."

    j=len(s)-1
    i=0
    while i<len(s)-1:
        if s[j].isalnum() == True and s[i].isalnum() == True:
            print(i)
            print(j)
            if s[i].lower() != s[j].lower():
                return False
        elif s[j].isalnum() == True and s[i].isalnum() == False:
            i+=1
            print(i)
            print(j)
            continue
        elif s[j].isalnum() == False and s[i].isalnum() == True:
            j-=1
            continue
        else:
            j-=1
            i+=1
            continue
        j-=1
        i+=1

    return True

print(isPalindrome("a."))
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome(".a"))
print(isPalindrome(" "))
print(isPalindrome("race a car"))
print(isPalindrome("0P"))
print(isPalindrome("!!!"))
print(isPalindrome("Marge, let's \"[went].\" I await {news} telegram."))
print(isPalindrome(",,,,,,,,,,,,acva"))