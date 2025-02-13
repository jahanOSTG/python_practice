#FIFO=First In First Out

from collections import deque  # deque - Double Ended Queue

bank = deque(("Rima", "Mina", "Mita"))  

print(bank)

bank.popleft()  # Remove the leftmost (first) element

print(bank)
