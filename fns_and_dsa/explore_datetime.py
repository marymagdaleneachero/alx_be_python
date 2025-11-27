from datetime import datetime, timedelta


# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Save the current date and time
    current_date = datetime.now()

    # Format the date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    # Print the formatted date and time
    print("Current date and time:", formatted_date)


# Part 2: Calculate a Future Date
def calculate_future_date(days_to_add):
    # Current date
    current_date = datetime.now()

    # Save the future date inside a variable
    future_date = current_date + timedelta(days=days_to_add)

    # Print the future date in YYYY-MM-DD format
    print("Future date:", future_date.strftime("%Y-%m-%d"))


# Main program execution
if __name__ == "__main__":
    # Display current date/time
    display_current_datetime()

    # Ask user for number of days
    days = int(input("Enter the number of days to add to the current date: "))

    # Calculate future date
    calculate_future_date(days)
