'''
Lab 5 (if statement)
'''

#5.1

alien_color = "green"
if alien_color == "green":
    print('you just earned 5 points')

#5.2

alien_color = "red"
if alien_color == "green":
    print('you just earned 5 points')
    
else:
     print('you just earned 10 points')
     
#5.3

favorite_fruits = ['watermelon','pineapple','banana']

if 'watermelon' in favorite_fruits:
    print('you really like watermelon')
    
if 'pineapple' in favorite_fruits:
    print('you really like pineapple')
    
if 'banana' in favorite_fruits:
    print('you really like banana')
    
#5.4

age = 19

#if age < 10:
#    print('you are a kid')
#elif age < 20:
#    print('you are a teenager')
#else:
#    print('you are an adult')
#    if age > 65:
#        print('you are an elder')

if age >= 20:
    print('you are an adult')
    if age > 65:
        print('you are an elder')
elif age >= 10:
    print('you are a teenager')
else:
    print('you are a kid')
    