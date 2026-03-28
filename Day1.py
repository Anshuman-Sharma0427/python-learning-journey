# Chapter - 2
# Pg - 21 , 22

# Fancy credits Program
# print("\t\tFancy credits Program")
# print("\tAnshuman\nSharma")

# Escape Sequence - ("/t") - this is only use inside the quotes whenever you need.
# So , you have wondered that how to print a backslash when python see this as a starting of an escape sequence. Well you just have to use 2 backslashes (\\).

# print("My hair stylist , Henry \' The Great,\' who never says\"can\'t\"")

# Inserting a new line we use \n but inside the quotes.
# print("Hello\nWorld")

# print("\aAnshuman")

#"\a" this escape character send a signal to the operating system to alert the user by making a beep sound. But now in modern terminal or mac or anyother operating system this might not work as expected.

# print("\nThis string" + "is on a new line.")
# print("\nThis string"+ "is on a new line.")
# print("\nThis string" +"is on a new line.")
# print("\nThis string"+"is on a new line.")
# print("\nThis string"+" is on a new line.")

# To add strings there should space in the second string.like in the last string " is on a new line." there is space between the double quotes and is.

# Line continuation character \ is for the code readability only not for the output and functionality.

from turtle import st


print("Hello I am a BTech student and "\
    + " I am in 2nd year of my college."\
    + " I am learning python and I am loving it.")


