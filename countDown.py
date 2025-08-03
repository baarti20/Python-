from datetime import datetime

def calculate_time_left(date_time_str):
    # Parse the input date-time string
    date_time = datetime.strptime(date_time_str, "%b %d %Y %I:%M %p")

    # Calculate the next new year's date-time
    next_new_year = datetime(date_time.year + 1, 1, 1, 0, 0)

    # Calculate the difference in total seconds
    time_diff = next_new_year - date_time
    total_seconds = time_diff.days * 24 * 3600 + time_diff.seconds

    # Convert total seconds to hours and minutes
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60

    # Return the time left in the specified format
    return f"{hours} hours {minutes} minutes"

# Get the input date-time from the user
date_time_str = input()

# Calculate and print the time left
time_left = calculate_time_left(date_time_str)
print(time_left)
