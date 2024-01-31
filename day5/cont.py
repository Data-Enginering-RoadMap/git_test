
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
    if user_response not in temp_database and user_response not in bad_users:
        temp_database.append(user_response)
        print(temp_database)
        return user_response
    else:
        print(f"You are already in the database {temp_database}")
    return user_response

def database():

    #read from database
    return read('day5/customercare.txt')

    #modify database
    #delete from database
    ...



def read(file_path):
    with open(file_path, 'r') as file:
        user = file.read().split(',')
        return user

def modify():
    ... 


def delete():
    ... 

def main():
    hola()
    database()

temp_database = database() # customer care 
print(temp_database)
bad_users = ['samson'] # Internal Audit


# main()
# read('day5/customercare.txt')
# read('day5/internalaudit.txt')