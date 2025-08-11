mes=input("Enter a message: ")
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscibe this"
p4 = "click this"

if((p1.lower() in mes.lower()) or (p2.lower() in mes.lower()) or (p3.lower() in mes.lower()) or (p4.lower() in mes.lower())):
    print("It contains SPAM")

else:
    print("No SPAM")

