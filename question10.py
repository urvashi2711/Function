# : Write a Python function that takes a list and returns a new list with unique elements of the first list.
#Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]

def unique(lst):
    a=[]
    for i in lst:
        if i not in a:
            a.append(i)
        else:
            pass
    return a
list=eval(input("Enter the List"))
print(unique(list))