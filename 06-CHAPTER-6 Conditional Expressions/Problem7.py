# write a program tofind out whether a given post is talking about"harry" or not.

post = input("Enter your post")
if("harry".lower() in post.lower()):
    print("yes harry is in the post")
else:
    print("harry is not in the post")
