num = int(input("Enter a Number:\n"))
if(num%2==0 and num>0):
    print(num," is even & positive!!")
elif(num%2==0 and num<0):
    print(num," is even & negative!!")
elif(num%2==1 and num>0):
    print(num," is odd & positive!!")
elif (num % 2==1 and num<0):
    print(num, " is odd & negative!!")
