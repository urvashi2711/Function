# Define a function which counts vowels and consonant in a word.

def count(str):
  a="AEIOUaeiou"
  v=0
  c=0
  for i in str:
    if i in a:
      v=v+1
    else:
      c=c+1
  print("Vowels :",v,"Consonant :",c)
s=input("Enter the String")
count(s)