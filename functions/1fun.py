'''def intro(name):
    print("hi"+name)
intro("deeps")
intro("sravys")'''

'''def gree(name,dept='me'):
    print(f"hi my name is {name}")
    print(f"i am from {dept}")
#gree("aids","deepika")
gree("deepa")'''
def mul(*num):
    c=1
    for i in num:
        c=c*i
        print(c)
mul(2,3,-6,8)
mul(2,5,8,9,0,6)
