
s=int(input())
arr=list(map(int,input().split()))
d={}
for i in arr:
    if(s-i in d):
        print(i,s-i)
        break
    d[i]=s-i
print("hello")