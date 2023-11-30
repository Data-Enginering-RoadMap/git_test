from pathlib import Path

# hint: use the pathlib module to get the path of the file
ROOT = Path(__file__).parent.parent
file_path = ROOT / 'Data'/'data.csv'


# hint: use the with statement to open the file
# hint: use the readlines method to read by itereating oeach line
# with open(file_path, 'r') as file:
#     contents = file.readlines()


#      OR 
# hint: use the read method to read the entire file
# with open(file_path, 'r') as file:
#     contents = file.read()



# Section 1: Reading files


#question 1: Read the file and print the contents



# question 2: Read the file and print the contents without the empty lines

# question 3: Read the file and print the contents without the empty lines and the lines that start with a hashtag (#)
# Quetion 4: Count the number of lines in the file


# Section 2: text processing and Manupulation

# Question 1: Count the total number of words in the file
# Question 2: Count the total number of characters in the file including spaces
# Question 3: Count the total number of characters in the file excluding spaces
# Question 4: ICount the number of times each word appears in the file
# Question 5 Identify the longest word in the file
# Question 6: Identify the shortest word in the file
# Question 7: Identify the most frequent word in the file
