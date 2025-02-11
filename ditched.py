# while True:
#     wlk_date = input("\n\tEnter the date of walk (e.g. DD-MM-YY): ").strip().split("-")

#     val = False
#     for i in wlk_date:
#         if i.lower() == "e":
#             print("\n\tExiting the menu. ;)")
#             return None
#         elif (not i.isdigit()) or (len(i) != 2) or (len(wlk_date) != 3):
#             print("\n\tInvalid Input! Try again. :0")
#             val = True
#             break
#     if val:
#         continue
#     break

# while True:
#     wlk_time = input("\n\tEnter the pickup time (e.g. HH-MM-AM/PM): ").strip().upper().split("-")

#     if (len(wlk_time) != 3) or (len(wlk_time[0]) != 2) or (len(wlk_time[1]) != 2) or (wlk_time[2] not in ["AM", "PM"]):
#         print("\n\tInvalid Format! Try again. :0")
#         continue

#     hour = int(wlk_time[0])
#     minute = int(wlk_time[1])

#     if (hour < 1) or (hour > 12) or (minute < 0) or (minute > 59):
#         print("\n\tInvalid Time! Try again. :0")
#         continue
#     break

# while True:
#     print("\n\tNote: Please use ")
#     wlk_duration = input("\n\tEnter the duration of walk/daycare (e.g. 60-minutes/24-hours): ").strip().lower().split("-")

#     if (len(wlk_duration) != 2)
