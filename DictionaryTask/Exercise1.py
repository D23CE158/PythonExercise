dog = {}
dog = {
    'name':'puppy',
    'color':'black',
    'breed':'lab',
    'legs':'black',
    'age':5
}
student = {
    'f_name':'namya',
    'l_name':'oza',
    'gender':'male',
    'age':18,
    'marital_status':'non_married',
    'skills':'playing tabla',
    'country':'India',
    'city':'Junagadh',
    'address':'Vanzari chowk'
}
print(len(student))
print(student.get('skills'))
l = list(student)       #convert dictionary to list
print(type(l))
student['skills'] = 'playing vollyball'     #modify skill
print(student.get('skills'))
print([student.keys()])     #get all keys as a list
print([student.values()])   #get all values as a list
print(student.items())      #get all items as a list of tuples
print(student.pop('address'))   #delete address
print(student)
del dog     #delete dog dictionary

