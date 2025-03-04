#Programmer: Alethea Lo
#Date: 3/3/25
#Title: Larger than n

def display_greater_numbers(num_list, n):
    """Displays numbers from num_list that are greater than n."""
    for num in num_list:
        if num > n:
            print(num)

#Example of usage:
numbers = [10, 25, 3, 50, 7, 30]
threshold = 20
display_greater_numbers(numbers, threshold)