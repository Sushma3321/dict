list=[1,2,3,6,7,3,4]
n=9
i=0
a=[]
while i<len(list):
    j=i+1
    while j<len(list):
        if list[i]+list[j]==n:
            c=[i,j]
            a.append(c)
        j=j+1
    i=i+1
print(a)


