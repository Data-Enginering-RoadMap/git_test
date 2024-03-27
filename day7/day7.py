#8
# 0 1 1 2 3 5 8 13 21 
# 0 1 2 3 4 5 6  7 8  

# curr + prev = next

def fib(number: int)->int:
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fib(number-1) + fib(number-2)
    
# print(fib(4))


# decorators


def calc1():# high order function
    def addition(num1, num2):
        print(f'i am executing this addition function ')
        return num1 + num2
    return addition


def addition(func):
    def func(num1, num2):
        print(f'i am executing this addition function {func.__name__} ')
        return num1 + num2
    return func

def subtraction(func):
    def func(num1, num2):
        print(f'i am executing this addition function {func.__name__} ')
        return num1 - num2
    return func

# print(calc1()(1, 2)) # calc1() ===> addition(1, 2)

@addition
def calculator(num1, num2):

    print(num1, num2)
    print(f'{func.__name__} is working')


@subtraction
def calculator1(num1, num2):
    print(f'{func.__name__} is working')
    print(num1, num2)


# print(calculator(1,2))
# print(calculator1(1,2))


#oop
# Abstraction, Inheritance, Polymorphism and Encapsulation

class Animal: #Object
   # attributes
    legs = True
    mouth = True
    eyes = True
   # methods
    def move(self):
        return True

dog = Animal()# instantiating a class
cat = Animal()


print(dog.legs)
print(dog.eyes)
print(dog.move())





