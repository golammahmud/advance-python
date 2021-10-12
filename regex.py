# import re

# txt = "The rain in Spain 2"

# #Check if the string has any 0, 1, 2, or 3 digits:

# x = re.findall("[0123]", txt)

# print(x)

# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")




# import re

# txt = "The rain in Spain"
# x = re.search("\s", txt )

# print("The first white-space character is located in position:", x.start()) 


# import re

# txt = "hello world hell"

# #Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

# x = re.findall("^he+..o?", txt)
# print(x)


import re
email=input("Enter email address:")
def validateEmail(email):
    if re.match('\b[\w[\.-]?]+@[\w\.-]+\.\w{2,4}\b', email):
        print(email)
        
    else:
        print('invalid email address')
e=validateEmail(email)