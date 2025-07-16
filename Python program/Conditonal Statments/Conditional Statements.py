# if statements for Age 

age = int(input("What is your Age:"))

if(age >= 18):                                                 # We can write n number of if(): and elif(): statements
    print("Can Vote and apply for Driving License")
    print("Can Also Drive Electircal Motorcycles")             # indentation is the proper spacing in the code
    
elif(age >= 16):                                               # The diffrence b/w if and elif statements is that if statements is always checked and elif statements are only checked when if statements is false
    print("Can only Drive Electircal Motorcycles")     
                                                       
else:
    print("Not Elegible for Both voting and license")           # else: statements runs only when all the statements checked above are false 


# if statements for Marks

marks = int(input("What is total marks:"))

if(marks >=90):
    grade = "A"
elif(marks>=80 and marks< 90):
    grade = "B"
elif(marks>=60 and marks<80):
    grade = "C"
elif(marks<=60):
    grade = "D"

print("Grade of the student is -> ",grade)

# Nesting   

age = int(input("What is your Age:"))          # When we use many if(): statements under one if(): statement then it is know as Nesting 

if(age >= 18):
    if(age>= 80):
        print("Cannot Drive")
    else:
        print("Can Drive")
else:
    print("Cannot drive")
                                                                                                                                                                                         