''' Messing around with tuples '''

file=input("Enter the file name\n")

thing=dict()
fhand=open(file)

for line in fhand:
    line=line.strip()
    line=line.split()
    if len(line)>5 and line[0]=="From":
        z=line[5]
        a=z[:2]
        thing[a]=thing.get(a,0)+1
    else:
        continue
x=list(thing.items())

for (time,count) in x:
    print(str(time)+" "+str(count))
