#every object in python has a type
print(type('hello')) #str 
print(type(str)) #type
print(type(1)) #str 
print(type(str)) #type



#data types
# boolean True False

# == vs is

# variables
 #variables are placeholders for data or objects



# integer 1 - 100000000 int
# float decimal 1.0 - 100000000.0 float
# string 'hello' "hello" """hello""" str

# list []   l
# tuple ()

# dictionary {}
# set {}



# DRY - Don't Repeat Yourself
# Variable_1
#variable_1
# var_1__2
# 1vars XXX
# VARIABLE_1

variable = 'The'

sentence = f'{variable} quick brown fox jumped over {variable} lazy dog'

pi= 3.15

calc = 200 * pi # multiple  pie
cla2 = 150 * pi 
calc4 = 100 * pi


#ty

#Methods
class Car:
    #attributes
    tires = 4

    def drive(self):
        print('driving')
    pass

ford = Car()

print(ford.tires)
print(ford.drive())

class str:
 #attributes
 #methods
    pass