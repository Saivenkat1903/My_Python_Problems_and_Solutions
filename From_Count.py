''' For a given file, counts the amount of times the word From is mentioned '''

file=input("Enter your file name:\n")

fhand=open(file)
count=0

for line in fhand:
    thing=line.split()
    if len(thing)==0:
        continue
    elif thing[0]=="From" and len(thing)!=0:
        count=count+1
        print(thing[1])
    else:
        continue
print("There were "+str(count)+" lines in the file with From as the first word")
