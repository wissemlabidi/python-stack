# Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
 {'first_name': 'Michael', 'last_name' : 'Jordan'},
 {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
 'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
 'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
    #Change the value 10 in x to 15
x[1][0] = 15
print(x)
    #Change 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students)
    #change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])
    #Change the value 20 in z to 30
z [0]['y'] = 30
print(z)



# Iterate Through a List of Dictionaries
students = [
{'first_name': 'Michael', 'last_name' : 'Jordan'},
{'first_name' : 'John', 'last_name' : 'Rosales'},
{'first_name' : 'Mark', 'last_name' : 'Guillen'},
{'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(some_list):
    for dictionary in some_list:
        for key, value in dictionary.items():
            print(key,'-', value)
        output = ', '.join([f'{key} {value}' for key, value in dictionary.items()])
        print(output)

iterateDictionary(students)


# Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        if key_name in dictionary:
            value = dictionary[key_name]
            print(value)
iterateDictionary2("first_name", students)
iterateDictionary2('last_name', students)


# Iterate Through a Dictionary with List Values
dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key, value in some_dict.items():
        print(f"{key}: {len(value)}")
        for item in value:
            print(item)
        print()
printInfo(dojo)



