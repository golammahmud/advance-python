# Python program to validate an Email

# import re module

# re module provides support
# for regular expressions
import re

# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Define a function for
# for validating an Email


# def check(email):

# 	# pass the regular expression
# 	# and the string into the fullmatch() method
# 	if(re.fullmatch(regex, email)):
# 		print("Valid Email")

# 	else:
# 		print("Invalid Email")


# # Driver Code
# if __name__ == '__main__':

# 	# Enter the email
# 	email = "ankitrai326@gmail.com"

# 	# calling run function
# 	check(email)

# 	email = "my.ownsite@our-earth.org"
# 	check(email)

# 	email = "ankitrai326.com"
# 	check(email)


 
import re
email="arpit.mandliya@gmail.com"
def isValid(email):
 if(re.match("^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$", email) != None):
     print(email)
     return True
 return print('email is invalid')
isValid(email)
# if(isValid() == True):
#  print("This is a valid email address")
# else:
#  print("This is not a valid email address")





txt = "The rain yuiyui uuy uyy uy9y898y  y7y7u in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
