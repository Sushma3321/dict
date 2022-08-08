dict={1:10,2:60,3:30,5:50,4:60,5:3}
# output={10: [1], 60: [2, 4], 30: [3], 3: [5]}

i=1
a={}
c=[]
while i<=len(dict):
    a[dict[i]]=[i]
    a[dict[2]]=c
    j=i+1
    while j<len(dict):
        if dict[i]==dict[j]:
            c.append(i)
            c.append(j)
            a[dict[2]]=c
        
        j=j+1
    i=i+1
print(a)