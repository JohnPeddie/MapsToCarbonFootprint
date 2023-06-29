# File containing references for average carbon emmisons by type of transport, Up to date CSV from: https://ourworldindata.org/travel-carbon-footprint
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


def matchActivityTypes(key):
    activityTypesDict = {"BOATING": "Sport",
                         "CATCHING_POKEMON": "Walking",
                         "CYCLING": "Sport",
                         "FLYING": "Long-haul flight (economy)",
                         "HIKING": "Sport",
                         "HORSEBACK_RIDING": "Sport",
                         "IN_BUS": "Bus",
                         "IN_CABLECAR": "Light rail and tram",
                         "IN_FERRY": "Ferry (foot passenger)",
                         "IN_FUNICULAR": "Light rail and tram",
                         "IN_GONDOLA_LIFT": "Light rail and tram",
                         "IN_PASSENGER_VEHICLE": "Small car (petrol)",
                         "IN_SUBWAY": "London Underground",
                         "IN_TAXI": "Black cab (taxi)",
                         "IN_TRAIN": "National rail",
                         "IN_TRAM": "Light rail and tram",
                         "IN_VEHICLE": "Small car (petrol)",
                         "IN_WHEELCHAIR": "Walking",
                         "KAYAKING": "Sport",
                         "KITESURFING": "Sport",
                         "MOTORCYCLING": "Motorcycle (small)",
                         "PARAGLIDING": "Sport",
                         "ROWING": "Sport",
                         "RUNNING": "Sport",
                         "SAILING": "Sport",
                         "SKATEBOARDING": "Sport",
                         "SKATING": "Sport",
                         "SKIING": "Sport",
                         "SLEDDING": "Sport",
                         "SNOWBOARDING": "Sport",
                         "SNOWMOBILE": "Motorcycle (medium)",
                         "SNOWSHOEING": "Sport",
                         "STILL": "Walking",
                         "SURFING": "Sport",
                         "SWIMMING": "Sport",
                         "UNKNOWN_ACTIVITY_TYPE": "Small car (petrol)",
                         "WALKING": "Walking",
                         "WALKING_NORDIC": "Sport"}
    return activityTypesDict[key]


def generateCarbonEmissionsDF(carbonEmissionsCSV, activityTypesCSV):
    carbonEmissionsDF = pd.read_csv(carbonEmissionsCSV)
    activityTypesDF = pd.read_csv(activityTypesCSV)
    carbonEmissionsDF = addWalkingAndSport(carbonEmissionsDF)
    print(carbonEmissionsDF)
    for index, row in activityTypesDF.iterrows():
        queryString = str(matchActivityTypes(row["Activity Type"]))
        print(queryString)
        print(carbonEmissionsDF.query("Entity == '"+queryString+"'")["GHG emissions (gCO2e/km)"])
        activityTypesDF= activityTypesDF._append({"GHG emissions (gCO2e/km)":(carbonEmissionsDF.query("Entity == '"+queryString+"'")["GHG emissions (gCO2e/km)"])},ignore_index=True)
    print(activityTypesDF)
    return carbonEmissionsDF

def addWalkingAndSport(carbonEmissionsDF):
    carbonEmissionsDF= carbonEmissionsDF._append({"Entity": 'Walking', "GHG emissions (gCO2e/km)": 0},ignore_index=True)
    carbonEmissionsDF = carbonEmissionsDF._append({"Entity": "Sport", "GHG emissions (gCO2e/km)": 0},ignore_index=True)
    return carbonEmissionsDF