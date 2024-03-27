from pathlib import Path

# hint: use the pathlib module to get the path of the file
ROOT = Path(__file__).parent.parent
file_path = ROOT / 'Data'/'data.csv'


# hint: use the with statement to open the file
# hint: use the readlines method to read by itereating oeach line


#      OR 
# hint: use the read method to read the entire file
# with open(file_path, 'r') as file:
#     contents = file.read()



# Section 1: Reading files


#question 1: Read the file and print the contents
with open(file_path, 'r') as file:
   contents = file.readlines()
print(contents)


# question 2: Read the file and print the contents without the empty lines
for content in contents:
   if content.strip():
      print(content.strip())


# question 3: Read the file and print the contents without the empty lines and the lines that start with a hashtag (#)
for content2 in contents:
   if content2.strip()and not content2.startswith('#'):
      print(content2.strip())
# Quetion 4: Count the number of lines in the file
length = len(contents)
print(length)

# Section 2: text processing and Manupulation

# Question 1: Count the total number of words in the file
with open(file_path, 'r') as file:
    content3 = file.read()
len_word = len(content3)
print(len_word)

# Question 2: Count the total number of characters in the file including spaces
len_word2= len(content3)
print(len_word2)
# Question 3: Count the total number of characters in the file excluding spaces
len_word3 = len(content3.replace(" ",""))
print(len_word3)
# Question 4: ICount the number of times each word appears in the file
words = content3.split()
word_count ={}
for word in words:
   word = word.strip('.,:#')
   word_count[word] = word_count.get(word, 0) + 1
   #print(word_count)
   #word_result = 
   for word,count in word_count.items():
      print(f"{word} : {count}")

# Question 5 Identify the longest word in the file
      #longword = ""
      #max_len = 0
      #for word in words:
       # word = word.strip('.,:#')
       # if len(word) > max_len:
          # longword = word
          # max_len =len(word)
      longword = max(words, key = len)
      print(longword)

# Question 6: Identify the shortest word in the file
      shortword = min(words, key = len)
      print(shortword)
# Question 7: Identify the most frequent word in the file
      wordcount ={}
      for word in words:
         word = word.strip('.,:#').lower
         wordcount[word] = wordcount.get(word, 0) + 1
         most_freq_word = max(wordcount, key = wordcount.get)
         print(most_freq_word)
