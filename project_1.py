print("****Welcome to Calculator****")

num1=float(input("enter first number:"))
print("the first numnber is:",num1)
num2=float(input("enter second number:"))
print("the second number is:",num2)
operator=input("enter the operator:")

if(operator=='+'):
    print("the addition of",num1,"and",num2,"is:",num1+num2)
elif(operator=='-'):
    print("the subtraction of",num1,"and",num2,"is:",num1-num2)
elif(operator=='*'):
    print("the multiplication of",num1,"and",num2,"is:",num1*num2)
elif(operator=='/'):
    print("the division of",num1,"and",num2,"is:",num1/num2)
else:
    print("please enter a valid operator!!!")



