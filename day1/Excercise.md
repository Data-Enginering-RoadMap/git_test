#String Manipulation
### The goal here is to make you familar with some string manipulation process

#
## 💻 Exercises - Day 1

1. Show how to convert a = '1'  where type(a) should return ===> <class int>
   a = '1'
   b = int(a)
   print(b)
2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
b ='Coding'
c ='For'
d= 'All'
x = b + ' ' + c + ' ' + d
print(x)

3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
4. Print the variable company using _print()_.
print(company)
5. Print the length of the company string using _len()_ method and _print()_.
my_string =len(company)
print(my_string)
6. Change all the characters to uppercase letters using _upper()_ method.
upper_case = company.upper()
print(upper_case)
7. Change all the characters to lowercase letters using _lower()_ method.
lower_case = company.lower()
print(company)
8. Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
code = 'coding for all'
capitalize = code.capitaize()
pring (capitalize)
title = code.title()
print(title)
swap = code.swapcase()
print(swap)
9. Cut(slice) out the first word of _Coding For All_ string. 
text = "_Coding For All_String'"
slice = text.split()[0]
print(slice)

10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods. 
check = 'Coding For All'
x = check.index('Coding')
print(x)

find = check.find('Coding')
print(find)



11. Replace the word coding in the string 'Coding For All' to Python.
rep = check.replace('Coding','Python')
print(rep)

12. Change Python for Everyone to Python for All using the replace method or other methods.
chan = 'Python for Everyone'
rep = chan.replace('Everyone','All')
print(rep)
13. Split the string 'Coding For All' using space as the separator (split()) .
code = 'Coding for All'
spt =code.split(' ')
print(spt)
14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
tec = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
tec_spt = tec.split(',')
print(tec_spt)
15. What is the character at index 0 in the string _Coding For All_.
char ='_Coding For All_.'
ind = char[0]
print(ind)


16. What is the last index of the string _Coding For All_.
char ='_Coding For All_.'
str = len(char)
print(str)
17. What character is at index 10 in "Coding For All" string.
cod = 'Coding For All'
cod2= cod[10]
print(cod2)
18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
word ='Python For Everyone'
spt = word.split()
acro = ' ' .join(work[0] for work in spt)
print(acro)
19. Create an acronym or an abbreviation for the name 'Coding For All'.
cod19 ='Coding For All'
num19 = cod19.split()
res19 =' '. join(word[0] for word in num19)
print(res19)
20. Use index to determine the position of the first occurrence of C in Coding For All.
str20 = 'Coding For All'
res20 = str20.index('C')
print(res20)

 21. Use index to determine the position of the first occurrence of F in Coding For All.
 str21 = 'Coding For All'
res21 = str21.index('F')
print(res21)
22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
str22 = 'Coding For All People'
res22 = str22.rfind('l')
print(res22)

23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
str23 = 'You cannot end a sentence with because because because is a conjunction'
res23 = str23.find('because')
print(res23)

24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
str24 = 'You cannot end a sentence with because because because is a conjunction'
res24 = str24.rfind('because')
print(res24)
25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
str25 = 'You cannot end a sentence with because because because is a conjunction'
res25 = str25.replace('because','')
print(res25)
26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
str26 = 'You cannot end a sentence with because because because is a conjunction'
res26 = str26.index('because')
print(res26)
27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
str25 = 'You cannot end a sentence with because because because is a conjunction'
res25 = str25.replace('because','')
print(res25)
28. Does '\'Coding For All' start with a substring _Coding_?
yes
29. Does 'Coding For All' end with a substring _coding_?
No
30. '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;, remove the left and right trailing spaces in the given string.
string30 = '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;'
res30 = string30.strip()
print(res30)
31. Which one of the following variables return True when we use the method isidentifier():
    - 30DaysOfPython #false
    - thirty_days_of_python #true
    string31 = '30DaysOfPython'
    res31 = string31.isidentifier()
    print(res31)

    str31 = 'thirty_days_of_python'
    result31 = str31.isidentifier()
    print(result31)
32. The following string contains the names of some of python libraries: 'the,boy,is,going,to,school' .
str32 = 'the,boy,is,going,to,school'
res32 = ' ' .join(word.capitalize() for word in str32.split(','))
print(res32)
  * Convert it to 'The boy is going to school'
  * Convert it to 'THE BOY IS GOING TO SCHOOL'
  stri32 = 'the,boy,is,going,to,school'
  resu32 = ' '. join(word.upper() for word in stri32.split(','))
  print(resu32)

  * Convert it to 'the-boy-is-going-school'
strin32 = 'the,boy,is,going,to,school'
resul32 = '-' .join(strin32.split(','))
print(resul32)

method 2
strin32 = 'the,boy,is,going,to,school'
resul32 = strin32.replace("," ,"-")
print(resul32)
33. Use the new line escape sequence to separate the following sentences.
    ```py
    I am enjoying this challenge.
    I just wonder what is next.
    ```
    print('I am enjoying this challenge.\nI just wonder what is next')
34. Use a tab escape sequence to write the following lines.
    ```py
    Name      Age     Country   City
    Asabeneh  250     Finland   Helsinki
    ```
    print('Name\tAge\tCountry\tCity')
    print('Asabeneh\t250\tFinland\tHelsinki')
35. Use the string formatting method to display the following:

```sh
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
```
print(f'The area of a circle with radius{radius} is {area} meters square.')

36. Make the following using string formatting methods:

```sh
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
```
a = 8
b = 6
add = f'{a} + {b} = {a + b}'
sub = f'{a} - {b} = {a - b}'
mult = f'{a} * {b} = {a * b}'
divi = f'{a} / {b} = {a / b:.2f}'
mode = f'{a} % {b} = {a % b}'
divi2 = f{a} // {b} = {a // b}'
expo = f{a} ** {b} = {a ** b}'

print(add)
print(sub)
print(mult)
print(divi)
print(mode)
print(divi2)
print(expo)