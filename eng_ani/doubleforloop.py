'''dia="aAA"
stones="aAAbbbb"
cou=0
for i in range(len(dia)+1):
    for j in range(len(stones)+1):
        if i in j:

            cou=cou+1
            print(cou)'''
'''li=[1,3,4,5,6,7,-1,-2]
c=0
for i in range(len(li)):
    d=li[i]
    if d<c:
        print(li[i])'''
x=123
d=str(x)
e=""
#print(type(d))
for i in range(len(d)-1,-1,-1):
    print(d[i],end="")
