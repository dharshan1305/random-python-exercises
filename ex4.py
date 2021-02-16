#Write a program that accepts a sequence of numbers.
#Return those numbers in a list and a tuple

number = input("Please enter numbers seperated with commas: ")
l=number.split(",")
t=tuple(l)
print(l)
print(t)
