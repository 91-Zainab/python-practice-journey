# Write a python function which converts inches to cms.
def inch_to_cms(inch):
    return(inch* 2.54)
inch=int(input("Enter value in inches:"))
print(f"The corresponding value in cmz is:{inch_to_cms(inch)}")