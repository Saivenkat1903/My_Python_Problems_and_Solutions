''' Learning about the while loop in order to make a countdown programs '''

i=int(input("Please enter number from which to start countdown"))
while True:
        if i!=0:
            print(i)
            i=i-1
            continue
        else:
            if i==0:
                print("BLAST OFF!!")
                break
