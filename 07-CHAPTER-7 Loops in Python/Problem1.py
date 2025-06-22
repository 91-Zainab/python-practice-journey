#Write a program to print multiplication table of a given num using for loop.
num=int(input("Enter any num:"))

for i in range(1, 11):
    print(f"{num}x{i}={num*i}")
