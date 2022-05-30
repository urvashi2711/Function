# 15: Write a Python program to reverse a string.
#Sample String: "1234abcd"
#Expected Output: "dcba4321"


def reverse(str):
    f=str[-1::-1]
    return f
s=input("Enter the string")
print("Reverse String:",reverse(s))