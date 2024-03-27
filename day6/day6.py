# recursive functions
# Generators
# Decorators
from sys import getsizeof

# Recursive functions
# sum of n numbers stop under a condition



container_sum_loop = container_sum_while = 0
# container_sum_loop = 0
# container_sum_while = 0


# for i in n: 
#     container_sum_loop += i

# lenght_arr = len(n)
# while lenght_arr: # 0 false
#     container_sum_while += n[lenght_arr - 1]
#     lenght_arr -= 1

def recursive_sum(n, state= 0, recursive_sum_val = 0):
    # check = state or len(n)
    indx = state
    print(f'{indx} before')

    container_recursive = recursive_sum_val # 0
   
    if indx == 0:
        container_recursive += n[indx] # 0
    else:
        container_recursive += n[indx] # 0

    indx += 1
    print(f'{indx} after')
    if indx < len(n) :
        return recursive_sum (n, indx, container_recursive)
    else:
        return container_recursive


def quicksort(n):
    if len(n) <= 1:
        return n
    pivot = min(n)
    left = [x for x in n if x < pivot]
    right = [x for x in n if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

# first call
#index o  
# call, index 1
# call, index 2
# call, index 3

# print(n)
# print(container_sum_loop)
# print(container_sum_while)
# print(recursive_sum(n))
arr = [3, 6, 8, 10, 1,10000000, 2, 1]
# print(quicksort(arr))
# gen = (x for x in range(1, 1000000000))
n = [x for x in range(1, 1000000)]

print(getsizeof(n))
# print(getsizeof(gen))

def gen_functin(n):
    for i in n:
        yield i


gen = gen_functin(n)
print(getsizeof(gen))
print(gen)
print(next(gen))

