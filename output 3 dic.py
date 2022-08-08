fruit = {}

def addone(i):
    if i in fruit:
        fruit[i] += 1
    else:
        fruit[i] = 1
        
addone('Apple')
addone('Banana')
addone('apple')
addone('Apple')

print(len(fruit))
print(fruit)