'''word=input("enter a string")
#print(word)
n=len(word)
add=0
for i in range(n-1):
    #print(word[i],word[i+1])
    a=ord(word[i])
    #print(a)
    b=ord(word[i+1])
    #print(b)
    temp=abs(a-b)
    add=add+temp
    print(add)'''


class Solution:
    def scoreOfString(self, s: str) -> int:
        d = 0
        for i in range(len(s) - 1):
            a = ord(s[i])
            b = ord(s[i + 1])
            c = abs(a - b)
            d = d + c
            return d
scoreOfString("hello")

