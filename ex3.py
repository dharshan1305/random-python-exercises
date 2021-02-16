#Write a program that returns (i, i*i) in the form of a dictionary
#The numbers must be within the the range 1 and n
#so input 3 will be (1:1, 2:4, 3:9)

#The question is pretty straight forward.
#The formula would be d[i] = i*i.


num = int(input("Please enter a number: "))
d = dict()
for i in range(1, num+1):
    d[i]=i*i
print(d)
