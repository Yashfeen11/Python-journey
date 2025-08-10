#To detect double space and replace by single space
a=input("Enter a string:")
str=a.find("  ") #it tells the index and if not found return -1
print(str)
print(a.replace("  "," "))