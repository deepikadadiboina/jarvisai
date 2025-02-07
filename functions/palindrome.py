word=input("enter a string")
n=len(word)//2
mul=n*2
for i in range(n):
    print(word[i],word[mul-1-i])
    a=word[i]
    b=word[mul-1-i]
if a==b:
    print("palindrom")
else:
    print("not a palindrome")
