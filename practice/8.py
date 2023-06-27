from datetime import datetime, timedelta

print("Please select one of the following options: add, compare")
option = input()

if option == "add":
    date_str = input("What is the date you want to add to? Please enter in DD/MM/YYYY format: ")
    days_to_add = int(input("How many days do you want to add? "))

    date = datetime.strptime(date_str, "%d/%m/%Y")
    new_date = date + timedelta(days=days_to_add)

    resultant_date = new_date.strftime("%d/%m/%Y")
    print("The resultant date is", resultant_date)

elif option == "compare":
    date1_str = input("Please give Date 1 in DD/MM/YYYY format: ")
    date2_str = input("Please give Date 2 in DD/MM/YYYY format: ")

    date1 = datetime.strptime(date1_str, "%d/%m/%Y")
    date2 = datetime.strptime(date2_str, "%d/%m/%Y")

    diff_days = abs((date1 - date2).days)

    print("There are", diff_days, "days between the given dates.")
else:
    print("Invalid option selected. Please try again.")

