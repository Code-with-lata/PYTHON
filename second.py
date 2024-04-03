#STRING

#write a program to input user's first name &print its length
a=str(input("enter your name "))
print("Length of your name is", len(a))

#WAP to find the occurrence of '$' in a string
str= "Hi,$ I am the $ symbol $ 99.99 "
print(str.count("$"))

##CONDITION STATEMENT

#WAP to check if a num entered by the user is odd or even

a=int(input("Enter the number"))
if(a%2==0):
    print("Even")
else:
    print("Odd")  

#WAP to find the greatest of 3 number entered by the user

a=int(input("Enter first num: "))
b=int(input("Enter second num: "))
c=int(input("Enter third num: "))
if(a>b and a>c):
    print("Greatest no is a")
elif(b>c):
    print("greatest num is b")
else:
    print("Greatest no is c")    

#WAP to check if a number is a multiple of 7 or not

a=int(input("Enter the number"))
if(a%7==0):
    print("Multiple of 7")
else:
    print("Entered num is not a multiple of 7")    