import time
import readline
# from prompt_toolkit import prompt


def user_input():
    print("\nBooking Menu:")

    print("\n\tNote: You can always enter [e] if you want to discard everything and exit.\n")

    while True:
        usr_name_f = input("\tEnter your first name: ").strip().capitalize()
        usr_name_l = input("\tEnter your last name: ").strip().capitalize()

        if (len(usr_name_f) or len(usr_name_l)) > 15:
            print("\n\tError! Maximum character limit for a name is '15' characters each. :0\n")
            continue
        elif (usr_name_f or usr_name_l).lower() == "e":
            return None
        else:
            break

    while True:
        usr_phone = input("\tEnter your phone number: ").strip()

        if (len(usr_phone) != 11) or (not usr_phone.isdigit()):
            print("\n\tError! Please enter a valid phone number. :0\n")
            continue
        elif usr_phone.lower() == "e":
            return None
        else:
            break

    while True:
        num_dogs = input("\tEnter the number of dog(s) for the walk [1-5]: ").strip()

        if not num_dogs.isdigit():
            print("\n\tInvalid Input! Try again. :0\n")
            continue
        elif int(num_dogs) > 5:
            print("\n\tCan't accept more than '5' dogs for a walk.")
            print("\tDog walkers are human too. :0\n")
            continue
        elif num_dogs.lower() == "e":
            return None
        else:
            break

    dog_breed = input("\tEnter the breed name(s): ").strip().capitalize().split(5)
    print("\tNote: If there are more than one breeds to enter, press ")
    # wlk_date = input("\tEnter the date of walk: ").strip()
    # print("\t(e.g. 31/12/2025)")
    # print("\n\t(Note: You can book a day only within '7' days of booking day.)")
    # wlk_time = input("\n\tEnter the time of walk: ")
    # wlk_duration = input("\tEnter the duration of walk: ")


def walker_input():
    pass


def list_walkers():
    pass


def main():
    print("\n WELCOME TO DOG WALKING APP")
    print("=(Where Dogs Can Have Fun!)=")

    while True:
        print("\nMain Menu:")
        print("\n\t[1] Book A Walk")
        print("\t[2] Be A Dog Walker")
        print("\t[e] Exit")

        choice = input("\n\tEnter your choice: ").strip()
        if choice == "1":
            user_input()
        elif choice == "2":
            walker_input()
        elif choice.lower() == "e":
            print("\nExiting the program. Bye! ;)\n")
            time.sleep(2)
            break
        else:
            print("\n\tInvalid Choice! Please try again. :0")
            continue


main()
