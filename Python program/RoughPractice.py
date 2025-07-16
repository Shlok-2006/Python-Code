# Input 2 numbers and Find its Sum

val1 = int(input("Input first number:"))
val2 = int(input("Input second number:"))

sum = val1 + val2

print("Sum: " , sum )

# My mistake here: for finding Sum the val1 and val2 should be an integer. So put val1 = int() and val2 = int()
# Reason: Because input() always gives a string result 



# Input the Side of a Square and Calulate its Area

a = int(input("Enter side of Square: "))

print("Area of Square: ", a * a)  # a * a or a ** 2 are same

# My mistake here: NO



# Input 2 floating point numbers and Print its Average

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

Sum = a + b

print("Average: ", Sum/2 )  #  (a+b)/2 also can be used instead of Sum/2

# My mistake here: NO



# Input 2 int number a and b . Print True if a is greater than or equal to b. If not print Flase

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))


print(a >= b)

# My mistake here: I forgot how the function print(a >= b) works



#Input users First name and print its Length

str = input("Enter your First Name:")

print("Length of your name:" ,len(str))

# My mistake here: Had to recheck length function 



# Find the occurrence of "S" in a string

str1 = "she sells sea shells on the sea shore"

print(str1.count("s"))

# My mistake here: NO

# Write a program(WAP) to check if a number entered by the user is odd or even

num = int(input("Enter a number: "))

if(num % 2 == 0):
   print("Number is even")
else:
   print("Number is odd")

# My mistake here: I forgot reminder operation


# WAP to find the greatest of 3 number entered by the user

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if(a >= b and a >= c):
    print("Greatest number is :" , a)
elif(b >= c):
    print("Greatest number is :" , b)
else:
    print("Greatest number is:", c)

#My misatke here:  Forgot to aline everything and forgot the elif statement

# WAP to check if a number is a multiple of 7 or not

x = int(input("Enter a number:"))

if(x % 7 == 0):
    print("The number is divisible by 7")
else:
    print("The number is not a multiple of 7")


