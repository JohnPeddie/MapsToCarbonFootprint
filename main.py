import geopy.distance

from jsonCleaner import *
from activitySegmentsParser import *
from statsFinder import *
from AverageCarbonEmissionsByActivity import *


def main():
    #Step one, read raw data and extract only what we want
    print("COMPILING ACTIVITY SEGMENTS ...")
    json_file_path = 'RawData/mapsCheckoutData/2022_FEBRUARY.json'
    output_file_path = 'ProcessedData/fromMapsTakeoutData/activitySegments.json'
    filter_json(json_file_path, output_file_path)

    #Step two, turn this into a dataframe and catagorize the useful info
    print("CONSTRUCTING DATAFRAME ...")
    json_file_path = 'ProcessedData/fromMapsTakeoutData/activitySegments.json'
    extractedDataDF = (constructDataFrame(json_file_path))

    #Step three, Use this DF to extract useful info
    print("BUILDING STATS ...")
    print(totalStatsPerActivity(extractedDataDF))

    #Step four, build a dataframe of average carbon emmissions and compare to stats dataframe
    carbonEmissionsCSVPath = "RawData/CarbonFootprint/carbon-footprint-travel-mode.csv"
    takeoutActivityTypes = 'RawData/CarbonFootprint/googleTakeoutActivityTypes.csv'
    print(generateCarbonEmissionsDF(carbonEmissionsCSVPath, takeoutActivityTypes))



if __name__ == "__main__":
    main()