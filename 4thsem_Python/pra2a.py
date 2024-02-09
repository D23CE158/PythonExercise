# 2(a)
a = [1,2,3,4,5,6,7,8]
a.append(9)
print(a)
a.extend([6,8,9])
print(a)
a.remove(3)
print(a)
a.reverse()
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)

# 2(b)

list1 = [1,2,3,4,['python','java','c++',[10,20,30]],5,6,7,['apple','banana','orange']]
orange = list1[-1][-1]
python = list1[4][0].capitalize()
print("Orange:",orange)
print("Python:",python)
repetelist = [list1] * 5
for lst in repetelist:
    print(lst)

# 2(c)

lst1 = [1,2,3,4]
clist = lst1[:]
clist.append(6)
print(lst1)
print(clist)

# 2(d)

tup1 = (1,2,3,4,5,6,7,8,9,10)
print(sum(tup1))
print(max(tup1))
print(min(tup1))