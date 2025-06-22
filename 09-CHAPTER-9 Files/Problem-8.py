#write a program to make a copy of text file "this.txt"

with open ("this.txt", "r") as f:
    content = f.read()

with open ("thiscopy.txt", "w") as f:
    f.write(content)