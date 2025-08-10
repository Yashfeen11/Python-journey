
a=input("Enter the name:")
b=int(input("Enter the date:"))
print(f"\'\'\'\nDear <|{a}|>,\nYou are selected!\n<|{b}|>\n\'\'\'")
letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|>'''
print(letter.replace("Name","Yashfeen").replace("Date","26 May"))