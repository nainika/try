# Program to calculate time saved by speeding

# Ask user for input
speedlimit = float(input("Enter the speed limit (mph): "))
speed = float(input("Enter your average speed (mph): "))
distance = float(input("Enter the distance traveled (miles): "))

# Calculate time taken at speed limit and at average speed
speedlimittime = distance / speedlimit  # hours
speedtime = distance / speed  # hours

Minutes_in_hour = 60

# Calculate time saved in minutes
timesaved = (speedlimittime - speedtime) * Minutes_in_hour  # minutes


if timesaved > 0:
    print(f"You saved by speeding {timesaved:.2f} minutes")
elif timesaved == 0:
    print("No time saved")
else:
    print(f"going slower than speed limit")
