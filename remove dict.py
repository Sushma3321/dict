# CAR_DETAILS={"brand": "Ford","model": "jason","year": 1964}
# CAR_DETAILS.pop("model")
# print(CAR_DETAILS)


# Write a program remove the first key value pair from a nested dictionary.


dic= {1: 'NAVGURUKUL',2: 'IN',  3:{"A":'WELCOME','B' : 'To','C' : 'DHARAMSALA'}}
# del(dic[1])
del(dic[3]["A"])
# dic.pop(1)


print(dic)



