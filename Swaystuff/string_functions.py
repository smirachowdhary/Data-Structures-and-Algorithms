from ast import Return


def capitalize_function(a):
    x = a.capitalize()
    return x

msg = "capitalize function!"
print(capitalize_function(msg))

def title_function(a):
    x = a.title()
    return x

msg2 = "title function!"
print(title_function(msg2))

def lOWER_fUNCTION(a):
    x = a.lower()
    return x

msg3 = "lOWER fUNCTION!"
print(lOWER_fUNCTION(msg3))

def Upper_funCTion(a):
    x = a.upper()
    return x

msg4 = "UppeR funCTion!"
print(Upper_funCTion(msg4))

def Ends_with_function(a):
    x = a.endswith("!")
    return x

msg5 = "Ends with function!"
print(Ends_with_function(msg5))