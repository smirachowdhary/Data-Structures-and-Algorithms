def titleToNumber(columnTitle):
    if 1 > len(columnTitle) or len(columnTitle) > 7:
        return f"Sorry, your array doesn't make the requierments."
    
    column_number = 0
    for i in range(len(columnTitle)):
        column_value = (ord(columnTitle[len(columnTitle)-1-i])-64)
        column_place = column_value * (26**i)
        column_number = column_number + column_place
    
    return column_number

testcase = titleToNumber("AAA")
print(testcase)