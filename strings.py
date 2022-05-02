mystring = "Hello World!"
ingredients ="carrots, red onion, avocado, parsley, rice"
MY_NAME = "Eudes"


# to see all posibilities to modify this string
#print(dir(mystring))


print(mystring.upper())
print(mystring.lower())
print(mystring.swapcase())
print(mystring.capitalize())

# replace

print(mystring.replace('Hello', 'Bye'))
print(mystring )
print(mystring.count('l'))
print(mystring.startswith('hola')) # False
print(mystring.startswith('hello')) # case sensitive
print(mystring.startswith('Hello')) # True
print(mystring.endswith("World!"))
print(mystring.split())
print(ingredients.split(',')) # To separate by comma
print(mystring.find('o')) # letter index position in the string
print(len(ingredients)) # lenght of the string
print(ingredients.index('red'))

print(mystring.isnumeric())

# concatenate

print(MY_NAME + " is on!")
print(f'Welcome, {MY_NAME}!') # 3.6 or above
print('Welcome, {0}!'.format(MY_NAME))