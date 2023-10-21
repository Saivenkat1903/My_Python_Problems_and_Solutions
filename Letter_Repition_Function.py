''' Counts the amount of times a specific letter gets repeated in a word '''

def count(word,a):
    var=0
    lol=0
    letter=word[lol]
    while True:
        if letter==a:
            var=var+1
            lol=lol+1
        elif letter!=a:
            var=var+0
            lol=lol+1
        else:
            print(var)
            break

kik=input("type ya word\n")

count(kik,"v")
