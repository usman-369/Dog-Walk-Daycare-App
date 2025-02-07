import csv
import time


BOOKINGS_FILE = "bookings.csv"
WALKERS_FILE = "walkers.csv"


def save_bookings(booking_data):
    try:
        with open(BOOKINGS_FILE, mode="a", newline="") as file:
            write = csv.writer(file)
            write.writerow(booking_data)
    except FileNotFoundError:
        print("\n\tFile Not Found! :0")


def save_walkers(walker_data):
    try:
        with open(WALKERS_FILE, mode="a", newline="") as file:
            write = csv.writer(file)
            write.writerow(walker_data)
    except FileNotFoundError:
        print("\n\tFile Not Found! :0")


def fetch_bookings():
    try:
        with open(BOOKINGS_FILE, mode="r") as file:
            reader = csv.reader(file)
            print("\nAll Bookings:")
            for row in reader:
                print(f"\t- {', '.join(row)}")
    except FileNotFoundError:
        print("\nNo bookings found. The file does not exist yet.")


def fetch_walkers():
    try:
        with open(WALKERS_FILE, mode="r") as file:
            reader = csv.reader(file)
            print("\nAll Walkers/Carers:")
            for row in reader:
                print(f"\t- {', '.join(row)}")
    except FileNotFoundError:
        print("\nNo walkers/carers found. The file does not exist yet.")


def assign_service(service_type):
    pass


def walk_input():
    print("\nYou have chosen the walk service.\a")

    while True:
        print("\nPlease choose the duration of walk:")
        print("\n\t[1] 30-minutes")
        print("\t[2] 1-hour")
        print("\t[3] 1.5-hours")
        print("\t[4] 2-hours")
        print("\t[e] Go Back")

        choice = input("\n\tEnter your choice: ").strip()

        if choice == "1":
            print("\n\tYou chose a 30-minute walk.")
            return 0.5
        elif choice == "2":
            print("\n\tYou chose a 1-hour walk.")
            return 1.0
        elif choice == "3":
            print("\n\tYou chose a 1.5-hour walk.")
            return 1.5
        elif choice == "4":
            print("\n\tYou chose a 2-hour walk.")
            return 2.0
        elif choice.lower() == "e":
            return False
        else:
            print("\n\tInvalid Choice! Try again. :0")
            continue


def daycare_input():
    print("\nYou have chosen the daycare service.\a")

    while True:
        print("\nPlease choose the duration of daycare:")
        print("\n\t[1] 4-hours")
        print("\t[2] 8-hours")
        print("\t[3] 12-hours")
        print("\t[4] 24-hours")
        print("\t[e] Go Back")

        choice = input("\n\tEnter your choice: ").strip()

        if choice == "1":
            print("\n\tYou chose 4-hours of daycare.")
            return 4.0
        elif choice == "2":
            print("\n\tYou chose 8-hours of daycare.")
            return 8.0
        elif choice == "3":
            print("\n\tYou chose 12-hours of daycare.")
            return 12.0
        elif choice == "4":
            print("\n\tYou chose 24-hours of daycare.")
            return 24.0
        elif choice.lower() == "e":
            return False
        else:
            print("\n\tInvalid Choice! Try again. :0")
            continue


def booking_input():
    print("\nBooking Menu:")

    print(
        "\n\tNote: You can always enter [exit] to discard\n\teverything and exit from the menu.\n"
    )

    while True:
        usr_name_f = input("\tEnter your first name: ").strip().capitalize()
        if usr_name_f.lower() == "exit":
            print("\n\tExiting the menu. ;)")
            return None

        usr_name_l = input("\tEnter your last name: ").strip().capitalize()
        if usr_name_l.lower() == "exit":
            print("\n\tExiting the menu. ;)")
            return None
        elif (len(usr_name_f) > 15) or (len(usr_name_l) > 15):
            print(
                '\n\tError! Maximum character limit for a name is "15" characters each. :0\n'
            )
            continue

        break

    while True:
        usr_phone = input("\tEnter your phone number: ").strip()
        if usr_phone.lower() == "exit":
            print("\n\tExiting the menu. ;)")
            return None
        elif (len(usr_phone) != 11) or (not usr_phone.isdigit()):
            print('\n\tError! Please enter a valid "11"-digit phone number. :0\n')
            continue

        break

    while True:
        num_dogs = input("\tEnter the number of dog(s) [1-5]: ").strip()
        if num_dogs.lower() == "exit":
            print("\n\tExiting the menu. ;)")
            return None
        elif not num_dogs.isdigit():
            print("\n\tInvalid Input! Try again. :0\n")
            continue
        elif int(num_dogs) > 5:
            print('\n\tCan\'t accept more than "5" dogs for a walk.')
            print("\tDog walkers are human too. :0\n")
            continue

        break

    print('\n\tNote: If there are more than one breeds, add comma "," after each one.')
    while True:
        dog_breed = (
            input("\n\tEnter the breed name(s): ").strip().capitalize().split(",")
        )
        if len(dog_breed) > int(num_dogs):
            print(
                f'\n\tMaximum "{num_dogs}" breed names are allowed for "{num_dogs}" number of dogs.'
            )
            print("It's really that simple. Try again. :0")
            continue
        if any(i.lower() == "exit" for i in dog_breed):
            print("\n\tExiting the menu. ;)")
            return None
        break

    while True:
        print(
            '\n\tNote: A walk is of "30" minutes minimum while\n\tdaycare is of "4" hours minimum.'
        )
        choice = (
            input("\n\tDo you want a walk or daycare for your dog? [walk/daycare]: ")
            .strip()
            .lower()
        )
        if choice == "exit":
            print("\n\tExiting the menu. ;)")
            return None
        elif choice == "walk":
            service_type = "Walk"
            details = walk_input()
        elif choice == "daycare":
            service_type = "Daycare"
            details = daycare_input()
        else:
            print("\n\tInvalid Choice! Try again. :0")
            continue
        if not details:
            continue
        break

    assigned_service = assign_service(service_type)
    if not assigned_service:
        print("\n\tSorry, no walker/carer is available at the moment. :(")
        return None

    print("\nEntered Details:")
    print(f"\n\tFirst Name: {usr_name_f}")
    print(f"\tLast Name: {usr_name_l}")
    print(f"\tPhone Number: {usr_phone}")
    print(f"\tNumber of Dog(s): {num_dogs}")
    print(f"\tDog Breed(s): {dog_breed}")

    while True:
        choice_b = (
            input(
                "\n\tPlease check the details carefually and answer [yes/no]\n\tif the details are correct or not: "
            )
            .strip()
            .lower()
        )

        if choice_b == "yes":
            pass
        elif choice_b == "no":
            pass
        else:
            print("\n\tInvalid Choice! Try again. :0")
            continue

        break


def walker_input():
    print("\n\tNothing here yet.")


def main():
    print("\nWELCOME TO DOG WALKING/DAYCARE APP")
    print("====(Where Dogs Can Have Fun!)====")

    while True:
        print("\nMain Menu:")
        print("\n\t[1] Book A Walk/Daycare")
        print("\t[2] Be A Walker/Carer")
        print("\t[3] View All Bookings")
        print("\t[4] View All Walkers/carers")
        print("\t[e] Exit")

        choice = input("\n\tEnter your choice: ").strip()
        if choice == "1":
            booking_input()
        elif choice == "2":
            walker_input()
        elif choice == "3":
            fetch_bookings()
        elif choice == "4":
            fetch_walkers()
        elif choice.lower() == "e":
            print("\nExiting the program. Bye! ;)\n")
            time.sleep(2)
            break
        else:
            print("\n\tInvalid Choice! Please try again. :0")
            continue


if __name__ == "__main__":
    main()
