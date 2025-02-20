import csv
import time
import random
from datetime import datetime, timedelta


def get_input(prompt, validation_func=None, error_message="Invalid Input! Try again."):
    """Reusable function to get validated user input."""
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == "exit":
            print("\n\tExiting the menu. ;)")
            return None
        if validation_func and not validation_func(user_input):
            print(f"\n\t{error_message}")
            continue
        return user_input


def save_to_csv(filename, data):
    """Appends data to a CSV file."""
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)


def fetch_walkers():
    """Reads available walkers from CSV and filters expired ones."""
    available_walkers = []
    current_time = datetime.now()

    try:
        with open("walkers.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                name, phone, service, end_time = row
                end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M")
                if end_time > current_time:
                    available_walkers.append(row)
    except FileNotFoundError:
        pass

    return available_walkers


def assign_walker():
    """Assigns a random walker if available, otherwise returns None."""
    walkers = fetch_walkers()
    return random.choice(walkers) if walkers else None


def booking_input():
    print("\nBooking Menu:")
    print("\n\tNote: Enter [exit] to discard everything and exit.")

    usr_name_f = get_input(
        "\tEnter your first name: ", lambda x: len(x) <= 15
    ).capitalize()
    if usr_name_f is None:
        return
    usr_name_l = get_input(
        "\tEnter your last name: ", lambda x: len(x) <= 15
    ).capitalize()
    if usr_name_l is None:
        return
    usr_phone = get_input(
        "\tEnter your phone number: ", lambda x: x.isdigit() and len(x) == 11
    )
    if usr_phone is None:
        return
    num_dogs = get_input(
        "\tEnter number of dog(s) [1-5]: ", lambda x: x.isdigit() and 1 <= int(x) <= 5
    )
    if num_dogs is None:
        return
    dog_breeds = get_input("\tEnter breed(s), comma-separated: ")
    if dog_breeds is None:
        return
    choice_a = get_input(
        "\tDo you want a walk or daycare? [walk/daycare]: ",
        lambda x: x in ["walk", "daycare"],
    )
    if choice_a is None:
        return

    walker = assign_walker()
    if not walker:
        print("\n\tNo walker/carer available at the moment. Try again later.")
        return

    print(f"\n\tAssigned Walker: {walker[0]} (Phone: {walker[1]})")

    save_to_csv(
        "bookings.csv",
        [
            usr_name_f,
            usr_name_l,
            usr_phone,
            num_dogs,
            dog_breeds,
            choice_a,
            walker[0],
            walker[1],
        ],
    )
    print("\n\tBooking confirmed! 🎉")


def walker_input():
    print("\nWalker Registration:")
    print("\n\tNote: Enter [exit] to discard everything and exit.")

    name = get_input("\tEnter your name: ", lambda x: len(x) <= 15).capitalize()
    if name is None:
        return
    phone = get_input(
        "\tEnter your phone number: ", lambda x: x.isdigit() and len(x) == 11
    )
    if phone is None:
        return
    service = get_input(
        "\tWhich service? [walk/daycare/both]: ",
        lambda x: x in ["walk", "daycare", "both"],
    )
    if service is None:
        return
    duration = get_input(
        "\tEnter availability duration in hours [1-12]: ",
        lambda x: x.isdigit() and 1 <= int(x) <= 12,
    )
    if duration is None:
        return

    end_time = datetime.now() + timedelta(hours=int(duration))
    save_to_csv(
        "walkers.csv", [name, phone, service, end_time.strftime("%Y-%m-%d %H:%M")]
    )
    print("\n\tRegistration successful! You are now an active walker/carer. 🐶")


def main():
    print("\n WELCOME TO DOG WALKING APP")
    print("=(Where Dogs Can Have Fun!)=")

    while True:
        print("\nMain Menu:")
        print("\t[1] Book A Walk/Daycare")
        print("\t[2] Register as Walker/Carer")
        print("\t[e] Exit")

        choice = input("\n\tEnter your choice: ").strip().lower()
        if choice == "1":
            booking_input()
        elif choice == "2":
            walker_input()
        elif choice == "e":
            print("\nExiting the program. Bye! ;)")
            time.sleep(2)
            break
        else:
            print("\n\tInvalid Choice! Please try again.")


main()
