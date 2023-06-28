import geopy.distance

from jsonCleaner import *
from activitySegmentsParser import *
from statsFinder import *


def main():
    #Step one, read raw data and extract only what we want
    print("COMPILING ACTIVITY SEGMENTS ...")
    json_file_path = 'RawData/2022_FEBRUARY.json'
    output_file_path = 'ProcessedData/activitySegments.json'
    filter_json(json_file_path, output_file_path)

    #Step two, turn this into a dataframe and catagorize the useful info
    print("CONSTRUCTING DATAFRAME ...")
    json_file_path = 'ProcessedData/activitySegments.json'
    extractedDataDF = (constructDataFrame(json_file_path))

    print("BUILDING STATS")
    print(totalStatsPerActivity(extractedDataDF))



if __name__ == "__main__":
    main()