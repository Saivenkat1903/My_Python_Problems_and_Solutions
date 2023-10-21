''' Goes through a file and sees the frequency of the letters that pop up in the file '''

import string

y=list()

thing=dict()

file=input("Enter your file\n")

fhand=open(file)

for line in fhand:
    line=line.strip()
    line=line.translate(str.maketrans("","",string.punctuation))
    line=line.lower()
    line=line.split()
    for word in line:
        for letter in word:
            thing[letter]=thing.get(letter,0)+1
print(thing)
x=list(thing.items())

for (letter,freq) in x:
    y.append((freq,letter))

y.sort(reverse=True)

for (freq,letter) in y:
    print(str(freq)+" "+letter)
