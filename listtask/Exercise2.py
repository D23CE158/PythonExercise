ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()     #sort the ages

print(ages)

min_age = min(ages)     #find the minimum age
max_age = max(ages)     #find the maximum age

print("Min age is:",min_age)
print("Max age is:",max_age)

ages.insert(5, min_age)     #insert minimum age at index 5
ages.insert(8, max_age)     #insert maximum age at index 8

print(ages)
lenage = len(ages)

mid = lenage // 2       #find mid age from list
if lenage % 2 == 1:
    median_age = ages[mid]
else:
    median_age = (ages[mid - 1] + ages[mid]) / 2

print("Median age is:",median_age)      #print the median age
print("Length of age is:",lenage)

avg_age = sum(ages) / lenage        #find the average age
print("Average age is:",avg_age)

r_ages = (max_age - min_age)    #find range of age
print("Range of age:",r_ages)

cmp = abs(min_age - avg_age)    #find absolute value for minimum
cmp1 = abs(max_age - avg_age)   #find absolute value for maximum
if cmp < cmp1:
    print("The absolute difference between min and average is smaller.")
elif cmp > cmp1:
    print("The absolute difference between max and average is smaller.")
else:
    print("The absolute differences are equal.")

countries = ['India','Pakistan','Australiya','South Africa','NewZelend']
mid_cou = len(countries) // 2
print(countries[mid_cou])
if len(countries) % 2 == 0:
    first_half = countries[:mid_cou]
    second_half = countries[mid_cou:]
else:
    first_half = countries[:mid_cou + 1]
    second_half = countries[mid_cou + 1:]

print("First half of countries:", first_half)  #print first half of list
print("Second half of countries:", second_half) #print second half of list

countries1 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

first_country, second_country, third_country, *scandic_countries = countries1 # find first three and all other in seperate

print("First country:", first_country)
print("Second country:", second_country)
print("Third country:", third_country)
print("Scandic countries:", scandic_countries)
