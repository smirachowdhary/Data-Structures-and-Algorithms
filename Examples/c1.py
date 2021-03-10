class My_Number:
    def __init__(self,num):
        self.num = num
    
    def is_prime(self):
        for i in range(2,self.num):
            if(self.num % i == 0):
                return False
        return True

    def is_even(self):
        return self.num % 2 == 0

class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'''
        Hello My name is {self.name}!!
        I am {self.age} years old
        How are you?
        ''')

    def GetIntroduction(self):
        return f'''
        Hello My name is {self.name}!!
        I am {self.age} years old
        How are you?
        '''


