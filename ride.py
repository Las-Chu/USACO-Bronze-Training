'''
ID: lctvchu1
LANG: PYTHON3
PROG: ride
'''
import os

#reading input file: ride.in
in_file = open('ride.in', 'r')
#for a_line in in_file:
    #print(a_line)
str_list = in_file.readlines()

    
str_group1 = str_list[0]
str_ufo1 = str_list[1]
#str_ufo1 = 'COMETQ'
#str_ufo2 = 'ABSTAR'


def calculation(my_string):  
    prod_g1 = 1
    for i in my_string:
        n = ord(i)-64
        prod_g1 = prod_g1*n
    return prod_g1


g1 = calculation(str_group1)
#g2 = calculation(str_group2)
ufo1 = calculation(str_ufo1)
#ufo2 = calculation(str_ufo2)

#print(g1, ufo1, g2, ufo2)
#print(g1%47, ufo1%47, g2%47, ufo2%47)


if g1%47 == ufo1%47:
    out = 'GO\n'
else:
    out = 'STAY\n'
    
#if g2%47 == ufo2%47:
    #print('GO')
#else:
    #print('STAY')
out_file = open('ride.out', 'w')
out_file.write(out)
out_file.close()
