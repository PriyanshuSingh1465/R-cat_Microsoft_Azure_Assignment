list1=[1,2,3,4,5,6,7,8,9,10]
list2 = [x**2 for x in list1 if x % 2 == 0]
print(list2)


# output :
# [4, 16, 36, 64, 100]