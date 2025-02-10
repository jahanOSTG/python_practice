"""
Algorithm: Sum of Numbers from Input
1. Start
2. Take input as a string of numbers separated by spaces
3. Split the string into a list of individual number strings
4. Initialize sum as 0
5. Convert each number string into an integer and add it to sum
6. Print the total sum
7. End
"""

n= input("Enter a text of numbers:")
list= n.split() #split() is used to break the input string into a list of words/numbers.
                #if the user inputs "10 20 30", split() will convert it into ['10', '20', '30']
sum=0
for num in list:
    sum=sum+ int(num)
print(sum)
