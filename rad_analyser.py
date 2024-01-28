locations = [
    "City Centre", 
    "Industrial Zone", 
    "Residential District", 
    "Rural Outskirts", 
    "Downtown"
    ]

levels = [
    [22.00, 19.00, 20.00, 31.00, 28.00],
    [35.00, 32.00, 30.00, 37.00, 40.00],
    [15.00, 12.00, 18.00, 20.00, 14.00],
    [9.00, 13.00, 16.00, 14.00, 7.00],
    [25.00, 18.00, 22.00, 21.00, 26.00]
]

import math

def calc_avg(levels):
    return sum(levels) / len(levels)

def calc_sd(levels):
    mean = sum(levels) / len(levels)
    var = sum(pow(x - mean,2) for x in levels) / len (levels)
    std = math.sqrt(var)
    return std

print("""Welcome to the Radiation Analyser.\n""")

for i, location in enumerate(locations):
    # Average
    print(f"Debug: Processing location {location} with levels {levels[i]}\n")
    
    average = calc_avg(levels[i])
    
    print(f"{location} Average Radiation Level: {average:.2f}\n")

    # SD
    sd = calc_sd(levels[i])

    print(f"{location} Standard Deviation of Radiation level: {sd:.2f}\n")
    
measurements = []

while True:
    
    level = input("Enter radiation level ('done' to finish):\n")

    if level.lower() == 'done':    
        print("Debug: Exiting input loop.")
        break
    
    try:
        new_level = int(level)
        measurements.append(new_level)
        
        print(f"Debug: Added level {new_level}")
    
    except ValueError:
            print("Invalid input. Please enter a valid number or 'done'.")


if measurements:

    average = calc_avg(measurements)
    sd = calc_sd(measurements)
    print(f"New Measurements Average Radiation Level: {average:.2f}")
    print(f"New Measurements Standard Deviation of Radiation Level: {sd:.2f}")

else:
    print("Debug: No new measurements were entered.")

