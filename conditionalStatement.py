is_hot = False
is_cold = True

if is_hot:
    print('it''s hot day')
    print('drink plenty of water')
elif is_cold:
    print('it''s cold day')
    print('Wear warm clothes')
else:
    print('It''s lovely day')

print("Enjoy your day")
print('----------------------------------------------')
print('----------------------------------------------')

house_price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * house_price
else:
    down_paymet = 0.2 * house_price
print(f" Down Payment:  $ {down_payment}")

x = 100
print("Global variable", x)
del x
print('-------------------Print the largest number of three---------------------------')

num1 = int(input("Enter the num1"))
num2 = int(input("Enter the num2"))
num3 = int(input("Enter the num3"))

if num1 > num2 and num1 > num3:
    print("num1 is the largest number")
if num2 > num1 and num2 > num3:
    print("num2 is the largest number")
else:
    print("num3 is largest number.")

# checking elif statement..
print('-------------------Checking the elif statement----------------------------')
number = int(input("pls Enter any number to check the availability"))
if number>1 and number <= 20:
    print("number is between 1 & 20")
elif number>21 and number<= 40:
    print("number is between 21 & 40")
elif number>41 and number<= 60:
    print("number is between 41 & 60")
elif number>61 and number<= 80:
    print("number is between 61 & 80")
elif number>81 and number<= 100:
    print("number is between 81 & 100")

else:
    print("number is out of the range!!! pls enter number between 1 to 100")
