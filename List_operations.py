''' First time messing around with list operations '''

final=list()

useful=dict()

useful["insert"]="final.insert(int(i[1]),int(i[2]))"
useful["print"]="print(final)"
useful["remove"]="final.remove(int(i[1]))"
useful["append"]="final.append(int(i[1]))"
useful["sort"]="final.sort()"
useful["pop"]="final.pop()"
useful["reverse"]="final.reverse()"

thing=list()

N = int(input())

for i in range(N):
    j=input()
    thing.append(str(j))

for k in thing:
    i=k.split()
    x=useful.get(i[0],None)
    exec(x)
