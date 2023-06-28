import json

def filter_json(file_path, output_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    activity_segments = []
    json_array = data['timelineObjects']
    for obj in json_array:
        if 'activitySegment' in obj:
            activity_segment = []
            activity_segment.append({"startLocation":obj['activitySegment']["startLocation"]})
            activity_segment.append({"endLocation":obj['activitySegment']["endLocation"]})
            activity_segment.append({"duration":obj['activitySegment']["duration"]})
            activity_segment.append({"distance":obj['activitySegment']["distance"]})
            activity_segment.append({"activityType":obj['activitySegment']["activityType"]})
            activity_segment.append({"confidence":obj['activitySegment']["confidence"]})
            activity_segments.append(activity_segment)

    with open(output_path, 'w') as output_file:
        json.dump(activity_segments, output_file, indent=4)

# Usage
