ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()

print(ages)

min_age = min(ages)
max_age = max(ages)

print("Min age is:",min_age)
print("Max age is:",max_age)

ages.insert(5, min_age)
ages.insert(8, max_age)

print(ages)
lenage = len(ages)
mid = lenage // 2
if lenage % 2 == 1:
    median_age = ages[mid]
else:
    median_age = (ages[mid - 1] + ages[mid]) / 2

print("Median age is:",median_age)
print("Length of age is:",lenage)

avg_age = sum(ages) / lenage
print("Average age is:",avg_age)

r_ages = (max_age - min_age)
print("Range of age:",r_ages)

cmp = abs(min_age - avg_age)
cmp1 = abs(max_age - avg_age)
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

print("First half of countries:", first_half)
print("Second half of countries:", second_half)

countries1 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

first_country, second_country, third_country, *scandic_countries = countries1

print("First country:", first_country)
print("Second country:", second_country)
print("Third country:", third_country)
print("Scandic countries:", scandic_countries)
