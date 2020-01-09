# simple python string test.
setence = 'this is Mukesh'
print(setence)

# slicing ::- You can return a range of characters by using the slice syntax.
print('output of array of string :: ' + setence[0:])
print('output of array of string :: ' + setence[1:-1])

# testing of string funtions..
print('-----------------------------------------')
first_name = 'Mukesh'
last_name = 'Pant'
print(first_name + last_name)
message = f'{ first_name} [{last_name}] is a coder'
print(message)
print("Length of message:: ", + len(message))
print("UPPERCASE LETTER message:: ",  message.upper())
print("lowercase message:: ", message.lower())
# strip() - this method removes white spaces from the string value.
new_name = " Ravi Singh "
print(new_name.strip())
print(new_name.split("."))

print('=============some more functions==========================')
print(first_name.find('h'))
print(first_name.replace('Mukesh', 'Rohit'))

# check the value of string if it is present in the expression/ variables
msg = 'Python course for absolute beginners'
print('Python' in msg)

print('Py' 'thon')

print('=======================================')



