#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
belgium_length = len(Belgium)
# print('Belgium string length =', belgium_length)
# dash_list = ['-',]
# for number in range(1, belgium_length):
#     dash_list.append("-")
# print('dash_list length =', len(dash_list))
dash_string = ''
for i in range(len(Belgium)):
    dash_string += '-'
print(dash_string)
print('\n', Belgium.replace(',', ':'))
# belgium_list is being created and assigned values after splitting the string Belgium
# wherever there was a comma
belgium_list = Belgium.split(',')
# print(10445852 + 737966)
print(f'The sum of the first two numbers in string = {int(belgium_list[1]) + int(belgium_list[3])}')
# slices before 1 and before 4 in steps of 2
print(f'List of first two numbers in string = {belgium_list[slice(1, 4, 2)]}')
