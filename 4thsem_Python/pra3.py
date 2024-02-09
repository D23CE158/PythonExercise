# A:String Operation

s = "Hello World"
s1 = "!Good Morning"
print(s[::-1])
print(s.replace("World","All"))
print(s + s1)
if "H" in s:
    print(s.index("H"))
else:
    print("No in string")
print(s.split())

# B:Dictionary Operations

student = {
    'name' : 'rohan',
    'age' : 20,
    'grade' : 'AA'

}
student.update({'grade' : 'BB'})
print(student)
del student['age']
print(student)
student.popitem()
print(student)
# student.pop('grade')
print(student)
student.get('name')
print(student)
print(student.items())
print(student.items())

# 2

dict1 = {
    'a' : 1,
    'b' : 2
}
dict2 = {
    'c' : 3,
    'd' : 4
}
dict3 = {
    'e' : 5,
    'f' : 6
}
merged_dict = {**dict1,**dict2,**dict3}
print(merged_dict)