mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

print("Total number of missions: " + str(len(mission_names))) # print total number of missions

print("Number of successful missions: " + str(mission_success.count(True))) # count and print number of successful missions

mission_success_rate = round(mission_success.count(True)/len(mission_success)*100, 2) # calculate success rate, round to nearest hundredth, store in variable
mission_success_rate_string = str(mission_success_rate) # convert float to string and store in new variable
print("Success rate: " + mission_success_rate_string + "%") # print sentence with success rate

print("Missions launched before the year 2000:")
for x in (mission_names): # list all mission names except Curiosity Rover because it happened after 2000
    if x == "Curiosity Rover":
        continue # skip Curiosity Rover in mission_names
    print("- " + x) # print missions that happened before 2000