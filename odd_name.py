def main():
    user_name = get_name()
    frequency = letter_frequency()
    while user_name == "":
        user_name = input("Name cannot be blank, please enter your name")
    print (user_name[::frequency])


def get_name():
    user_name = input("Please enter your name")
    return user_name

def letter_frequency():
    frequency = int(input("Enter an integer"))
    return frequency


main()
