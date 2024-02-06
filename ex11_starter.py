#!/usr/bin/python
# Week 3 homework - Exercise 11

# The Belgium string declared below was provided in the homework as a starter.
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# Homework part 1.
# To create a string of dashes equal to the length of Belgium string and print it.
# starting with getting the length of Belgium string
belgium_length = len(Belgium)
print(f'\n Belgium string length = {belgium_length}')
# creating a variable dash_string and assigning it a blank value
dash_string = ''

# .join Method
# Following loop runs for number i in range 0 to length of Belgium and adds one dash '-' each time to dash_string
# at the end of the loop the dash_string is printed
for i in range(len(Belgium)):
    # dash_string += '-'
    dash_string += ''.join('-')
print(dash_string)
print(f'{'':<1}dash strings printed above and below are of length = {len(dash_string)}')
# {'':<1} adds padding to the left hand side of the screen

# Alternative Method 2
dash_string2 = '-' * len(Belgium)
print(dash_string2)

# Homework part 2.
# To replace commas in the string with colons
# replacing characters in a string - replace() method is used on the string
print("\n Printed below is the Belgium String with each comma replaced with a colon...")
print(f"{'':<0}", Belgium.replace(',', ':'))
print("\n Printed below is the original Belgium String (remained unchanged)...")
print(f"{'':<0}", Belgium)
print("\n Printed below is the Belgium String with each comma replaced with a forward slash...")
print(f"{'':<0}", Belgium.translate(str.maketrans(',', '/')))
# .translate is used for more complex string manipulations
# ([target],[replacement], [omit chosen character])

# Homework part 3.
# Add the first two numbers (populations) in the string.
# belgium_list is being created and assigned values after splitting the string Belgium at all the commas
belgium_list = Belgium.split(',')
print("\n Belgium string split into list:\n", belgium_list)
print(f"\n The sum of first two numbers should be 10445852 + 737966 = {10445852 + 737966}")

# Following line of code slices belgium_list between 1 and 4 in steps of 2 i.e. slices out elements
# belgium_list[1] and belgium_list[3]
print(f'\n{'':<1}List of first two numbers in string =  {belgium_list[slice(1, 4, 2)]}')
# adding belgium_list[1] and belgium_list[3]
print(f'Sum is same as of belgium_list[1] and belgium_list[3] = {int(belgium_list[1]) + int(belgium_list[3])}')

# Alternatively, slicing the string directly without using list and doing the addition shows same result
print(f"{'':<1}Using alternative approach to slice the strings directly, the sum is the same...")
print(f'{'':<0} {int(Belgium[8:16]) + int(Belgium[26:32])}')
