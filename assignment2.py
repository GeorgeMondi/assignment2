#1Write a python program to remove a given character from string.
iteam = "python"
char_remove = "t"
final_iteam = iteam.replace(char_remove, " ")
print(iteam)
print(final_iteam)

#2Write a program to check String is Palindrome or not.
iteam = "madam"
iteam2 =iteam[::-1]
if iteam == iteam2:
    print("The given String is a Palindrome.")
else:
    print("The given String is not a Palindrome.")

#3Write a Python program to check given character is vowel or consonant.
iteam = input()
iteam = iteam.lower()
if iteam == "a" or iteam == "e" or iteam == "i" or iteam == "o" or iteam == "u":
    print("The character is a vowel.")
else:
    print("The character is a consonat.")
 
#4Write a python program to replace string space with given character in python.
input = "Hello World!"
replacer = "-"
new_string = input.replace(" ",replacer)
print(new_string)

#5Write a python program to count alphabets, digits ,and special characters in the string.
input = "George@0709#"
alphabet_num = 0
digit_num = 0
special_char_num = 0

for char in input:
    if char.isalpha():
        alphabet_num += 1 
    elif char.isdigit():
        digit_num += 1
    else:
        special_char_num += 1
print("Alphabets:",alphabet_num)
print("Digits:",digit_num)
print("Special_characters:",special_char_num)

#6Write a python program to  remove all the blank spaces in a given String.
input = ("Learning Python is easy")
remove_space = input.replace(" ","")
print(remove_space)

#7Write a python program to find sum of integers in the string.
input = "python3426"
sum_num = 0
current_num = ""
for char in input:
    if char.isdigit():
        current_num += char
    elif current_num:
        sum_num += int(current_num)
        current_num = ""
if current_num:
    sum_num += int(current_num)
print("Sum of integers in the given String:", sum_num)

#8Write a python program to remove Repeated characters from the string.
input = "Grammeraer"
charat = ""
reapeted_char = set()
for char in input:
    if char not in reapeted_char:
        charat += char
        reapeted_char.add(char)
print(charat)

#9Write a python program to count occurrence of given characters in string.
input = "reapeted"
char_count = "e"
count = input.count(char_count)
print(count)

#10Write a python program to check string is anagrams or not in python.
input1 = "george"
input2 = "ganesh"

if len(input1) != len(input2):
    print("The string are not anagrams.")
else:
    print("The strings are anagrams.")





































