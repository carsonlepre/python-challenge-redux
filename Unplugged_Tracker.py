#Import libraries.
import csv
import os

#Declare variables with empty lists to collect details of unplugged vehicles to log after print statement.
unplugged_vehicle_id = []
unplugged_vehicle_location = []
unplugged_vehicle_access_group = []

#Declare a variable to locate source file.
csvpath = os.path.join("scooterdata.csv")

#Open csv and prepare to rock and roll.
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
#for loop scanning through the appropriate rows to see which vehicles are both 'in a garage' and 'not charging.' 
    for row in csvreader:
        if row[0].isdigit():
            if (int(row[0])) >= 450 and row[8] == "true" and row[12] == "false":
            #Updates lists with data for logging
                unplugged_vehicle_id.append(row[0])
                unplugged_vehicle_location.append(row[7])
                unplugged_vehicle_access_group.append(row[4])
                #prints a helpful phrase letting the dispatcher know which vehicles need to be plugged in where.
                print("Vehicle number " + row[0] + " needs to be plugged in at " + row[7] + ". " "It is in " + row[4] + " access group.")
print("There are "  + str(len(unplugged_vehicle_id)) + " vehicles that need attention.")

# #Creating a log for future reference.
with open("Unplugged_Log.md", "w") as output:
    for i in range(len(unplugged_vehicle_id)):
        output.write(f"Vehicle number {unplugged_vehicle_id[i]} was unplugged at {unplugged_vehicle_location[i]}. It was in {unplugged_vehicle_access_group[i]} access group."'\r')
    output.write(f"There were "  + str(len(unplugged_vehicle_id)) + " vehicles that needed attention."'\r')