import pandas
import json

oldScore = 0
addPoints = int(input("How many points to add? "))
newScore = oldScore + addPoints

# Open file
try:
    with open("CSBoysScore.json", "r") as file:
        # Read old data
        data = json.load(file)
except FileNotFoundError:
    with open("CSBoysScore.json", "w") as file:
        # Create new data
        json.dump(0, file, indent=4)

else:
    with open("CSBoysScore.json", "w") as file:
        # Update data with new data
        data.update(1)
        json.dump(2, file, indent=4)

