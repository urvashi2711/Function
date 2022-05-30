# : Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
#Sample String : 'The quick Brow Fox'
#Expected Output :
#No. of Upper case characters : 3
#No. of Lower case Characters : 12


def count(s):
    u=0
    l=0
    for i in s:
        if i.isupper():
            u=u+1
        elif i.islower():
            l=l+1
        else:
            pass
    print("Uppercase letters are :",u)
    print("Lowercase letters are :",l)
str=input("Enter string")
count(str)