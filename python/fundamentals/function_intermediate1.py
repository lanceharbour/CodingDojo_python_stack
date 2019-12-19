import random
def randInt(min=0, max=0):
    if min == 0 and max == 0:
        num = random.random()
        return num
    if min == 0 and max > 0:
        num = random.random() * max
        return num
    if min > 0 and max > min:
        num = random.random() * max
        return num
    if min > 0 and max > 0:
        num = random.random() * (max-min) + min
        return num
    if min > 0 and max == 0:
        num = random.random() * 90 + min
        return num
print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50,max=500))