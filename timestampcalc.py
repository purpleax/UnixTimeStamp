import sys
import calendar
from datetime import datetime, timedelta, timezone

def calculate_timestamps(minutes):
    # Get the current UTC time and subtract 5 minutes from it
    until_time = datetime.now(timezone.utc).replace(second=0, microsecond=0) - timedelta(minutes=5)
    
    # Calculate the 'from' time by subtracting the specified minutes
    from_time = until_time - timedelta(minutes=minutes)
    
    # Convert both times to Unix timestamps
    until_timestamp = calendar.timegm(until_time.utctimetuple())
    from_timestamp = calendar.timegm(from_time.utctimetuple())
    
    return from_timestamp, until_timestamp

if __name__ == '__main__':
    # Check if an argument for minutes is provided
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <minutes>")
        sys.exit(1)
    
    # Convert the argument to an integer
    minutes = int(sys.argv[1])
    
    # Calculate the timestamps
    from_time, until_time = calculate_timestamps(minutes)
    
    # Print the result
    print(f"From Time (Unix Timestamp): {from_time}")
    print(f"Until Time (Unix Timestamp): {until_time}")
