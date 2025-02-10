n= input("Enter a text of numbers:")
list= n.split() #split() is used to break the input string into a list of words/numbers.
                #if the user inputs "10 20 30", split() will convert it into ['10', '20', '30']
sum=0
for num in list:
    sum=sum+ int(num)
print(sum)