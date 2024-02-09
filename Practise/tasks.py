#  String

# 1
s = "Hello World"
print(s[::-1])

# 2
print(s.replace("World","All"))

# 3
if "H" in s:
    print(s.index("H"))

# 4
tup = ("h","e","l","l","o")
str = " ".join(tup)
print(str)

li = ["1","2","3","4","5"]
str = " ".join(li)
print(str)

sets = set()
sets.add("2")
sets.add("5")
sets.add("8")
str = " ".join(sets)
print(str)

# 5
print(s.upper())
print(s.lower())
print(s.split())

# 6
print("Tuple",max(tup))
print("Tuple",min(tup))
print("Tuple",len(tup))
tup1 = (1,2,3,4)
print("Tuple",sum(tup1))

print("List",max(li))
print("List",min(li))
print("List",len(li))
li1 = [1,2,3,4]
print("List",sum(li1))

# 7
li2 = li + li1
print(li2)

# 8
student = {
    'name' : 'rohan',
    'age' : 20,
    'grade' : 'AA'
}
print(student.values())
print(student.get('age'))
student['age'] = 18
print(student.get('age'))
student.update({'grade' : 'BB'})
print(student)
if 'gender' in student:
    print("Yes")
else:
    print("No")

# 9
set1 = set()
set2 = set()
set1.add(1)
set1.add(2)
set1.add(3)
print(set1)
set2.add(3)
set2.add(4)
set2.add(5)
print(set2)

su = set1.union(set2)
su2 = set2.union(set1)
print(su)
print(su2)

si = set1.intersection(set2)
si2 = set2.intersection(set1)
print(si)
print(si2)

sd = set1.difference(set2)
print(sd)

ss = set1.issubset(set2)
print(ss)

# 10
mathset = set()
mathset.add('Rutik')
mathset.add('Vishal')
scienceset = set()
scienceset.add('Rutik')
scienceset.add('Utsav')

subjects = {
    'maths' : mathset,
    'science' : scienceset
}
print(subjects)
mathset.add('Nehit')
subjects.update({'maths' : mathset})
print(subjects.get('maths'))

scienceset.remove('Utsav')
subjects.update({'science' : scienceset})
print(subjects.get('science'))

common = mathset.intersection(scienceset)
print("Common student is",common)

country = {
    'India' : {
        'City' : 'Junagadh',
        'Population' : '15 lakh'
    },
    'USA' : {
        'City' : 'NewYork',
        'Population' : '20 lakh'
    }
}
print(country)

# 11
l = [1,2,3,4,5,6,7,8,9,10]
# str(l)
odd = []
even = []
for i in range(0,len(l)):
    if i % 2 == 0:
        odd.append(l[i])
    else:
        even.append(l[i])

# sep = odd + even
print("Even Values",even)
print("Odd Values",odd)

# 12
a = 5
b = 8
tup = (a,b)
b,a = tup
print('a:',a)
print('b:',b)

# 13
s1 = [1,2,3,2,1]
if s1 == s1[::-1]:
    print("Yes it is pelindrom")
else:
    print("No it is pelindrom")

# 14
tup1 = (1,2,3,4)
tup2 = (5,6,7,8)
lst1 = list(tup1)
lst2 = list(tup2)
lst1.extend(lst2)
concate = tuple(lst1)
print(concate)



