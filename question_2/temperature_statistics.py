# Program: temperature_statistics.py
# Author: Princyben Chetankumar Patel, Lamia Sarwar
# Student ID: S388343, S390060

import os

# Define seasons constants based on Australian seasons.
SEASONS = {
    'Spring': ['September', 'October', 'November'],
    'Summer': ['December', 'January', 'February'],
    'Autumn': ['March', 'April', 'May'],
    'Winter': ['June', 'July', 'August']
}

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

TEMPERATURE_DATA_PATH = 'temperature_data'


########################################################
# Functions
########################################################


def read_temperature_data():
    """ reads the temperature data from the csv files and returns a list of dictionaries """
    data = []
    files = os.listdir(TEMPERATURE_DATA_PATH)
    

    # these keys exist on all csv file
    csv_keys = [
        'STATION_NAME',
        'STATION_ID',
        'LAT',
        'LON',
        *MONTHS
    ]
    
    for file in files:
        with open(f'{TEMPERATURE_DATA_PATH}/{file}', 'r') as f:
            # skip the header line
            for line in f.readlines()[1:]:
                # csv are separated by commas, so we need to split by commas.
                line = line.strip().split(',')
                data.append(dict(zip(csv_keys, line)))
    return data

def calculate_seasonal_averages(data):
    """ calculates the seasonal averages of the temperature data """

    seasonal_totals = dict()
    seasonal_counts = dict()

    for season in SEASONS:
        seasonal_totals[season] = 0
        seasonal_counts[season] = 0
    

    # Process each station -> each season -> each month.
    # Calculate the total and count of temperature for each season.
    # Divide those to get the average.
    for station in data:
        for season, season_months in SEASONS.items():
            season_temp = 0
            count = 0
            for season_month in season_months:
                if season_month in station:
                    try:
                        season_temp += float(station[season_month])
                        count += 1
                    except ValueError:
                        print(f"Invalid Data found for {station['STATION_NAME']} in {season_month}")
                        exit()
            if count > 0:
                seasonal_totals[season] += season_temp / count
                seasonal_counts[season] += 1
    
    seasonal_averages = dict()
    for season in seasonal_totals:
        average_temp = seasonal_totals[season] / seasonal_counts[season]
        seasonal_averages[season] = average_temp
    return seasonal_averages

def find_largest_temp_range(data):
    """ finds the stations with the largest temperature range """
    max_range = 0
    max_range_stations = []
    station_ranges = []
    
    for station in data:
        temps = []
        for month in MONTHS:
            if month in station:
                try:
                    temps.append(float(station[month]))
                except ValueError:
                    print(f"Invalid Data found for {station['STATION_NAME']} in {month}")
                    exit()

        if temps:
            # Calculate maximum gap between the highest and lowest temperature.
            temp_range = max(temps) - min(temps)
            station_ranges.append((station['STATION_NAME'], temp_range))
            if temp_range > max_range:
                max_range = temp_range

    for station in station_ranges:
        if station[1] == max_range:
            max_range_stations.append(station[0])

    return max_range_stations, max_range

def find_warmest_and_coolest_stations(data):
    """ finds the warmest and coolest stations """
    station_avgs = []
    
    for station in data:
        temps = []
        for month in MONTHS:
            if month in station:
                try:
                    temps.append(float(station[month]))
                except ValueError:
                    print(f"Invalid Data found for {station['STATION_NAME']} in {month}")
                    exit()
            
        
        if temps:
            avg_temp = sum(temps) / len(temps)
            station_avgs.append((station['STATION_NAME'], avg_temp))
    
    # Sort the stations by average temperature.
    station_avgs.sort(key=lambda x: x[1])
    
    warmest_temp = station_avgs[-1][1]
    coolest_temp = station_avgs[0][1]

    warmest_stations = []
    coolest_stations = []

    for station in station_avgs:
        if station[1] == warmest_temp:
            warmest_stations.append(station[0])
        elif station[1] == coolest_temp:
            coolest_stations.append(station[0])

    return warmest_stations, coolest_stations, warmest_temp, coolest_temp

########################################################
# Main Program
########################################################

data = read_temperature_data()

seasonal_averages = calculate_seasonal_averages(data)
max_range_stations, max_range = find_largest_temp_range(data)
warmest_stations, coolest_stations, warmest_temp, coolest_temp = find_warmest_and_coolest_stations(data)

with open('average_temp.txt', 'w') as f:
    f.write("Seasonal Average Temperatures:\n")
    for season, avg in seasonal_averages.items():
        f.write(f"{season}: {avg:.2f}°C\n")

with open('largest_temp_range_station.txt', 'w') as f:
    f.write("Stations with Largest Temperature Range:\n")
    for station in max_range_stations: 
        f.write(f"{station}: {max_range:.2f}°C range\n")

with open('warmest_and_coolest_station.txt', 'w') as f:
    f.write("Warmest Stations:\n")
    for station in warmest_stations:    
        f.write(f"{station}: {warmest_temp:.2f}°C average\n")
    f.write("\nCoolest Stations:\n")
    for station in coolest_stations:
        f.write(f"{station}: {coolest_temp:.2f}°C average\n")


