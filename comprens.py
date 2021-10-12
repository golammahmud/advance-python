'''list compresions'''
list_1=[12,32,43,55,565,3,2,4,4,5,2,67,8,9,45,454,56,534,6]
name=['r','M','g']
# div_2=[]
# for i in list_1:
#     if i%2==0:
#         div_2.append(i)
# print('thes value are divided into 2',div_2)
# print('thes value are divided into 2',[item for item in list_1 if item%3==0])
# list_comp=[item*2 for item in list_1 if item%3==0]
# print(list_comp)


# print([i.lower() for i in name ])
'''dict compresions'''

# dict1={'a':34,'b':45,'A':67}
# # print({k.upper():dict1.get(k.lower(),0)+dict1.get(k.upper(),0) for k in dict1.keys()})
# print({k.upper():dict1.get(k.lower(),0)+dict1.get(k.upper(),0) for k in dict1.keys()})

print([x**2 for x in list_1 if x%2==0])


'''generator comprensions'''

gen=(i for i in range(100) if i%3==0)
for i in gen:
    print(i)