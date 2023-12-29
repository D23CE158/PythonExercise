# Exrecise 1
l1 = []
l2 = [1,2,3,4,5,6]
print(len(l1))  #print the length of l1
print(len(l2))  #print the length of l2
print(l2[0])    #print the first element of l2
print(l2[3])    #print the middle element of l2
print(l2[5])    #print the last element of l2

mixed_data_types = ["Yash",20,5.12,False,"Junagadh"]
print(mixed_data_types)

it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
print(it_companies) #print all the companies
print(len(it_companies))    #print length of list
print(it_companies[0])      #print the first element of list
mid = len(it_companies) // 2
print(it_companies[mid])    #print the middle element of list
print(it_companies[-1])     #print the last element of list
it_companies[2] = "Infosys" #Modify the name of company at index 2
print(it_companies)
it = "TCS"
it_companies.append(it)     #add TCS to the existing list using append
print(it_companies)
c1 = "Wattsap"
it_companies.insert(mid,c1) #add wattsap to the middle of the list
print(it_companies)

company_to_change = "Google"
index_to_change = it_companies.index(company_to_change)
if company_to_change != "IBM":
    it_companies[index_to_change] = company_to_change.upper() #covert Google to Upper case
print(it_companies)
joined_it = ' #'.join(it_companies) #concate string with every element of list
print(joined_it)
if 'IBM' in it_companies:
    print("IBM is at ",it_companies.index("IBM")) #print the index of IBM if it is in the list

it_companies.sort()     #sort the list
print(it_companies)

it_companies.reverse()  #reverse the list
print(it_companies)

first_three = it_companies[:3]  #print first three element
print(first_three)

last_three = it_companies[-3:]  #print last three element
print(last_three)

print(it_companies[mid])    #print the middle element

it_companies.pop(0)     #remove the first element
print(it_companies)

it_companies.pop(mid)   #remove the mid element
print(it_companies)

it_companies.pop(-1)    #remove the last element
print(it_companies)

it_companies.clear()    #clear all the data of list
print(it_companies)

del it_companies    #delete the list

front_end = ["HTML","CSS","JS","REACT","REDUX"]
back_end = ["NODE","EXPRESS","MONGODB"]
join = front_end + back_end     #concate the both list
print(join)

print(len(front_end))
full_stack = join.copy()        #copy the list in fullstack
full_stack.insert(5,"Python")   #add python at index 5
full_stack.insert(6,"SQL")      #add sql at index 6
print(full_stack)