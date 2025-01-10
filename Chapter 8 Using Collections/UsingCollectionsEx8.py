text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

#Explain why the code below prints different values on lines 3 and 4.

#The first one extracts a slice from the text ranging from 21 to 35: print(text[21:35]) and then finds 'f' from within
#slice. Whereas the second one searches for f between indexes 21 and 35 and returns 29 bc that's where the f occurs.