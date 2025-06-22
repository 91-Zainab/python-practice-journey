#Write a program to find out whether a file is identical and matches the content of another file.

with open ("this.txt", "r") as f:
    content1 = f.read()

with open ("poems.txt","r") as f:
    content2 = f.read()

if (content1 == content2):
    print("Yes content of these files are same.")
else:
    print("content of these files are not same.")