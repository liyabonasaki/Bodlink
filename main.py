##################################
#   @Author : Liyabona Saki
#   @Descr  : Bodlink Excercise
#
###################################
import sys


def __init__(self):
    pass


def print_hi():
    name = input("Please enter your name\n")
    print(f'Hi, {name}')


def menu():
    print("\n1 --> Run the program")
    print("2 --> Exits the program")
    try:
        user = int(input("\nPlease enter choice\n"))
        if user != 1:
            print("Exiting the program....")
            sys.exit()

        else:
            print_hi()
            menu()

    except:
        print("Sorry something went wrong")


# menu()

if __name__ == '__main__':
    menu()
