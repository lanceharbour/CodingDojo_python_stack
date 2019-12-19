#1
def countdown(x):
    newx = []
    for num in range(x,-1,-1):
        print(num)
        newx.append(num)
    return newx
y = countdown(5)
print(y)

#2
def print_and_return(x):
    print(x[0])
    return x[1]
print_and_return([1,2])

#3
def first_plus_length(x):
    sum = x[0] + len(x)
    return sum
y = first_plus_length([1,2,3,4,5])
print(y)

#4
def values_greater_than_second(x):
    newx = []
    for i in range(0,len(x)):
        if x[i] > x[1]:
            newx.append(x[i])
    print(len(newx))
    return newx
y = values_greater_than_second([5,2,3,2,1,4])
print(y)

#5
def length_and_value(a,b):
    newlist = []
    for i in range(0,a,1):
        newlist.append(b)
    return newlist
y = length_and_value(4,7)
print(y)