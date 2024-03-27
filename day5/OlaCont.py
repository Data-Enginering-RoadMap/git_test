
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

customercare = ''
baduser = 

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
        print("BAD USER!!!!")
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
    data_file = read(data_file)
    return data_file

    #read from database
    #database_txt = read('day5/customercare.txt')
    return database_txt
    #modify database
    #delete from database
    ...
    #write and the input into the textfile when the name doesn't already exist in
def databasebaduser():
    return read('day5/internalaudit.txt')


def read(file_path):
    with open(file_path, 'r') as file:
        user = file.read().split(',')
        return user

def modify(user_response):
    f =open('day5/customercare.txt')
    f.write(',' + user_response)
    f.close()
    ... 


def delete():
    ... 

def main():
    hola()
    database()

temp_database = database(customercare) # customer care 
print(temp_database)
bad_users = database(baduser) # Internal Audit
print(bad_users)


main()
# read('day5/customercare.txt')
# read('day5/internalaudit.txt')S