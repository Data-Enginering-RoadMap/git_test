import re

file_path = 'Ingestion/data/ipLogTable.txt'
with open(file_path) as f:
    data = f.read()

pattern =r'\d{3}\.\d{2}\.\d{3}\.\d{2}\:\d*'

# matches = re.findall(pattern, data)
# re.search(pattern, data)
# print(re.search(pattern, data))


emails = """ade.ademola@gmail.com
            john.doe@test.com
            jane.doe@test.org
            jane.doe@test.io
            jane.doe@test.cu
"""

pattern2 = '(\w*)\.(\w*)@(\w*)\.(com|org)'
read = re.findall(pattern2, emails)

list_firstname =[]
list_lastname = []
list_domain = []

for i in read:
        # i[0],i[1], i[2]
    first, last, *domain = i
    list_firstname.append(first)
    list_lastname.append(last)
    list_domain.append(domain)


print(list_firstname)
print(list_lastname )
print(list_domain )


