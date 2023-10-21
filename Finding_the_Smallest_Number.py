''' Finds the smallest number given a set of numbers '''

given=input("enter the numbers\n").split()

smallest=None

for number in given:
    int(number)
    if smallest==None or int(number)<smallest:
        smallest=int(number)

print("the smallest number in this list is",smallest)
