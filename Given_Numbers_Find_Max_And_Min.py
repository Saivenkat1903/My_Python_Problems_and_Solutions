''' Find the max and min of a given set of Numbers '''

max=0
min=0
while True:
    x=input("Enter a number?\n")
    try:
        if x!="done" and x!="DONE" and x!="Done":
            float(x)
            while max==0 or max<x:
                max=x
            while min==0 or min>x:
                    min=x
        else:
            if x=="done" or x=="Done" or x=="DONE":
                print("This is the maximum number of the numbers given", max)
                print("This is the minimum number of the numbers given", min)
                break
    except:
        print("Invalid input")
        print("Type in a number only please")
        continue

#Given_Numbers_Find_Max_And_Min.py
