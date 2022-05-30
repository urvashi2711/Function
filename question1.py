# Define a function that accepts roll number and returns whether the student is present or absent.

def rollno(n):
    a=[1,2,3,4,5,6,7,8,9,10]
    if n in a:
        return "Prsent"
    else:
        return "absent"
a=eval(input())
print(rollno(a))