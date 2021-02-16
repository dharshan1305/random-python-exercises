#define  class wit two methods, getString and printString.
#get string to get the string from console input
#print string to print the string in uppercase

#I will use an init method to set the attribute


class InputOutString():
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Please enter a sentence: ")

    def printString(self):
        print(self.string.upper())

stringObj = InputOutString()
stringObj.getString()
stringObj.printString()

