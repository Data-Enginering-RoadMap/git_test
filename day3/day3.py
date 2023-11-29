# while loops 
# while loops are used to repeat a block of code until a condition is met


# true condition
# it a continues loop
# danger!!! lead to infinite loop
counter = 0
stopper = 10

condition = stopper > counter #true
print(condition)



while condition: # while stopper > counter
    print(f"Hello {counter}")
    counter += 1
    if counter == 10:
        condition = False

while stopper > counter: # while stopper > counter
    print(f"Hello {counter}")
    counter += 1


#Ternary Opertors  DRY
value = 10
container = ''

if value == 10:
    container = value * 10 
else:
    container = value 

container = value * 10 if value == 10 else value

## is  == & =
# assignment operator
# comparison operator
# identity operator

# truthsy and falsy values

a = []
b = []
# c = b

print(a is b)
print(a == b)
print(id(a),  id(b))

ans = value == 10

if ans:
    container = value * 10 


container = value


