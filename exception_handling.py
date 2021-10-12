# try:
#   print(x)
# except NameError as e:
#   print(e)
# except:
#   print("Something else went wrong")

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The 'try except' is finished")