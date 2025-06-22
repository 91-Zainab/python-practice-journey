# Write a python program using function to convert celcuis to fahrenheit
# formula: c/5 = (f-32)/9
#  c =5*(f-32)/9
def f_to_C(f):
    return 5*(f-32)/9
f=int(input("Enter temperature in fahrenheit:"))
c= f_to_C(f)
print(f"{round(c, 2)} °C")
