#Write a program that calculates and displays the value given the
#formula Q=square root of [(2 *C*D)/H]
#C is 50, H is 30...D is user inputted sequence of numbers

#My output should be in a list, I will also use built in math

import math
c=50
h=30
ans=[]
item=[num for num in input("Enter numbers, seperated by a comma: ").split(',')]
for i in  item:
    ans.append(str(int(round(math.sqrt(2*c*float(i)/h)))))

print(','.join(ans))
