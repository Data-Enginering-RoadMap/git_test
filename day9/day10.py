item = 'a b c d e f a a a a b b b b n d'.split(' ')


# return unique items 

result = []

for i in item:
    if i not in result:
        result.append(i)

print(result)


result_dict = {}

for i in item:
    if i not in result_dict:
        result_dict[i] = i

print(result_dict.keys())

result_set = set(item)
print(result_set)
