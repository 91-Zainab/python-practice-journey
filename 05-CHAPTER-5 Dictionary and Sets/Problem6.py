# Create an empty dictioonary. allow 4 friends to enter their favourite language as value and use key as their names.assume that the names are unique.

d={}
name=input("Enter friends name:")
lang=input("Enter language:")
d.update({name:lang})
name=input("Enter friends name:")
lang=input("Enter language:")
d.update({name:lang})
name=input("Enter friends name:")
lang=input("Enter language:")
d.update({name:lang})
name=input("Enter friends name:")
lang=input("Enter language:")
d.update({name:lang})
print(d)