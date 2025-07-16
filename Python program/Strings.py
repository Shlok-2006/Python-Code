# We use single and triple upper collen because we may need to put apostrophys like sam's etc.

str1 = "My name is Shlok"
str2 = 'My age is 18'    
str3 = """I am from SRM"""



# ESCAPE SEQUENCE CHARACTERS: (Used for formating a line while coding)
#\n : used to shift to the next line.
#\t : used to give a tab sapce in between diffrent sentences.


str4 = "This is a String. \nWe are using python."  
str5 = "This is a String. \tWe are using python."
print (str4)
print(str5)



# Basic Operations
# Concatenation: Adding two strings

str6 = "Shlok"
str7 = "Agarwal"
Finalstr = str6 +" "+ str7           # Used " " in the middle to give a gap 

print(Finalstr)



# Length of string : Gives the number of characters in the letter

str8 = "Game"
len1 = len(str8)
print(len1)

str9 = "Developer"
len2 = len(str9)
print(len2)



# Indexing : Each character in a string is given a postion starting from "0"
# Example: Shlok Agarwal  then S is the "0" postion character and h is the "1" postion character and    is the "5" postion character

str10 = "Coding AI"
ch = str10[3]
ch1 = str10[5]
ch2 = str10[6]
print(ch)
print(ch1)
print(ch2)



# Slicing: We can print any part of a string by slecting the postion number
# str[starting_idx : ending_idx]   # ending_idx is not included

str11 = "Srm_Ktr"
print(str11[1 : 4])    

print(str11[1 : ])   # str[1: ] same as str[1:len(str)] that means it will slice 1 to end  postion  of string 

print(str11[ : 4])   # str[ : 4] same as str[0 : 4] that means it will slice the 0 to 4th postion of string

print(str11[-5 : -1]) # Negative Index starts from "-1" and same way the ending_idx is not included



# String Function:

str12 = "i am coding python"

print(str12.endswith("thon"))   # str.endswith()    function returns true if string ends with the substring mentioned in the brakets

print(str12.capitalize())       # str.capitalize()      function returns the first character in CAPS LOCK

print(str12.replace("o" , "a"))   # str.replace("old" , "new")   Used for replace of a letter/substring from another letter/substring. 

print(str12.find("am"))           # str.find("")    Used to find a letter/substring And If u find any NON-EXISTING letter/substring then it returns -1.

print(str12.count("q"))           # str.count("")   Used to find the number of occurences of a letter/substring



