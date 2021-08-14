last_week_of_month = input("Is it the last week of the mounth?(Answer like y/n) :")
today = input("Enter day name: ")
if last_week_of_month == 'y':
    if today == 'friday':
        print("Wear green clothes")
    else:
        print("Don't wear green clothes")

else:
    if today == 'thursday':
        print("Wear green clothes")
    else:
        print("Don't wear green clothes")
