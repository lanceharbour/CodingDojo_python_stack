#1
def biggie_size(x):
    for i in range(0,len(x)):
        if x[i] > 0:
            x[i] = "big"
    return x
y = biggie_size([-1,3,5,-5])
print(y)

#2
def count_positives(x):
    count = 0
    for i in range(0,len(x)):
            if(x[i] > 0):
                count += 1
    x = x[:-1]
    x.append(count)
    print(x)
count_positives([-1,1,1,1])

#3
def sum_total(x):
    sum = 0
    for i in range(0,len(x),1):
        sum = sum + x[i]
    return sum
y = sum_total([6,3,-2])
print(y)

#4
def average(x):
    sums = 0
    count = 0
    for i in range(0,len(x)):
        sums = sums + x[i]
        count += 1
    avg = sums/count
    return avg
y = average([1,2,3,4])
print(y)

#5
def length(x):
    return len(x)
y = length([])
print(y)

#6
def minimum(x):
    min = 0
    if not x:
        x = 'False'
        return x
    else:
        for i in range(0,len(x)):
            if x[i] < min:
                min = x[i]
    return min
y = minimum([])
print(y)

#7
def maximum(x):
    max = 0
    if not x:
        x = 'False'
        return x
    else:
        for i in range(0,len(x)):
            if x[i] > max:
                max = x[i]
    return max
y = maximum([37,2,1,-9])
print(y)

#8
def ultimate_analysis(x):
    count = 0
    total = 0
    sums = 0
    min = 0
    max = 0
    length = 0
    #min, max
    if not x:
        x = 'False'
        return x
    else:
        for i in range(0,len(x)):
            if x[i] < min:
                min = x[i]
        for i in range(0,len(x)):
            if x[i] > max:
                max = x[i]
    #length of x
    length = len(x)
    #total and avg 
    for i in range(0,len(x)):
        sums = sums + x[i]
        count += 1
    total = sums
    avg = sums/count
    x = ({'sumTotal':total,'average':avg,'minimum': min,'maximum':max,'length':length})
    return x
y=ultimate_analysis([37,2,1,-9])
print(y)

#9
def reverse_list(x):
    a = len(x)
    for i in range(a-1, -1, -1):
        x.append(x[i])
    while a > 0:
        x.pop(0)
        a -= 1
    return x
y = reverse_list([37,2,1,-9])
print(y)