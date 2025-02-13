def add(*numbers):
    sum=0
    for x in numbers:
        sum=sum+x
    print(sum)
add(6,5)
add(4,6,3)


def info(*all):
    print(*all)
info(551,"Faria Jahan Janie")
