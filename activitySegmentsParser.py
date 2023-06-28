import pandas as pd
import json
from datetime import datetime

def calculate_elapsed_time(start_timestamp, end_timestamp):
    #I am sure there is a better way of doing this, but I couldn't figure it out - issue is some had milliseconds and some didn't, this makes sure the formatting works /s
    try:
        start_dt = datetime.strptime(start_timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        start_dt = datetime.strptime(start_timestamp, "%Y-%m-%dT%H:%M:%SZ")
    try:
        end_dt = datetime.strptime(end_timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        end_dt = datetime.strptime(end_timestamp, "%Y-%m-%dT%H:%M:%SZ")
    elapsed_seconds = (end_dt - start_dt).total_seconds()
    return elapsed_seconds

def constructDataFrame(jsonFile):
    df = pd.DataFrame(columns=["Start Location", "End Location", "Distance", "Start Time", "End Time", "Elapsed Time", "Method of Transport", "Confidence"])


    with open(jsonFile, 'r') as file:
        data = json.load(file)
    for i in data:
        startLoc = [i[0]['startLocation']['latitudeE7'],i[0]['startLocation']['longitudeE7']]
        endLoc = [i[1]['endLocation']['latitudeE7'],i[1]['endLocation']['longitudeE7']]
        distance = i[3]['distance']
        startTime = i[2]['duration']['startTimestamp']
        endTime = i[2]['duration']['endTimestamp']
        elapsedTime = calculate_elapsed_time(startTime,endTime)
        transport = i[4]['activityType']
        confidence = i[5]['confidence']

        # Add the values to the DataFrame
        df = df._append({'Start Location': startLoc, 'End Location': endLoc, 'Distance': distance, "Start Time": startTime, "End Time":endTime, "Elapsed Time": elapsedTime, "Method of Transport": transport, "Confidence":confidence}, ignore_index=True)
    return df