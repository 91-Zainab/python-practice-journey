#Write a program to find whether a given number is prime or not.
num=int(input("Enter any num:"))
for i in range(2,num):
    if(num%i) == 0:
        print("The num is not prime")
        break
else:
    print("The num is prime")
