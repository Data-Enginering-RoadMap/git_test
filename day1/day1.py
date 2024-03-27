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

a='1'
print (a)


b ='Coding'
c ='For'
d= 'All'
X = b + ' ' + c + ' ' + d
print (X)


code = 'coding for all'
capitalize = code.capitalize()
print(capitalize)
title = code.title()
print(title)
swap = code.swapcase()
print(swap)


check = 'Coding For All'
x = check.index('Coding')
print(x)

find = check.find('Coding')
print(find)

chan = 'Python for Everyone'
rep = chan.replace('Everyone','All')
print(rep)


code = 'Coding for All'
spt =code.split(' ')
print(spt)

tec = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
tec_spt = tec.split(',')
print(tec_spt)


char ='_Coding For All_.'
ind = char[0]
print(ind)

char ='_Coding For All_.'
str = len(char)
print(str)
cod = 'Coding For All'
cod2= cod[10]
print(cod2)

word ='Python For Everyone'
spt = word.split()
acro = '.'.join(work[0] for work in spt)
print(acro)


cod19 ='Coding For All'
num19 = cod19.split()
res19 =' '. join(word[0] for word in num19)
print(res19)


str20 = 'Coding for All'
res20 = str20.index('C')
print(res20)

str21 = 'Coding For All'
res21 = str21.index('F')
print(res21)

str22 = 'Coding For All People'
res22 = str22.rfind('l')
print(res22)

str23 = 'You cannot end a sentence with because because because is a conjunction'
res23 = str23.find('because')
print(res23)
str23 = 'You cannot end a sentence with because because because is a conjunction'
res23 = str23.index('because')
print(res23)

str23 = 'You cannot end a sentence with because because because is a conjunction'
res23 = str23.rfind('because')
print(res23)

str25 = 'You cannot end a sentence with because because because is a conjunction'
res25 = str25.replace('because','')
print(res25)


string30 = "&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;"
res30 = string30.strip("&nbsp;")
print(res30)

string31 = '30DaysOfPython'
res31 = string31.isidentifier()
print(res31)

str31 = 'thirty_days_of_python'
result31 = str31.isidentifier()
print(result31)

str32 = 'the,boy,is,going,to,school'
res32 = ' ' .join(word.capitalize() for word in str32.split(','))
print(res32)

stri32 = 'the,boy,is,going,to,school'
resu32 = ' '. join(word.upper() for word in stri32.split(','))
print(resu32)

strin32 = 'the,boy,is,going,to,school'
resul32 = '-' .join(strin32.split(','))
print(resul32)

strin32 = 'the,boy,is,going,to,school'
resul32 = strin32.replace("," ,"-")
print(resul32)

print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')


radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square.')




a = 8
b = 6
add = f'{a} + {b} = {a + b}'
sub = f'{a} - {b} = {a - b}'
mult = f'{a} * {b} = {a * b}'
divi = f'{a} / {b} = {a / b:.2f}'
mode = f'{a} % {b} = {a % b}'
divi2 = f'{a} // {b} = {a // b}'
expo = f'{a} ** {b} = {a ** b}'

print(add)
print(sub)
print(mult)
print(divi)
print(mode)
print(divi2)
print(expo)

text = "_Coding For All_String'"
slice = text.split()[0]
print(slice)