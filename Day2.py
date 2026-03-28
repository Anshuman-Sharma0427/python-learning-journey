# Quotation Manipulation
str = "my name is anshuman Sharma and i am a ai & ml engineer."
print(str)
print(str.upper())
print(str.lower())
print(str.title())
print(str.replace("anshuman", "anshu"))

#!Question--1.
# What if i want to replace string from end , at middle and from a specific position .

text = "one two two two"
# rsplit method is used to split from right to left.And the second argument tell from where to split.
from_end = text.rsplit("two" , 1)
# join method is used to join string into list and also convert the list into string.(always join in between)
text = "three".join(from_end)
print(text)

x = "one,two,three,four,five,six,seven,eight"
y = x.rsplit(",")
# z = "nine".join(y)
print(y)

###################################################################

