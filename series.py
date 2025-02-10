#series: 1 + 2 + 3 + 4 +........+n 
n = int(input("Enter the last number of the series: ")) 
 # taking last v alue from user

sum = 0  

for i in range(1, n + 1): # i =iteration number
  sum =sum+ i  
print(sum)  # Fixed indentation







#series: 2 + 4 + 6 +........+n 
n = int(input("Enter the ending value: "))  

sum = 0

for i in range(2, n + 1,2):  # Fixed step argument
   sum =sum+ i  # Corrected addition syntax

print(sum)  # Fixed indentation