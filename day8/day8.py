import time



#without Parameters
def timer(the_function):

    def inner(): 
        print(f' the function started at 12:00')
        ans = f'{the_function()} inside inner'
        print(ans)
        print(f' the function ended at 1pm')
        
    return inner

@timer  #timer(calculation2)
def calculation():
    some_cal = [x for x in range(10000)]
    for i in some_cal:
        ...
    return 'Executed Func'

# def calculation2():
#     some_cal = [x for x in range(10000)]
#     for i in some_cal:
#         ...
#     print('Executed Func')


# timer(calculation2)
    
calculation() #timer(calculation)



#with Parameters
def upper_validation(func):
    def inner(string):
        result = func(string) # sting_parser('sam')
        print(result.upper())
    return inner


@upper_validation
def string_parser(val):
    return val

# sam ---> SAM

# string_parser('sam')