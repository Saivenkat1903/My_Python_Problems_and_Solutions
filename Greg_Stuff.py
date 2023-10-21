''' First time experimenting with Regular Expressions '''

import re

y=list()
x=input("Enter a regular expression.\n")

fhand=open("mbox.txt")

for line in fhand:
    if re.search(x,line):
        y.append(line)
z=len(y)
print("mbox.txt had "+str(z)+" lines which matched "+x+".")
