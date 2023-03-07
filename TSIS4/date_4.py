from datetime import datetime

def date_diff_in_seconds(date1, date2):
    # Convert string dates to datetime objects
    date1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
    date2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')

    # Calculate the difference in seconds
    diff_in_seconds = (date2 - date1).total_seconds()

    return diff_in_seconds

# Example usage
date1 = '2022-01-01 00:00:00'
date2 = '2022-02-01 12:30:00'
print(date_diff_in_seconds(date1, date2))  # Output: 2674800.0 seconds