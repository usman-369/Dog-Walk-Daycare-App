import csv
import random
import time
import sys
from tabulate import tabulate


EXIT_MSG = "\n\tExiting the menu. ;)"
INV_MSG = "\n\tIvalid Choice! Try again. :0"
FNF_MSG = "\nFile Not Found! :0"
ERROR_MSG = "\nAn error occurred: "


BOOKINGS_FILE = "bookings.csv"
SERVICES_FILE = "services.csv"


def save_bookings(booking_data):
    try:
        with open(BOOKINGS_FILE, mode="a", newline="") as file:
            write = csv.writer(file)
            write.writerow(booking_data)
    except FileNotFoundError:
        print(FNF_MSG)
    except Exception as e:
        print(f"{ERROR_MSG}{e}")
        return None


def save_services(service_data):
    try:
        with open(SERVICES_FILE, mode="a", newline="") as file:
            write = csv.writer(file)
            write.writerow(service_data)
    except FileNotFoundError:
        print(FNF_MSG)
    except Exception as e:
        print(f"{ERROR_MSG}{e}")
        return None


def fetch_bookings():
    try:
        with open(BOOKINGS_FILE, mode="r") as file:
            reader = csv.reader(file)
            rows = list(reader)

            print("\nAll Bookings:\n")
            headers = [
                "First Name",
                "Last Name",
                "Phone",
                "Dogs",
                "Breed",
                "Service",
                "Duration",
            ]
            print(tabulate(reader, headers=headers, tablefmt="fancy_grid"))
            print("\nTotal Bookings:", len(rows))
    except FileNotFoundError:
        print(FNF_MSG)
        return None
    except Exception as e:
        print(f"{ERROR_MSG}{e}")
        return None


def fetch_services():
    try:
        with open(SERVICES_FILE, mode="r") as file:
            reader = csv.reader(file)
            rows = list(reader)

            print("\nAll Walkers/Carers:")
            headers = ["First Name", "Last Name", "Phone", "Service"]
            print(tabulate(reader, headers=headers, tablefmt="fancy_grid"))
            print("\nTotal Walkers/Carers:", len(rows))
    except FileNotFoundError:
        print(FNF_MSG)
        return None
    except Exception as e:
        print(f"{ERROR_MSG}{e}")
        return None


def assign_service(chosen_service):
    try:
        with open(SERVICES_FILE, mode="r") as file:
            reader = csv.reader(file)

            rows = [row for row in reader if row[3].strip() == chosen_service]
            if rows:
                return random.choice(rows)
            else:
                return None
    except FileNotFoundError:
        print(FNF_MSG)
        return None
    except Exception as e:
        print(f"{ERROR_MSG}{e}")
        return None


def show_details(all_details, func):
    print("\nEntered Details:")
    general_details = all_details[:3]
    first_name, last_name, phone = general_details
    print(f"\n\tFirst Name: {first_name}")
    print(f"\tLast Name: {last_name}")
    print(f"\tPhone Number: {phone}")

    if func == "booking":
        dog_details = all_details[3:]
        num_dogs, dog_breed, chosen_service, duration = dog_details
        print(f"\tNumber of Dog(s): {num_dogs}")
        print(f"\tDog Breed(s): {', '.join(dog_breed)}")
        print(f"\tChosen Service: {chosen_service}")
        if duration == 0.5:
            print(f"\tDuration of {chosen_service}: 30-Minutes")
        elif duration == 1.0:
            print(f"\tDuration of {chosen_service}: {duration}-Hour")
        elif duration in [1.5, 2.0, 4.0, 8.0, 12.0, 24.0]:
            print(f"\tDuration of {chosen_service}: {duration}-Hours")
        return None

    elif func == "registration":
        service_details = all_details[3:]
        service_type = service_details[0]
        print(f"\tChosen Service: {service_type}")
        return None


def fee_calculation(chosen_service, duration):
    walk_fee_rates = {0.5: 500.0, 1.0: 1000.0, 1.5: 1500.0, 2.0: 2000.0}
    daycare_fee_rates = {4.0: 3000.0, 8.0: 5000.0, 12.0: 7000.0, 24.0: 10000.0}

    if chosen_service == "Walk":
        walk_fee = walk_fee_rates.get(duration)
        return walk_fee
    elif chosen_service == "Daycare":
        daycare_fee = daycare_fee_rates.get(duration)
        return daycare_fee


def confirm_input(func):
    while True:
        choice = (
            input(
                f"\n\tPlease check if the details are correct and\n\tanswer [yes/no] to confirm your {func}: "
            )
            .strip()
            .lower()
        )
        if choice == "yes":
            return True
        elif choice == "no":
            while True:
                inr_choice = (
                    input(
                        "\n\tDo you want to change your details or\n\tdiscard everything and exit? [change/exit]: "
                    )
                    .strip()
                    .lower()
                )
                if inr_choice == "change":
                    if func == "booking":
                        return booking_input()
                    elif func == "registration":
                        return service_input()
                elif inr_choice == "exit":
                    return False
                else:
                    print(INV_MSG)
                    continue
        else:
            print(INV_MSG)
            continue


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
            print(INV_MSG)
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
            print(INV_MSG)
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
            print(f"{INV_MSG}\n")
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
            chosen_service = "Walk"
            duration = walk_input()
        elif choice == "daycare":
            chosen_service = "Daycare"
            duration = daycare_input()
        else:
            print(INV_MSG)
            continue
        if not duration:
            continue
        break

    availability = assign_service(chosen_service)
    if not availability:
        if chosen_service == "Walk":
            print("\nSorry, no walker is available at the moment. :(")
            return None
        elif chosen_service == "Daycare":
            print("\nSorry, no carer is available at the moment. :(")
            return None

    func = "booking"
    all_details = [
        first_name,
        last_name,
        phone,
        num_dogs,
        dog_breed,
        chosen_service,
        duration,
    ]
    show_details(all_details, func)

    fee = fee_calculation(chosen_service, duration)
    print(f"\n\tTotal Fee: {fee}PKR")

    confirmation = confirm_input(func)
    if confirmation is True:
        save_bookings(all_details)
        print("\n\tBooking Successful! ;)")
        service_provider = assign_service(chosen_service)
        print(f"\n\tAssigned Walker/Carer: {service_provider[0]} {service_provider[1]}")
        print(f"\tContact: {service_provider[2]}")
        return None
    elif confirmation is False:
        print(EXIT_MSG)
        return None


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
            print(INV_MSG)
            continue
        break

    func = "registration"
    all_details = [
        first_name,
        last_name,
        phone,
        service_type,
    ]
    show_details(all_details, func)

    confirmation = confirm_input(func)
    if confirmation is True:
        save_services(all_details)
        print("\n\tRegistration Successful! ;)")
        return None
    elif confirmation is False:
        print(EXIT_MSG)
        return None


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
            fetch_services()
        elif choice.lower() == "e":
            print("\nExiting the program. Bye! ;)\n")
            time.sleep(1)
            sys.exit()
        else:
            print(INV_MSG)
            continue


if __name__ == "__main__":
    main()
