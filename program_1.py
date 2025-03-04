#Programmer: Alethea Lo
#Date: 3/3/25
#Title: Rainfall

#List of month names
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#Initialize an empty list to store rainfall values
rainfall = []

#Obtain rainfall information by USER
for month in months:
    while True:
        try:
            amount = float(input(f"Enter rainfall for {month}: "))
            if amount < 0:
                print("Rainfall cannot be negative. Please enter a valid amount.")
            else:
                rainfall.append(amount)
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

#Calculating the total and average rainfall
total_rainfall = sum(rainfall)
average_rainfall = total_rainfall / 12

#Finding the highest and lowest rainfall months
max_rainfall = max(rainfall)
min_rainfall = min(rainfall)
max_month = months[rainfall.index(max_rainfall)]
min_month = months[rainfall.index(min_rainfall)]

#Display results
print("\nRainfall Summary:")
print(f"Total rainfall for the year: {total_rainfall:.2f} inches")
print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
print(f"Month with highest rainfall: {max_month} ({max_rainfall:.2f} inches)")
print(f"Month with lowest rainfall: {min_month} ({min_rainfall:.2f} inches)")