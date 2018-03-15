user_name = input("Please enter your name")
while user_name == "":
    user_name = input("Name cannot be blank, please enter your name")
print (user_name[::2])