# Store the unique letters and their frequency of the letters from the word "MISSISSIPPI" to a dictionary, were the letters are the keys and their frequencies are the values.
a="MISSISSIPPI"
i=0
c=0
b={}
while i<len(a):
    d=a.count(a[i])
    b[a[i]]=d
    i=i+1
print(b)


