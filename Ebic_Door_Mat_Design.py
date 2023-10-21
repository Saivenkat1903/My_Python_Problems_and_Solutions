
''' Hackerrank door mat design problem https://www.hackerrank.com/challenges/designer-door-mat/problem '''

holder=".|."

data=input()

n=data.split()[0]
N=int(n)
M=3*N
useful=int((N+1)/2)  #4

for i in range(useful):
    random1=int(((M-3)/2)-3*i)
    if i!=(N+1)/2-1:
        x="-"*random1+holder*(1+2*i)+"-"*random1
        x.replace(" ", "")
        print(x)
    if i==useful-1:
        y="-"*int(M/2-7/2)+"WELCOME"+"-"*int(M/2-7/2)
        y.replace(" ", "")
        print(y)

for k in range(N-useful):
    random2="-"*(3+3*k)
    random3=int((M-6-6*k)/3)
    z=random2+holder*random3+random2
    z.replace(" ", "")
    print(z)
