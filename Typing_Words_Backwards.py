''' Types the given word Backwards '''

word=input("Please type your word\n")

a=len(word)

index=a

while index>=0:
    index=index-1
    print(word[index])
