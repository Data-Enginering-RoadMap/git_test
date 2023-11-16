# conditional
# ternary operator


# if condition true:
    #execute this code
# else:
    #execute this code



# store ={'vip': [1,2,3,4], 'regular': [6,7,8,9]}
# # 4 cheque bounced 3 times
# # 3 has  discount of 10%
# result1 = f' Alert you balance is now {1000 * 0.9}' 
# result2 = 'bounced cheque'

# bank_balnce = 1000
# 1 == 4 #false
# if store['vip'][0] == 4:
#     if bank_balnce > 1000:
#         print(result2 )


# elif store['vip'][1] == 3:
#     print(result1 )
# elif store['vip'][2] == 3:
#     print(result1 )
# else:
#     print('welcome!!')




# if store['vip'][2] == 3:
#     print(result2  )
# else :
#     print(result1)

# final_output = result2 if store['vip'][2] == 3 else result1
# print(final_output)

# if true result if condition else false result



# print(1 == 1)
# print(1 != 2)
# print(0 < 1)
# print(6 > 5)

# ' a for apple '+' '+ ' B for Ball'


# a = ' a for apple '
# b = ' B for Ball'

# print('%s %s' % (a, b))
# print('{1} {0}'.format(a, b))
# print(f'sampeke {b}')
# print(a, b)
# m = f'{a}-{b: >10}'
# print(m)

# loops
# for loop
# while loop # problem infinity loop
# regular = store['regular']  #[6,7,8,9]
# # musa = regular[0]
# # sam = regular[1]
# # isaac = regular[3]

# *musa, sam, isaac, all_other, last = regular
# print(musa, sam, isaac, all_other)

# for value in store:
#     print(value)

store = {
            'vip': [('name',1),('name',4),('name',9)], 
            'regular': [6,7,8,9,1,2,3,4,5,5,6]
         }

# for name, id in [('name',1),('name',4),('name',2)]:
#     print(id)
#     break


# for key, value in store.items():
#     # print(f'{key} ===> {value}')
#     print(f'{key} ===>{value}')
#     # print(dir(store))
#     print('     ------- ')
 
print(store.items())  # [('vip', [('name', 1), ('name', 4), ('name', 2)]), ('regular', [6, 7, 8, 9, 1, 2, 3, 4, 5, 5, 6])]

for customer_type, value in store.items():
    print(customer_type )
    if customer_type == 'regular': #true vip == 'regular
        print('yes regular customer')
        if 9 in value: #[6, 7, 8, 9, 1, 2, 3, 4, 5, 5, 6]
            print('yes')
            print(value[3])
            for item in value:
                if item == 9:
                    print(item)
    else:
        print('not regular')
    print(value)

    

# for value in store:

