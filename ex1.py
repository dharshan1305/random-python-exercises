#A program that will find numbers between 1 and 500
#The number returned must be divisible by 3 and a multiple of 5

#First I will create  list to hold the returned values
#I will loop through the range of 1 and 500
#I will use of statement to sort through the divisible and multiples

list = []
for i in range(1, 500):
    if (i%3 ==0) and (i%5!=0):
        list.append(str(i))
print(','.join(list))
