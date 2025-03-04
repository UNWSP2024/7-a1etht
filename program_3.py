#Programmer: Alethea Lo
#Date: 3/3/25
#Title: US_Population

#Initialize an empty list to store the data
population_data = []

#Loop to collect user input
done = False
while not done:
    try:
        year = int(input("Enter year: "))
        state = input("Enter state name: ")
        population = int(input("Enter population: "))

        if population < 0:
            print("Population cannot be negative. Try again.")
            continue

        #Store the data as a list inside the main list
        population_data.append([year, state, population])

        #Ask user if they want to continue
        more = input("Do you want to enter another record? (yes/no): ").strip().lower()
        if more != 'yes':
            done = True
    except ValueError:
        print("Invalid input. Please enter numerical values for year and population.")

#Inputing year for population sum
target_year = int(input("Enter a year to calculate total population: "))

#Calculate the total population for the given year
total_population = sum(record[2] for record in population_data if record[0] == target_year)

#Display the result
print(f"Total population for the year {target_year}: {total_population}")