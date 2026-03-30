# Starting of Branching , While Loops and Program planning

#------------------------------------------------------------------

#.        ** Craps Roller Program

import random
# Generating random numbers using random module
die_1 = random.randint(1,6)
die_2 = random.randrange(6) + 1
total = die_1 + die_2
print("You rolled a",die_1,"and a",die_2,"for a total of",total)

#------------------------------------------------------------------

#.        **  Password Program

password = "abc123"
user_input = input("Enter the password: ")
if user_input == password:
    print("Access granted.")
else:
    print("Access denied.")

# In real world , to create a password validation system , a programmer use some form of cryptography.

if "zpple" < "orange":
    print("true")

# Here the results are based on the alphabetical order. 