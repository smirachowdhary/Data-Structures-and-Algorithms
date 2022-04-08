def isPalindrome(s: str) -> bool:
    if 1 > len(s) or len(s)> 2 * (10 ** 5):
        return f"Sorry, your array doesn't make the requierments."

    # reverse_original_code = s
    # halfOfLength = len(s)//2
    # i=0
    # while i < halfOfLength:
    #     ch_start = s[i]
    #     ch_end = s[len(s)-1-i]
    #     reverse_original_code = s.replace(str(i),ch_end)
    #     reverse_original_code = s.replace(ch_end,ch_start)
    #     i+=1
        
    # # reverse_original_code = reverse_original_code.lower()
    # # s = s.lower()
        
    # if s == reverse_original_code:
    #     return True
    # if s != reverse_original_code:
    #     return False

    halfOfLength = len(s)//2
    i=0
    for i in range(halfOfLength):
        if s[i].lower() != s[-1-i].lower():
            return False

    return True

print(isPalindrome("aba"))
print(isPalindrome("abca"))
print(isPalindrome("abA"))
print(isPalindrome("abA."))
# print(isPalindrome("000Assa000"))
# print(isPalindrome("000Assa001"))