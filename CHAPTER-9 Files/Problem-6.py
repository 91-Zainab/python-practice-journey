#Writre a program to mine a log file and find out whether it contains 'Python'.

with open ("log.txt", "r") as f:
    content = f.read()

if ("python" in content):
    print("Yes Python is in content.")
else:
    print("Python is'nt in the content.")