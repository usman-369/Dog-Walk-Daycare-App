import csv
import sys
import time


BOOKINGS_FILE = "services.csv"
SERVICES_FILE = "walkers.csv"


EXIT_MSG = "\n\tExiting the menu. ;)"


def save_bookings(booking_data):
    try:
        with open(BOOKINGS_FILE, mode="a", newline="") as file:
            write = csv.writer(file)
            write.writerow(booking_data)
    except FileNotFoundError:
        print("\n\tFile Not Found! :0")


def save_services(service_data):
    try:
        with open(SERVICES_FILE, mode="a", newline="") as file:
            write = csv.writer(file)
            write.writerow(service_data)
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
            return None
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
            return None
        else:
            print("\n\tInvalid Choice! Try again. :0")
            continue


def general_input():
    print(
            "\n\tNote: You can always enter [exit] to\n\tdiscard everything and exit from the menu.\n"
        )

    while True:
        first_name = input("\tEnter your first name: ").strip().capitalize()
        if first_name.lower() == "exit":
            return None

        last_name = input("\tEnter your last name: ").strip().capitalize()
        if last_name.lower() == "exit":
            return None
        elif (len(first_name) > 15) or (len(last_name) > 15):
            print(
                '\n\tError! Maximum character limit for a name is "15" characters each. :0\n'
            )
            continue
        break

    while True:
        phone = input("\tEnter your phone number: ").strip()
        if phone.lower() == "exit":
            return None
        elif (len(phone) != 11) or (not phone.isdigit()):
            print("\n\tError! Please enter a valid phone number. :0\n")
            continue
        break

    return first_name, last_name, phone


def booking_input():
    print("\nBooking Menu:")

    g_input = general_input()
    if g_input is None:
        print(EXIT_MSG)
        return None

    first_name, last_name, phone = g_input

    while True:
        num_dogs = input("\tEnter the number of dog(s) [1-5]: ").strip()
        if num_dogs.lower() == "exit":
            print(EXIT_MSG)
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
            print(EXIT_MSG)
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
            print(EXIT_MSG)
            return None
        elif choice == "walk":
            service_type = "Walk"
            duration = walk_input()
        elif choice == "daycare":
            service_type = "Daycare"
            duration = daycare_input()
        else:
            print("\n\tInvalid Choice! Try again. :0")
            continue
        if not duration:
            continue
        break

    # assigned_service = assign_service(service_type)
    # if not assigned_service:
    #     print("\n\tSorry, no walker/carer is available at the moment. :(")
    #     return None

    print("\nEntered Details:")
    print(f"\n\tFirst Name: {first_name}")
    print(f"\tLast Name: {last_name}")
    print(f"\tPhone Number: {phone}")
    print(f"\tNumber of Dog(s): {num_dogs}")
    print(f"\tDog Breed(s): {', '.join(dog_breed)}")
    print(f"\tChosen Service: {service_type}")
    if duration in [0.5]:
        print(f"\tDuration of {service_type}: 30-Minutes")
    elif duration in [1.0]:
        print(f"\tDuration of {service_type}: {duration}-Hour")
    elif duration in [1.5, 2.0, 4.0, 8.0, 12.0, 24.0]:
        print(f"\tDuration of {service_type}: {duration}-Hours")

    while True:
        choice = (
            input(
                "\n\tPlease check if the details are correct or not\n\tand answer [yes/no] to continue your booking: "
            )
            .strip()
            .lower()
        )
        if choice == "yes":
            booking_data = []
        elif choice == "no":
            inr_choice = input("\n\tDo you want to change your details or\n\tdiscard everything and exit? [change/exit]: ").strip().lower()
            if inr_choice == "change":
                booking_input()
            elif inr_choice == "exit":
                print(EXIT_MSG)
                return None
            else:
                print("\n\tInvalid Choice! Try again. :0")
        else:
            print("\n\tInvalid Choice! Try again. :0")
            continue
        break


def service_input():
    print("\nWalker/Carer Registration Menu:")

    g_input = general_input()
    if g_input is None:
        print(EXIT_MSG)
        return None

    first_name, last_name, phone = g_input

    while True:
        service_type = (
            input("\tEnter the service you want to provide [walk/daycare]: ")
            .strip()
            .lower()
        )
        if service_type == "exit":
            print(EXIT_MSG)
            return None
        elif service_type not in ["walk", "daycare"]:
            print("\n\tInvalid Input! Try again. :0")
            continue
        break

    service_data = [
        first_name,
        last_name,
        phone,
        service_type,
    ]
    save_services(service_data)
    print("\n\tWalker/Carer Registration Successful! ;)")


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
            service_input()
        elif choice == "3":
            fetch_bookings()
        elif choice == "4":
            fetch_walkers()
        elif choice.lower() == "e":
            print("\nExiting the program. Bye! ;)\n")
            time.sleep(1)
            sys.exit()
        else:
            print("\n\tInvalid Choice! Please try again. :0")
            continue


if __name__ == "__main__":
    main()
