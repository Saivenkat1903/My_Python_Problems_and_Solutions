''' Using lists to calculate max min sum and average of a set of numbers '''

while True:
    thing=list()
    x=input("Welcome! This program is meant to tell you the maximum, minimum, sum and average of the given numbers you input! Enter 'start' to start giving your numbers or 'close' to leave the program\n")
    if x in ["start","Start"]:
        while True:
            y=input("Please enter your numbers when prompted and when you are done; type in done\n")
            try:
                float(y)
                thing.append(float(y))
                continue
            except:
                if y in ["Done","done"]:
                    print(max(thing))
                    print(min(thing))
                    print(sum(thing))
                    print(len(thing))
                    print(sum(thing)/len(thing))
                    break
                else:
                    print("please enter a number only!")
                    continue
    elif x in ["close","Close"]:
        quit()
    else:
        print("Please follow the instructions idiot.")
    continue    
