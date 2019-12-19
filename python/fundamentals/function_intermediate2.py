#1
def changeX(y):
    x = [[5,2,3],[10,8,9]]
    x[1][0]=y
    print(x)
changeX(15)

def changeLastName(last_name):
    students = [
        {'first_name': 'Michael', 'last_name': 'Jordan'},
        {'first_name': 'John', 'last_name': "Rosales"}
        ]
    students[0]['last_name'] = last_name
    print(students[0]['last_name'])
changeLastName("Bryant")

def changeName(first):
    sports_directory = {
        'basketball':['Kobe', 'Jordan', 'James', 'Curry'],
        'soccer':['Messi', 'Ronaldo', 'Rooney']
        }
    sports_directory['soccer'][0] = first
    print(sports_directory['soccer'][0])
changeName('Andres')

def changeVal(a):
    z = [{'x': 10, 'y': 20}]
    z[0]['y'] = a
    print(z[0]['y'])
changeVal(30)

#2
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'},
]
def iterateDictionary(list):
    p = ""
    for i in list:
        for k,v in i.items():
            print(p + k + " - " + v)
iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    # print(key_name)
    # print(some_list)
    for i in some_list:
        print(i[key_name])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(list):
    for i in list:
        print(len(list[i]), i.upper()),
        for x in list[i]:
            print(x)

printInfo(dojo)