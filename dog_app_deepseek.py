import csv
import time
import random

# CSV files
BOOKINGS_FILE = "bookings.csv"
WALKERS_FILE = "walkers.csv"


# Function to save booking data to CSV
def save_booking_to_csv(booking_data):
    """Save booking details to a CSV file."""
    with open(BOOKINGS_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(booking_data)


# Function to save walker/carer data to CSV
def save_walker_to_csv(walker_data):
    """Save walker/carer details to a CSV file."""
    with open(WALKERS_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(walker_data)


# Function to fetch all bookings from CSV
def fetch_bookings():
    """Fetch and display all bookings from the CSV file."""
    try:
        with open(BOOKINGS_FILE, mode="r") as file:
            reader = csv.reader(file)
            print("\nAll Bookings:")
            for row in reader:
                print(f"\t- {', '.join(row)}")
    except FileNotFoundError:
        print("\nNo bookings found. The file does not exist yet.")


# Function to fetch all walkers/carers from CSV
def fetch_walkers():
    """Fetch and display all walkers/carers from the CSV file."""
    try:
        with open(WALKERS_FILE, mode="r") as file:
            reader = csv.reader(file)
            print("\nAll Walkers/Carers:")
            for row in reader:
                print(f"\t- {', '.join(row)}")
    except FileNotFoundError:
        print("\nNo walkers/carers found. The file does not exist yet.")


# Function to assign a random walker/carer
def assign_walker(service_type):
    """Assign a random walker/carer if available."""
    try:
        with open(WALKERS_FILE, mode="r") as file:
            reader = csv.reader(file)
            walkers = [row for row in reader if row[2].lower() == service_type.lower()]
            if walkers:
                return random.choice(walkers)
            else:
                return None
    except FileNotFoundError:
        return None


# Function to handle walk service
def walk():
    """Handle walk service details."""
    print("\nYou have selected the Walk service.")
    while True:
        duration = (
            input("\tEnter the duration of the walk (e.g., 30-minutes, 60-minutes): ")
            .strip()
            .lower()
        )
        if duration in ["30-minutes", "60-minutes"]:
            return duration
        else:
            print(
                "\n\tInvalid duration! Please enter either '30-minutes' or '60-minutes'. :0"
            )


# Function to handle daycare service
def daycare():
    """Handle daycare service details."""
    print("\nYou have selected the Daycare service.")
    while True:
        duration = (
            input(
                "\tEnter the duration of daycare (e.g., 4-hours, 8-hours, 24-hours): "
            )
            .strip()
            .lower()
        )
        if duration in ["4-hours", "8-hours", "24-hours"]:
            return duration
        else:
            print(
                "\n\tInvalid duration! Please enter either '4-hours', '8-hours', or '24-hours'. :0"
            )


# Function to handle user input and booking
def user_input():
    """Collect user input and process booking."""
    print("\nBooking Menu:")
    print(
        "\n\tNote: You can always enter [exit] to\n\tdiscard everything and exit from the menu.\n"
    )

    # Collect user details
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
            print("\n\tError! Please enter a valid phone number. :0\n")
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
            print("\n\tCan't accept more than '5' dogs for a walk.")
            print("\tDog walkers are human too. :0\n")
            continue

        break

    print("\n\tNote: If there are more than one breeds, add comma after each one.")
    while True:
        dog_breed = (
            input("\n\tEnter the breed name(s): ").strip().capitalize().split(",")
        )
        if len(dog_breed) > int(num_dogs):
            print(
                f'\n\tMaximum "{num_dogs}" breed names for "{num_dogs}" dogs. It\'s really that simple. :0'
            )
            print("\tTry again.")
            continue

        for i in dog_breed:
            if i.lower() == "exit":
                print("\n\tExiting the menu. ;)")
                return None

        break

    # Select service type
    while True:
        choice_a = (
            input("\n\tDo you want a walk or daycare for your dog? [walk/daycare]: ")
            .strip()
            .lower()
        )

        if choice_a == "exit":
            print("\n\tExiting the menu. ;)")
            return None

        elif choice_a == "walk":
            service_type = "Walk"
            service_details = walk()
            break

        elif choice_a == "daycare":
            service_type = "Daycare"
            service_details = daycare()
            break

        else:
            print("\n\tInvalid Choice! Try again. :0")
            continue

    # Assign a walker/carer
    assigned_walker = assign_walker(service_type)
    if not assigned_walker:
        print("\n\tSorry, no walker/carer is available at the moment. :(")
        return None

    print(f"\n\tAssigned Walker/Carer: {assigned_walker[0]} {assigned_walker[1]}")

    # Display entered details
    print("\nEntered Details:")
    print(f"\n\tFirst Name: {usr_name_f}")
    print(f"\tLast Name: {usr_name_l}")
    print(f"\tPhone Number: {usr_phone}")
    print(f"\tNumber of Dog(s): {num_dogs}")
    print(f"\tDog Breed(s): {', '.join(dog_breed)}")
    print(f"\tService Type: {service_type}")
    print(f"\tService Details: {service_details}")
    print(f"\tAssigned Walker/Carer: {assigned_walker[0]} {assigned_walker[1]}")

    # Confirm booking
    while True:
        choice_b = (
            input(
                "\n\tPlease check the details carefully and answer [yes/no] \nif the details are correct or not: "
            )
            .strip()
            .lower()
        )

        if choice_b == "yes":
            # Save booking data to CSV
            booking_data = [
                usr_name_f,
                usr_name_l,
                usr_phone,
                num_dogs,
                ", ".join(dog_breed),
                service_type,
                service_details,
                assigned_walker[0],
                assigned_walker[1],
            ]
            save_booking_to_csv(booking_data)
            print("\n\tBooking saved successfully! :)")
            break
        elif choice_b == "no":
            print("\n\tBooking discarded. Please start again. :0")
            return None
        else:
            print("\n\tInvalid Choice! Try again. :0")
            continue


# Function to handle walker/carer registration
def walker_input():
    """Handle walker/carer registration."""
    print("\nWalker/Carer Registration:")
    print(
        "\n\tNote: You can always enter [exit] to\n\tdiscard everything and exit from the menu.\n"
    )

    # Collect walker/carer details
    while True:
        walker_name_f = input("\tEnter your first name: ").strip().capitalize()
        if walker_name_f.lower() == "exit":
            print("\n\tExiting the menu. ;)")
            return None

        walker_name_l = input("\tEnter your last name: ").strip().capitalize()
        if walker_name_l.lower() == "exit":
            print("\n\tExiting the menu. ;)")
            return None
        elif (len(walker_name_f) > 15) or (len(walker_name_l) > 15):
            print(
                '\n\tError! Maximum character limit for a name is "15" characters each. :0\n'
            )
            continue

        break

    while True:
        walker_phone = input("\tEnter your phone number: ").strip()
        if walker_phone.lower() == "exit":
            print("\n\tExiting the menu. ;)")
            return None
        elif (len(walker_phone) != 11) or (not walker_phone.isdigit()):
            print("\n\tError! Please enter a valid phone number. :0\n")
            continue

        break

    while True:
        service_type = (
            input("\tEnter the service you want to provide [walk/daycare/both]: ")
            .strip()
            .lower()
        )
        if service_type == "exit":
            print("\n\tExiting the menu. ;)")
            return None
        elif service_type not in ["walk", "daycare", "both"]:
            print(
                "\n\tInvalid service type! Please enter 'walk', 'daycare', or 'both'. :0"
            )
            continue

        break

    while True:
        availability = (
            input("\tEnter your availability duration (e.g., 2-hours, 4-hours): ")
            .strip()
            .lower()
        )
        if availability == "exit":
            print("\n\tExiting the menu. ;)")
            return None
        elif availability not in ["2-hours", "4-hours", "8-hours"]:
            print(
                "\n\tInvalid duration! Please enter '2-hours', '4-hours', or '8-hours'. :0"
            )
            continue

        break

    # Save walker/carer data to CSV
    walker_data = [
        walker_name_f,
        walker_name_l,
        walker_phone,
        service_type,
        availability,
    ]
    save_walker_to_csv(walker_data)
    print("\n\tWalker/Carer registration successful! :)")


# Main function
def main():
    """Main function to run the program."""
    print("\n WELCOME TO DOG WALKING APP")
    print("=(Where Dogs Can Have Fun!)=")

    while True:
        print("\nMain Menu:")
        print("\n\t[1] Book A Walk/Daycare")
        print("\t[2] Be A Dog Walker/Carer")
        print("\t[3] View All Bookings")
        print("\t[4] View All Walkers/Carers")
        print("\t[e] Exit")

        choice = input("\n\tEnter your choice: ").strip()
        if choice == "1":
            user_input()
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


# Run the program
if __name__ == "__main__":
    main()
