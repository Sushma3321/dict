# Write a program to remove duplicate keys.


dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
dict1={}
for i in dic:
    if dic[i] not in dict1:
        dict1[i]=dic[i]
print(dict1)