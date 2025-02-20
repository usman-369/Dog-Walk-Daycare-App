# import winsound
# import pygame
# from playsound import playsound
# import os


# def user_input():
#     while True:
#         wlk_time = input("\n\tEnter the time of walk (e.g. HH-MM-(AM/PM)): ").strip().upper().split("-")

#         if (len(wlk_time) != 3) or (len(wlk_time[0]) != 2) or (len(wlk_time[1]) != 2) or (wlk_time[2] not in ["AM", "PM"]):
#             print("\n\tInvalid Format! Try again. :0")
#             continue

#         hour = int(wlk_time[0])
#         minute = int(wlk_time[1])

#         if (hour < 1) or (hour > 12) or (minute < 0) or (minute > 59):
#             print("\n\tInvalid Time! Try again. :0")
#             continue

#         break


#         val = False
#         # int_wlk_time = int(wlk_time)

#         for i in wlk_time:
#             # time_val = int(i)

#             if i.lower() == "e":
#                 print("\n\tExiting the menu. ;)")
#                 return None

#             elif (len(i) != 2) or (len(wlk_time) != 3) or (not wlk_time[0:2].isdigit()) or (wlk_time[2] not in ["AM", "PM"]):
#                 print("\n\tInvalid Input! Try again. :0")
#                 val = True
#                 break

#             elif (wlk_time[0] < 1) or (int_wlk_time[0] > 12) or (int_wlk_time[1] < 0) or (int_wlk_time[1] < 60):
#                 print("\n\tInvalid Time! Try again. :0")
#                 val = True
#                 break

#         if val:
#             continue

#         break


# user_input()


# Windows beep sound
# winsound.Beep(1000, 1000)  # 1000 Hz for 1000 milliseconds
# Play a WAV or MP3 file
# playsound('beep.wav')  # Replace with your sound file path
# Initialize pygame mixer
# pygame.mixer.init()

# Load and play sound using pygame
# pygame.mixer.music.load('beep.wav')  # Replace with your sound file path
# pygame.mixer.music.play()

# Wait for the sound to finish
# while pygame.mixer.music.get_busy():
#     pygame.time.Clock().tick(10)

# os.system("beep -f 300")

# os.system("aplay /usr/share/sounds/alsa/Noise.wav")


# def walk():
#     print("\nYou have selected the Walk service.")

#     while True:
#         print("\n please select the duration:")
#         print("\n\t[1] 30 minutes walk")
#         print("\t[2] 60 minutes walk")
#         print("\t[3] 90 minutes walk")
#         print("\t[4] 120 minutes walk")
#         print("\t[e] Exit from the booking menu")

#         choice = input("\n\tEnter your choice: ").strip()

#         if choice == "1":
#             print("\nYou selected a 30-minute walk.")

#             print("30-minute walk completed.")

#         elif choice == "2":
#             print("\nYou selected a 60-minute walk.")

#             print("60-minute walk completed.")

#         elif choice == "3":
#             print("\nYou selected a 90-minute walk.")

#             print("90-minute walk completed.")

#         elif choice == "4":
#             print("\nYou selected a 120-minute walk.")

#             print("120-minute walk completed.")

#         elif choice.lower() == "e":
#             print("\nExiting Walk service. Goodbye!")

#             return False

#         else:
#             print("\nInvalid choice. Please try again.")
#             continue
#         break


# def daycare():
#     print("\nYou have selected the Daycare service.")

#     while True:
#         print("\nPlease select the duration:")
#         print("\n\t[1] 8-hour Daycare")
#         print("\t[2] 24-hour Daycare")
#         print("\t[3] 1.5-day Daycare")
#         print("\t[4] 2.5-day Daycare")
#         print("\t[e] Exit from the booking menu")

#         choice = input("\n\tEnter your choice: ").strip()

#         if choice == "1":
#             print("\nYou selected a 8-hour Daycare service.")

#         elif choice == "2":
#             print("\nYou selected a 24-hour Daycare service.")

#         elif choice == "3":
#             print("\nYou selected a 1.5-day Daycare service.")

#         elif choice == "4":
#             print("\nYou selected a 2.5-day Daycare service.")

#         elif choice.lower() == "e":
#             print("\nExiting from the booking menu. Goodbye!")
#             break

#         else:
#             print("\nInvalid choice. Please try again.")



# def general_input():
#     print(
#             "\n\tNote: You can always enter [exit] to\n\tdiscard everything and exit from the menu.\n"
#         )

#     while True:
#         walker_name_f = input("\tEnter your first name: ").strip().capitalize()
#         if walker_name_f.lower() == "exit":
#             print("\n\tExiting the menu. ;)")
#             return None

#         walker_name_l = input("\tEnter your last name: ").strip().capitalize()
#         if walker_name_l.lower() == "exit":
#             print("\n\tExiting the menu. ;)")
#             return None
#         elif (len(walker_name_f) > 15) or (len(walker_name_l) > 15):
#             print(
#                 '\n\tError! Maximum character limit for a name is "15" characters each. :0\n'
#             )
#             continue
#         break

#     while True:
#         walker_phone = input("\tEnter your phone number: ").strip()
#         if walker_phone.lower() == "exit":
#             print("\n\tExiting the menu. ;)")
#             return None
#         elif (len(walker_phone) != 11) or (not walker_phone.isdigit()):
#             print("\n\tError! Please enter a valid phone number. :0\n")
#             continue
#         break


# def assign_service(service_type):
#     try:
#         with open(SERVICES_FILE, mode="r") as file:
#             reader = csv.reader(file)

#             rows = [row for row in reader if row[3].strip() == service_type]
#             if rows:
#                 return random.choice(rows)
#             else:
#                 print(f"\n\tNo {service_type} service providers found.")
#                 return None
#     except FileNotFoundError:
#         print("\n\tNo walkers/carers found. The file does not exist yet.")
#         return None
#     except Exception as e:
#         print(f"\n\tAn error occurred: {e}")
#         return None





# def calculate_fee_walk(duration):


#     fee_rates = {0.5: 50.0, 1.0: 100.0, 1.5: 150.0, 2.0: 200.0}


#     fee1 = fee_rates.get(duration)
#     return fee1
