# Write a program to find out whether a student has passed or failed if it reauires a total of 40% and atleast 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
marks1=int(input("Enter Marks of sub 1:"))
marks2=int(input("Enter Marks of sub 2:"))
marks3=int(input("Enter Marks of sub 3:"))

total_percentage= (100*(marks1+marks2+marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("Congratulations you're passed.",total_percentage)
else:
    print("You failed",total_percentage)