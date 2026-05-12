# day = input("Enter the day: ").lower

# if day == "Saturday" or day == "Sunday":
#  if day == "Saturday":
#     print("It's laundry day.")
#     else:
#     print("Prepare for nextweek.")
#     else:
# if day == "Monday":
#     print("Work na naman!")
# elif day == "Friday":
#     print("Thank God it's friday!")
# elif day == "Tuesday" or day == "Wednesday" or day == "Thursday":
#     print("Regular work week.")
# else:
#     print("Invalid Input.")

day = input("Enter the day: ")

if day == "saturday" or day == "sunday":
    if day == "saturday":
        print("It's laundry day.")
    else:
        print("Prepare for next week.")
elif day == "monday":
    print("Work na naman!")
elif day == "friday":
    print("Thank God it's Friday!")
elif day == "tuesday" or day == "wednesday" or day == "thursday":
    print("Regular work week.")
else:
    print("Invalid Input.")

