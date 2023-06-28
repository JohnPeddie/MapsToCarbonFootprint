import pandas as pd

def totalStatsPerActivity(df):
    totalStatsDict = {}
    totalTimesList = []
    totalDistanceList = []
    activities = []
    activitiesCleaned = []
    for index, row in df.iterrows():
        activities.append(row["Method of Transport"])
    for value in activities:
        # Check if the value is not already in the unique list
        if value not in activitiesCleaned:
            # Add the value to the unique list
            activitiesCleaned.append(value)
    for i in activitiesCleaned:
        totalTimesList.append(timePerActivity(i,df))
        totalDistanceList.append(distancePerActivity(i,df))

    totalStatsDict["Method of Transport"] = activitiesCleaned
    totalStatsDict["Total Elapsed Time"] = totalTimesList
    totalStatsDict["Total Distance Travelled"]= totalDistanceList

    totalStatsDF = pd.DataFrame(totalStatsDict)



    return totalStatsDF

def timePerActivity(activity,df):
    time =0
    for index, row in df.iterrows():
        if row['Method of Transport'] == activity:
            time += row["Elapsed Time"]
    return time

def distancePerActivity(activity,df):
    distance = 0
    for index, row in df.iterrows():
        if row['Method of Transport'] == activity:
            distance += row["Distance"]
    return distance
