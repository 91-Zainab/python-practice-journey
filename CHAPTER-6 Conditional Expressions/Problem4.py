# write a program to find whether a given username contains less than 10 characters or not.

name=input("Enter username:")
if(len(name)<10):
    print("This user name contains less than 10 characters.")
else:
    print("This user name contains less than or equal to 10 characters.")