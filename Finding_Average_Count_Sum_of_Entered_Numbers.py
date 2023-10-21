''' From the given numbers, calculates the average, sum and amount of numbers '''

total=0
count=0
average=0
while True:
    x=input("Enter a number?\n")
    try:
        if x!="done" and x!="DONE" and x!="Done":
            float(x)
            total=total+float(x)
            count=count+1
            average=total/count
            continue
        else:
            if x=="done" or x=="Done" or x=="DONE":
                print("This is the total of the numbers given", total)
                print("This is the total number of numbers given", count)
                print("This is the average of the numbers given", average)
                break
    except:
        print("Invalid input")
        print("Type in a number only please")
        continue
