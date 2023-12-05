
my_bot = input("Enter your your name and a number: ")   #DRY
print(my_bot)

# def greeting1():Ade,2_bot} !")

# def greeting2():
#     print(f"Hello {my_bot} !")

# def greeting3():
#     print(f"Hello {my_bot} !")

# if my_bot == "chatGPT":
#     greeting1()
# elif my_bot == "alexa":
#     greeting2()
# else:
#     greeting3()

Last login: Tue Dec  5 17:46:40 on ttys054
Agent pid 80099
Identity added: /Users/ADEFIA01/.ssh/id_rsa (ADEFIA01@KFMFVFGTAEFQ05N)





















┌─(~)─────────────────────────────────────────(ADEFIA01@KFMFVFGTAEFQ05N:s054)─┐
└─(18:06:37)──> clear                                                                                                                                                                                                         ──(Tue,Dec05)─┘





































┌─(~)───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────(ADEFIA01@KFMFVFGTAEFQ05N:s054)─┐
└─(18:06:39)──>                                                                                                                                                                                                               ──(Tue,Dec05)─┘



























































┌─(~)───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────(ADEFIA01@KFMFVFGTAEFQ05N:s054)─┐
└─(18:06:44)──> clear                                                                                                                          ──(Tue,Dec05)─┘



┌─(~)────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────(ADEFIA01@KFMFVFGTAEFQ05N:s054)─┐
└─(18:06:48)──> cd Desktop/test_git/git_test                                                                                                   ──(Tue,Dec05)─┘
┌─(~/Desktop/test_git/git_test)──────────────────────────────────────────────────────────────────────────────────────────────(ADEFIA01@KFMFVFGTAEFQ05N:s054)─┐
└─(18:06:55 on main ✭)──> source venv/bin/activate                                                                                             ──(Tue,Dec05)─┘
(venv) ┌─(~/Desktop/test_git/git_test)──────────────────────────────────────────────────────────────────────────────────────────────(ADEFIA01@KFMFVFGTAEFQ05N:s054)─┐
└─(18:06:59 on main ✭)──> python -m bpython                                                                                                    ──(Tue,Dec05)─┘
bpython version 0.24 on top of Python 3.10.5 /Users/ADEFIA01/Desktop/test_git/git_test/venv/bin/python
>>> # type hinting
>>> var_1 = 'sting'
>>> var_1 = 1
>>> var_1 = False
>>> string : str = 'string variable type'
>>> string : str = 1
>>> boolean: bool 
>>> boolean
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    boolean
NameError: name 'boolean' is not defined
>>> boolean: bool 
>>> boolean = False
>>> for i in range(10):
...     print(i)
...     
... 
0
1
2
3
4
5
6
7
8
9
>>> # function is composed of 4 layers
>>> # definition 
>>> # usually optional - parameters --- Parameter vs Arguements 
>>> # Body
>>> # Return statements
>>> # Return statements
>>> # usually optional - parameters --- Parameter vs Arguements 
>>> # Body
>>> # definition 
>>> # def < name > (...):
>>> #naming conventions 
>>> #camelCasing
>>> def namingFunction():
...     pass
... 
>>> #Pascal
>>> def NamingFunction():
...     ...
... 
>>> #snake_casing
>>> def naming_function():
...     pass
... 
>>> 
>>> def counter():
...     for i in range(10):
...         print(i)
...         
...     
... 
>>> counter
<function counter at 0x101e81870>
>>> dir()
['NamingFunction', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'boolean', 'counter', 'help', 'i', 'namin
gFunction', 'naming_function', 'string', 'var_1']
>>> bot = input()
samoke
>>> print(bot)
samoke
>>> def greeting_bot(name: str)
  File "<input>", line 1
    def greeting_bot(name: str)
                               ^
SyntaxError: expected ':'
>>> def greeting_bot(name: str)
  File "<input>", line 1
    def greeting_bot(name: str)
                               ^
SyntaxError: expected ':'
>>> 
[No write since last change]                                                                                                                                   
>>> def greeting_bot(name: str):
...     if name == 'Alexa':
...         print('Hello, My name is Alexa')
...     else: 
...         print('Unknown Command')
...         
#<---History inconsistent with output shown--->
... 
>>> usr_name = input('what bot are you looking for:')
what bot are you looking for:Alexa
>>> usr_name
'Alexa'
>>> greeting_bot()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    greeting_bot()
TypeError: greeting_bot() missing 1 required positional argument: 'name'
>>> greeting_bot(usr_name)
Hello, My name is Alexa
>>> def greeting_complex(name: str, number: int):
...     for i in range(number):
...         print(f'Hello {name}')
...         
...     
... 
>>> ans = input('enter your name and a number:')
enter your name and a number:Ade,2
>>> ans
'Ade,2'
>>> greeting_complex('Ade', 2)
Hello Ade
Hello Ade
>>> #split ans
>>> #create 2 variables to store result
>>> #strip
>>> ans.strip()
'Ade,2'
>>> ans.strip(',')
'Ade,2'
>>> ans.split()
['Ade,2']
>>> ans.split(',')
['Ade', '2']
>>> result = ans.split(',')
>>> name= result[0]
>>> no = int(result[1])
>>> greeting_complex(name, no)
Hello Ade
Hello Ade
>>> name2,no2 = ans.split(',')
>>> greeting_complex(name2, int(no2))
Hello Ade
Hello Ade
>>> def greeting_with_default_value(name:str, no=2):
...     for i in range(no):
...         print(f'welcome {Ade}')
...         
...     
... 
>>> answer = input('enter response:').split(',')
enter response:Ade,2
>>> answer
['Ade', '2']
>>> answer = input('enter response:').split(',')
enter response:Ade
>>> answer
['Ade']
>>> 
>>> answer = input('enter response:').split(',')
enter response:2
>>> answer
['2']
>>> user1 = input('enter response:').split(',')
enter response:Ade,2
>>> user1
['Ade', '2']
>>> user2 = input('enter response:').split(',')
enter response:John
>>> user2
['John']
>>> def usr_input():
...     prompt = input()
...     if ',' in prompt:
...         answe = prompt.split(',')
...         print(answe)
...     elif ' ' in prompt:
...         answe = prompt.split(' ')
...         print(answe)
...     else:
...         print('Wrong input')
...         
...     
... 
>>> usr_input()
Ada 3
['Ada', '3']
>>> usr_input()
John 12
['John', '12']
>>> usr_input()
Ada,11
['Ada', '11']
>>> usr_input()
Samsmith
Wrong input
>>> answer2 = usr_input()
Ade,2
['Ade', '2']
>>> answer2
>>> print(answer2)
None
>>> var1 = print('hello')
hello
>>> print(var1)
None
>>> # Return statment
>>> # Every function must return something
>>> def somethin_return():
...     return 'Hello'
... 
>>> print(somethin_return())
Hello
>>> def somethin_without_return():
...     print('hello')
...     
... 
>>> print(somethin_without_return())
hello
None
>>> def usr_input():
... ...     prompt = input()
  File "<bpython-input-1612>", line 2
    ...     prompt = input()
#<---History contiguity broken by rewind--->
['Ada', '3']
>>> usr_input()
Ade,2
['Ade', '2']
>>> usr_input()
John 12
['John', '12']
>>> usr_input()
Ada,11
['Ada', '11']
>>> answer2 = usr_input()
Samsmith
Wrong input
>>> answer2
>>> print(answer2)
None
>>> var1 = print('hello')
hello
>>> print(var1)
None
>>> # Return statment
>>> # Every function must return something
>>> def somethin_return():
...     return 'Hello'
... 
>>> print(somethin_return())
Hello
>>> def somethin_without_return():
...     print('hello')
...     
... 
>>> print(somethin_without_return())
hello
None
>>> def usr_input_v2():
...     prompt = input('Enter your response')
...     answer = prompt.split(',') if ',' in prompt else prompt.split(' ')
...     if len(answer) == 2:
...         return answer
...     else: 
...         print('Error!!!')
...         
...     
... 
>>> usr_input_v2()
Enter your responseAde,2
['Ade', '2']
>>> usr_input_v2()
Enter your responseAde,2
['Ade', '2']
>>> new_response = usr_input_v2()
Enter your responseAde1
Error!!!
>>> new_response
>>> name, number = new_response[0], int(new_response[1])
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    name, number = new_response[0], int(new_response[1])
TypeError: 'NoneType' object is not subscriptable
>>> greeting_with_default_value(name,number)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    greeting_with_default_value(name,number)
NameError: name 'number' is not defined
>>> greeting_with_default_value(name,number)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    greeting_with_default_value(name,number)
NameError: name 'number' is not defined
>>> name, number = new_response[0], int(new_response[1])
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    name, number = new_response[0], int(new_response[1])
TypeError: 'NoneType' object is not subscriptable
>>> new_response
>>> new_response = usr_input_v2()
Enter your responseAde2
Error!!!
>>> new_response = usr_input_v2()
Enter your responseAde,2
>>> name, number = new_response[0], int(new_response[1])
>>> greeting_with_default_value(name,number)
welcome Ade
welcome Ade
>>> list_users = [('Ada',22),('Tyla',22)]
>>> for i in list_users:
...     print(i)
...     
... 
('Ada', 22)
('Tyla', 22)
>>> for i, j in list_users:
...     greeting_with_default_value(i,j)
...     
... 
welcome Ada
welcome Ada
welcome Ada
welcome Ada
welcome Ada
welcome Ada
welcome Ada
welcome Ada
welcome Ada
welcome Ada
welcome Ada
welcome Ada
welcome Ada
welcome Ada
welcome Ada
welcome Ada
welcome Ada
welcome Ada
welcome Ada
welcome Ada
welcome Ada
welcome Ada
welcome Tyla
welcome Tyla
welcome Tyla
welcome Tyla
welcome Tyla
welcome Tyla
welcome Tyla
welcome Tyla
welcome Tyla
welcome Tyla
welcome Tyla
welcome Tyla
welcome Tyla
welcome Tyla
welcome Tyla
welcome Tyla
welcome Tyla
welcome Tyla
welcome Tyla
welcome Tyla
welcome Tyla
welcome Tyla
>>> list_users = [('Ada',2),('Tyla',2)]
>>> for i, j in list_users:
...     greeting_with_default_value(i,j)
welcome Tyla
welcome Tyla
welcome Tyla
>>> list_users = [('Ada',2),('Tyla',2)]
>>> for i, j in list_users:
...     greeting_with_default_value(i,j)
...     
... 
welcome Ada
welcome Ada
welcome Tyla
welcome Tyla
>>> for i in list_users:
...     greeting_with_default_value(*i)
...     
... 
welcome Ada
welcome Ada
welcome Tyla
welcome Tyla
>>> def any_var_name(*args):
...     print(args)
...     
... 
>>> 
>>> any_var_name(1,2,3,4,5,6,6)
(1, 2, 3, 4, 5, 6, 6)
>>> def any_var_name(*args):
...     for i in args:
...         print(i)
...         
...     
... 
>>> def greewting_position(*args):
...     name, no, *_ = args
...     print(name, no)
...     
... 
>>> 
>>> greewting_position('Ade', 22,'Address', 'pobox', False)
Ade 22
>>> def grreeting_keyword(**kwargs):
...     print(kwargs)
...     
... 
>>> grreeting_keyword('Ade', 22,'Address', 'pobox', False)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    grreeting_keyword('Ade', 22,'Address', 'pobox', False)
TypeError: grreeting_keyword() takes 0 positional arguments but 5 were given
>>> list_user= {'pbox': 1234,'name': 'John', 'nu':3}
>>> grreeting_keyword(name = 'Ade')
{'name': 'Ade'}
>>> 
 
 
 
 
 
1   ### current bpython session - make changes and save to reevaluate session.                
  1 ### lines beginning with ### will be ignored.                                             
  2 ### To return to bpython without reevaluating make no changes to this file                
  3 ### or save an empty file.                                                                
  4 # type hinting                                                                            
  5 var_1 = 'sting'                                                                           
  6 var_1 = 1                                                                                 
  7 var_1 = False                                                                             
  8 string : str = 'string variable type'                                                     
  9 string : str = 1                                                                          
 10 boolean: bool                                                                             
 11 boolean                                                                                   
 12 # OUT: Traceback (most recent call last):                                                 
 13 # OUT:   File "<input>", line 1, in <module>                                              
 14 # OUT:     boolean                                                                        
 15 # OUT: NameError: name 'boolean' is not defined                                           
 16 boolean: bool                                                                             
 17 boolean = False                                                                           
 18 for i in range(10):                                                                       
 19     print(i)                                                                              
 20                                                                                           
 21                                                                                           
 22 # OUT: 0                                                                                  
 23 # OUT: 1                                                                                  
 24 # OUT: 2                                                                                  
 25 # OUT: 3                                                                                  
 26 # OUT: 4                                                                                  
 27 # OUT: 5                                                                                  
 28 # OUT: 6                                                                                  
 29 # OUT: 7                                                                                  
 30 # OUT: 8                                                                                  
 31 # OUT: 9                                                                                  
 32 # function is composed of 4 layers                                                        
 33 # definition                                                                              
 34 # usually optional - parameters --- Parameter vs Arguements                               
 35 # Body                                                                                    
 36 # Return statements                                                                       
 37 # Return statements                                                                       
"/var/folders/qw/mqlq39k57r9b96xcws4zl15m0000gp/T/tmpr_i8oinx.py" [noeol] 371L, 8687B
