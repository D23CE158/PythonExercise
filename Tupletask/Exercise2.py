brother = ('virat','rahul','rohit','dhoni')
sister = ('gauri','pooja','tanu')
siblings = brother + sister     #join brother and sister
print(len(siblings))    #length of tuple
father = 'Prakash'
mother = 'Prakashini'
family_members = siblings + (father,mother)     #join father,mother and siblinigs
unpack = father,mother,*siblings    #unpack father,mother and siblings
print('Father = ',father)
print('Mother = ',mother)
print('siblings = ',*siblings)

fruits = ('Apple','Banana','Oranage')
vegetables = ('Potato','Tomato','Carrot')
animal = ('Cow','Horse','Dog')

food_stuff_tp = fruits + vegetables + animal    #join three tuples
food_stuff_tp_list = list(food_stuff_tp)    #convert tuple into list
print(len(food_stuff_tp_list))
mid_item = len(food_stuff_tp_list) // 2     #mid item of list
print(food_stuff_tp_list[mid_item])
print(food_stuff_tp[mid_item])
print(food_stuff_tp_list[0:3])      #first three item
print(food_stuff_tp_list[-3:])      #last three item
# del food_stuff_tp     #delete tuple
if 'Apple' in food_stuff_tp:
    print('Apple is at:',food_stuff_tp.index('Apple'))
nordic_countries = ('Denmark','Finland','Iceland','Norway','Sweden')
if 'Estonia' in nordic_countries:
    print(True)
else:
    print(False)
if 'Iceland' in nordic_countries:
    print(True)
else:
    print(False)