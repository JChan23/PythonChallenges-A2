#Write a program to convert to (and from) roman numerals. So your program should be able to take the input of 27 and return XXVII, and take MCMLXXXI and return 1981. And of course any other values. The program must work for all numbers between the upper bound of 4000 and the lower bound of 0 (both non-inclusive)
#This program requires the external module "roman". It can be installed by using: $ pip install roman

import roman

type = input('Would you like to convert a Roman or Normal number? ')
if type == 'roman':
    romannumeral = input('Please enter your Roman numeral: ')
    number = roman.fromRoman(romannumeral)
    print(number)
elif type == 'normal':
    number = int(input('Please enter your number: '))
    romannumeral = roman.toRoman(number)
    print(romannumeral)
else:
    print("Error. Please enter either 'normal' or 'roman'")
