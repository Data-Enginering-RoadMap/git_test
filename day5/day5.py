# Starting a new year with Functions

#definition
def sample_function(a,b,c):
    for i in [1]:
        # continue
        print(f'inside of the loop {a} - {b} - {c}')
        return i

#return value a function without an explicit return keyword is

#call function
# print(sample_function(1,2,4))

def add_number(a, b):
    addition = a + b
    # print(addition)
    return addition

add_number(12, 12)
houston = 12222222
Dallas = 10020202020
population_texas = add_number(houston, Dallas)

# print(population_texas)

# def sample_function(a,b,c):
#     for i in [1]:
#         # continue
#         # break
#         print(f'inside of the loop {a} - {b} - {c}')
#         return i

items = [1,2,3,4,5,6,7,8]
result = []

for item in items:
    if item in [3,6]: #i == 3 or i == 6
        continue
        result.append(item)
    else:
        # print(item)
        result.append(item)


print(result)

def keyword_args(z: int, y: str):
    print(f'a value is {z}')
    print(f'b value is {y}')
    conversion = z * 10
    stringer = f'{y}s'
    return conversion, stringer

z = 10
y= 'book'
new_val = {'y': 'book', 'z': 10}  # y = book z = 10
# print(keyword_args(y, z))
print(keyword_args(**new_val))


# *args **kwargs
# sum the n amount of array(s) and return the last item of the array
array = [1,2,3,4,5,6,7]
# array2 = [2,3,4,5,5]

def sum_array(array):
    result = 0
    last_item = None

    for i in array:
        result += i
        last_item = i
        # result = result + i
    
    return result, last_item

# print(sum_array(array))

def sum_array2(*args): #* is positional ** is keyward
    result = 0
    last_item = None
    # print(args)
    array = []
    for item in args:
        array.extend(item)

    for i in array:
        result += i
        last_item = i
        # result = result + i
    
    return result, last_item
new= [12,10000,938733]


def sum_array3(array, *args): #* is positional ** is keyward
    result = 0
    last_item = None
    # print(args)

    for item in args:
        array.extend(item)

    for i in array:
        result += i
        last_item = i
        # result = result + i
    
    return result, last_item

print(sum_array2(array, new))
print(sum_array3(array, new))

# print(sum_array2(array, new))


# def sum_array4(a,*,b=None):
#     print(b)
# sum_array4(1)
def sum_array4(b, c, /):
    print(b)
sum_array4(1,2)

print()