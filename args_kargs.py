# def listofnumbers(*numbers):
#     j = 0
#     for i in numbers:
#         j = i + j
#     print(f"Sum of all numbers is {j}")

# listofnumbers(1,2,3,700,800,100,390,32809,29380,23908,283703)
# numberlist = [1,2,3,700,800,100,390,32809,29380,23908,283703]
# listofnumbers(*numberlist)

dic = {"red": "#f00",
"green": "#0f0",
"blue": "#00f",
"cyan": "#0ff",
"magenta": "#f0f",
"yellow": "#ff0",
"black": "#000",}

def dicitems(**dic):
    for color, colorcode in dic.items():
        print(f"Color code for {color} color is {colorcode}")

dicitems(**dic)

# *args and **kwargs tutorial
# *vars and **kvars tutorial

def function_1(*argsjoke):

    if(len(argsjoke) ==3):
        print("The name of the student is", argsjoke[0], "and age is",argsjoke[1], "and rollno is",argsjoke[2])
    else:
        print("The name of the student is ", argsjoke[0], "and age is ", argsjoke[1])

def printmarks(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)

def master(normal, *args, **kwargs):
    print(normal)
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print(key, value)

lis = ["harry", 22, 867656]
# function_1(*lis)
marklist = {"Harry" : 100, "rohan das":97, "Aman Bhateja": 91, "The Programmer":80,
            "Mani Verma":89, "Rajan Gupta":87, "Sanket Wankhede":90, "gaming with hunny": 76}

# printmarks(**marklist)
master("normal arg", *lis, **marklist)
