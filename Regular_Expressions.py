''' Using regular expressions to get specific sections from a string '''

import re

thing=list()

file=input("Enter file name.\n")

fhand=open(file)

for line in fhand:
    x=re.findall("New Revision: ([0-9]+)",line)
    if len(x)!=0:
        thing.append(int(x[0]))
    else:
        continue
try:
    while True:
        thing.remove([])
except ValueError:
    pass
if len(thing)!=0:
    z=sum(thing)/len(thing)
    print(z)
else:
    print("0")
