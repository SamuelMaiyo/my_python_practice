# strings: ordered, immutable, text representation

my_string = "I'm a programmer"
print(my_string)

my_string = """I'm a 
programmer"""
print(my_string)    # Used for multiline strings


stringA = "Hello World"
char = stringA[0]
print(char)

substring = stringA[1:8] # Slicing
print(substring)

substring = stringA[::2] # Step
print(substring)

substring = stringA[::-1] # Reverse String
print(substring)

# Concatenate String
greeting = "Hello"
name = "Tom"

sentence = greeting + " " + name
print(sentence)

# Iterate string
greeting = "Hello"
for i in greeting:
    print(i)

if "e" in greeting:
    print('yes')
else:
    print('no')

# Remove white space
stringB = '    Hello Mike     '
print(stringB)

stringB = stringB.strip()
print(stringB)

print(stringB.upper())
print(stringB.lower())
print(stringB.startswith("Hello"))
print(stringB.startswith("L"))
print(stringB.endswith("E"))

print(stringB.find("p")) # Find index of letter

#Replace char in String
print(stringB.replace("Hello", "Hi"))

# Convert string to list
stringC = "How are you doing ?"
my_list = stringC.split()
print(my_list)

new_string = ''.join(my_list)
print(new_string)


listA = ['a']*6 
print(listA)
new_string_A = ''
for i in my_list:
    new_string_A += i
print(new_string_A)

# Format strings
var = "Tom`"
stringD = "The variable is %s" % var
print(stringD)

var = 3.1427865
stringD = 'The variable is %f' % var
print(stringD)

var = 3.1427865
stringD = 'The variable is %.2f' % var # returns 2 decimal places
print(stringD)

var = 3.1427865
stringD = 'The variable is {}'.format(var)
print(stringD)

var = 3.1427865
var2 = 789
stringD = f"The variable is {var} and {var2}"
print(stringD)