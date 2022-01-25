def reverseArray(lst):
    lst = lst[::-1]
    print(lst)

# creating an empty list
lst = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
 
    lst.append(ele) # adding the element

reverseArray(lst)

