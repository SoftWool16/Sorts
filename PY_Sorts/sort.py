import random
n=int(input())
s=random.sample(range(100),n)
print(s)
i=0
while i<n-1:
    m=i
    j=i+1
    while j<n:
        if s[j]<s[m]:
            m=j
        j+=1
    s[i],s[m]=s[m],s[i]
    i+=1
print(s)