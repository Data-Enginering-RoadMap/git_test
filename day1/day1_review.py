# b ='Coding'
# c ='For'
# d= 'All'

# #first method
# print(b + ' ' + c + ' ' + d)
# sentent = b + ' ' + c + ' ' + d

# #string formating
# #first method
# first_method = '%s %s %s'%(c,b,d)
# print(first_method)

# #Second method
# second_method = '{2} {1} {0} {1}'.format(d, c,b)
# print(second_method)

# #third method
# third_method = f'{1.00000:.d} {c} {d}'
# print(third_method)


#multiline string

#1
print('sample\nanother\n')
print('sample\tanother\t')
print('sample', 'another')
print('sample', 'another', end='\n', sep='\n')

file = open('sample1.txt', 'wb')
# print('sample', 'another', end='\n', sep='\n',file= file)

multiline= '''
the boy the bla bla
            bla bla
bla
'''
# print(multiline)

# iterables, list, tuples
# iteration 

#index, loop through
#strings
#list
#tuples
#dict
#sets
example = {'jey':'value', 'key2':'value'}
# for i in {'jey':'value', 'key2':'value'}:
#     print(i)

# print(example['jey'])

list_item = [1,2,4,5, 'anything']
tuple_item = (1,1,1,5, 'anything')
#3customers priority
#10 regular
## 5regular 1 priority 5 regular, 2priority

ola_customer_list = {
    'priority': [('p1','address'), 'p2', 'p3'],
    'Regular': ['R1', '....']
}

# list_item[4]= 6 # i can reassign
list_item1= [('p1','address'), ('p2', 'addre2'), ('p3', 'ssss'), ('p1','address')]
list_item2= [['p1','address'], ('p2', 'addre2'), ('p3', 'ssss')]
list_item2[0][1]= 'sample'
# print(list_item2)
# list_item1[0][1]= 'sample'
print(list_item1)
# list_item1[0] = ('p1','addressmmmm')
print(list_item1)
# tuple_item[4]=6
# print(tuple_item)
list_itemunique= [{('p1','address'), ('p2', 'addre2'), ('p3', 'ssss'), ('p1','address')}]
print(list_itemunique)
print('abc'[1])


#join
list1 = ['name', 'sample']

print('- '.join(list1))
print('-'.join('BOY'))
print('-'.join({'key': 1, 'sample':2}))
print('-'.join({'sample', 'another'}))
print('-'.join(('sample', 'another')))

print(' sample')
print(' sample'.strip())

# class car: #object
#     tyre = 4#attribute

#     def honk_honr(self):#method
#         ...

# class str: #object
#     def join(self)#