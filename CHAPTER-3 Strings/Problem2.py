#write a program to fill in a letter template given below with name and date.
letter= '''Dear <|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>","Zainab").replace("<|Date|>","29-August-2004"))