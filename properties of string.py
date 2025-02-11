#Find the number od words ,digits and letters in a string

numberOfWord=0
numberOfletter=0
numberOfdigit=0
string=input("Enter the String: ")
for x in string:
    x=x.lower()
    if x>='a' and x<='z':
         numberOfletter = numberOfletter+1
    
    elif x>='0' and x<='9':
         numberOfdigit = numberOfdigit+1
         
    elif x==" ":
         numberOfWord = numberOfWord+1  
print(f"Number of words: {numberOfWord+1}")

print(f"Number of letters: {numberOfWord}")

print(f"Number of digits: {numberOfdigit}")
