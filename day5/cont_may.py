
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

customercare="day5/customercare.txt"
baduser="day5/internalaudit.txt"

def hola():
    '''The name of the bot is Hola'''
    #read from database
    # grab users input
    valu_input = input("Enter your name: ")
    users(valu_input)



def greetings():
    ...

def users(response):

    if response: #truthy falsy

        validated_user = validate(response) # caps version of response
        response = validated_user
        # response = validate(response)
        
        print("Hello, " + response + "! " + validated_user)
    else:
        raise Exception("You did not enter a name") ## exceptions
    ...
    


def validate(user_response):
    user_response = user_response.capitalize()
    if user_response in bad_users:
        print(f"You are a bad user.Geroouuutttttt")
        return user_response
    elif user_response not in temp_database:
        temp_database.append(user_response)
        print(temp_database)
        modify(user_response)
        return user_response
    else:
        print(f"You are already in the database {temp_database}")
    return user_response

def database(data_file):
    data_file=read(data_file)
    return data_file

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

def modify(user_response):#write to the database
    f= open("day5/customercare.txt", "a")
    f.write(',' + user_response)
    f.close()


def modify(file_path, content):
    file = open(file_path, 'a') # r, w, a, rb, wb, ab
    file.write(content)
    file.close()

def auth (user, password):
    ...



def delete(file_path, content, style): 
    file = open(file_path, 'r').read()
    filtered = ''
    
    if style == 'landscape':
        for  i in file.split(','): 
            if i != content:
                filtered += i + ','
        open(file_path, 'w').write(filtered)

    elif style == 'portrait':
        for  i in file.split(','): 
            if i != content:
                open(file_path, 'w').write(i + '\n')
    else:
        print("Invalid style")



def main():
    hola()
    #database()

<<<<<<< HEAD
temp_database = database(customercare)# customer care 
print(temp_database)
bad_users = database(baduser) # Internal Audit
print(bad_users)

main()
=======
database('read', file_path = 'day5/customercare.txt') #
database('delete', file_path= 'day5/customercare.txt', content='Ade', style= 'portrait') #
database('modify', file_path = 'day5/internalaudit.txt', content =  'Ade')
# main()
>>>>>>> c10c642ca55f0d6e43fc654de8528d72ccc74c0a
# read('day5/customercare.txt')
# read('day5/internalaudit.txt')