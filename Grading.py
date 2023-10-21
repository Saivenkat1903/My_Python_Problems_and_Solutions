''' First time using if-else loops in order to write programs '''

data=input("Please input the numerical score you have achieved.\n")


try:
    float(data)
    if float(data)<=0.6:
        print("Honestly you could do better, you got a grade F for this semester")
    else:
        if float(data)<=0.7:
            print("This is nothing to be proud of, you got a grade D this semester")
        else:
            if float(data)<=0.8:
                print("Average is not good enough these days, you got a grade C this semester")
            else:
                if float(data)<=0.9:
                    print("Great work! Work even harder and you can turn your grade B this semester to a grade A")
                else:
                    if float(data)>0.9 and float(data)<=1:
                        print("Keep up the good work, you got the best grade, grade A this semester")
                    else:
                        print("Please input the number between 0-1 which depicts your performance in the finals")
except:
    print("Please input the number between 0-1 which depicts your performance in the finals")






    #Program takes the number between 0-1 and associates it with the given grade based on the system
    #system being 0-0.6 F   0.6-0.7 D   0.7-0.8 C   0.8-0.9 B   0.9-1 A
