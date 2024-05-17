
        # bot
# repond to greetings
# identify users
# store input information into a database - file
# read information from the database
# modify a content of a database
# delete a content of a database

# Ola
# Mayowa
# Tunde
# Tolu
# Titi

# customercare="day5/customercare.txt"
# baduser="day5/internalaudit.txt"
# baduser =database()

def hola():
    '''The name of the bot is Hola'''
    #read from database
    # grab users input
    valu_input = input("Enter your name: ")
    users(valu_input)
    #include your statements here to incorporate your delete function
    remove_input=input("would you like to delete your information from the database?Y/N: ")
    if remove_input =='Y':
        print("Its sad to see you leave")
        database('delete', file_path= 'day5/customercare.txt',content=valu_input.capitalize(),remove_input=remove_input)
    else:
        print("Thanks for not leaving")







# def greetings():
#     print("Hello, " + response + "! " + validated_user)

def users(response):

    if response: #truthy falsy

        validated_user = validate(response) # caps version of response
        response = validated_user
        # response = validate(response)
        
        # print("Hello, " + response + "! " + validated_user)
        greetings(response, validated_user)
    else:
        raise Exception("You did not enter a name") ## exceptions
    ...
def greetings(response, validated_user):
    print("Hello, " + response + "! " + validated_user) 


def validate(user_response):
    user_response = user_response.capitalize()
    if user_response in database('read', file_path = 'day5/internalaudit.txt'):#bad_users:
        print(f"You are a bad user.Geroouuutttttt")
        return user_response
    elif user_response not in database('read', file_path = 'day5/customercare.txt'):
        #temp_database.append(user_response)
        database('modify', file_path = 'day5/customercare.txt',content=user_response)
        #print(temp_database)
        #database(user_response)
        return user_response
    else:
        print(f"You are already in the database ") #{database('read', file_path = 'day5/customercare.txt')}
        return user_response

# def database(data_file):
#     data_file=read(data_file)
#     return data_file

    #read from database
    #return read()

#def database_bad_user():
    #return read()

    #modify database

def database(action,*args, **kwargs): 
    #read from database
    #mdify database
    #delete from database
    #autnenticate user
    if action == 'read':
        return read(**kwargs)
    if action == 'modify':
        return modify(**kwargs)
    if action == 'delete':
        return delete(**kwargs)


def read(file_path):
    with open(file_path, 'r') as file:
        user = file.read().split(',')
        return user

# def modify(user_response):#write to the database
#     f= open("day5/customercare.txt", "a")
#     f.write(',' + user_response)
#     f.close()


def modify(file_path, content):
    file = open(file_path, 'a') # r, w, a, rb, wb, ab
    file.write(',' + content)
    file.close()

def auth (user, password):
    ...
    login_input = input("Enter your login: ")
    password_input = input("Enter your password: ")
    users(valu_input)


# def delete(file_path, content, style): 
#     file = open(file_path, 'r').read()
#     filtered = ''
    
#     if style == 'landscape':
#         for  i in file.split(','): 
#             if i != content:
#                 filtered += i + ','
#         open(file_path, 'w').write(filtered)

#     elif style == 'portrait':
#         for  i in file.split(','): 
#             if i != content:
#                 open(file_path, 'w').write(i + '\n')
#     else:
#         print("Invalid style")

def delete(file_path, content,remove_input): 
    file = open(file_path, 'r').read()
    filtered = ''
    split_db=file.rstrip().split(',')
    length=len(split_db)-1
    if remove_input== 'Y':
        for  index,i in enumerate(split_db): 
            if i != content:
                if index != length: 
                    filtered += i + ','
                else:
                    filtered += i  
        open(file_path, 'w').write(filtered) 

        #         filtered += i #+ ','
        # open(file_path, 'w').write(filtered)


def main():
    hola()
    #remove_record()
    #database()

# temp_database = database(customercare)# customer care 
# print(temp_database)
# bad_users = database(baduser) # Internal Audit
# print(bad_users)

main()
# temp_database=database('read', file_path = 'day5/customercare.txt') #
# bad_users=database('read', file_path = 'day5/internalaudit.txt')
# database('delete', file_path= 'day5/customercare.txt', content='Ade', style= 'portrait') #
# database('modify', file_path = 'day5/internalaudit.txt', content =  'Ade')
# main()
# read('day5/customercare.txt')
# read('day5/internalaudit.txt')