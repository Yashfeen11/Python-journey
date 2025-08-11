s1=input("Enter the subject 1:")
s2=input("Enter the subject 22:")
s3=input("Enter the subject 3:")
ms1=int(input("Enter the marks in s1:"))
ms2=int(input("Enter the marks in s2:"))
ms3=int(input("Enter the marks in s3:"))
t1=(ms1+ms2+ms3)/3
print(t1)
if(t1>40 and ms1>33 and ms2>33 and ms3>33):
    print("Passed")

else:
    print("Failed")

 