'''s="abcd"
ans=""
ans=ans+s[3]
ans=ans+s[2]
ans=ans+s[1]
ans=ans+s[0]
print(ans,end="")'''
'''s="abcd"
ans=""
for i in range(3,-1,-1):
    ans=ans+s[i]
print(ans)'''
'''user=list(input("enter a list"))
li=[]
li.append(user)'''
'''li=[1,3,5,6,7,9]
n=len(li)
for i in range(n-1,-1,-1):
    print(li[i],end="")'''
'''a=input("enter a string:")
n=len(a)
ans=""
for i in range(n-1,-1,-1):
    ans=ans+a[i]
    print(ans)
if a==ans:
    print("palindrome")
else:
    print("not")'''
a="abba"
n=2
y=len(a)
for i in range(n):
print(a[i],a[y-1])
print(a[i+1],[y-2])
print(a[i+2],a[y-3])
