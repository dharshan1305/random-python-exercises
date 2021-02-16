#Write a program that calcultes a factorial.

#I will use recursion to do this

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

num = int(input("Please enter a number: "))
print(factorial(num))
