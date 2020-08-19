#Calculator using functions
print("Calculator- by defining functions")

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def exp(x,y):
    return x**y
def mod(x,y):
    return x//y
def remainder(x,y):
    return x%y


x= int(input("enter the value of x"))
y= int(input("enter the value of y"))
print('')

print("addition is",x+y)
print("multiplication is",x*y)
print("subtraction is",x-y)
print("remainder is",x%y)
print("modulus is",x//y)
print("exponential is",x**y)
print("division ",x/y)
