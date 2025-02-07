'''def addition (a,b):
    print(a+b)
addition(2,5)
addition(2,7)'''
'''def addition(*num):
    for i in num:
     print(num,end="")
addition(1,2,3,9,10)'''
def info(*rank,**data,):
    for i ,j in data.items():
        print(i,j)
    print(rank)
info(22,name="deepika",dept="ai&ds",age=21)
info(21,name="sravya",dept="cse")

