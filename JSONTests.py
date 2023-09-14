import json
from itertools import groupby
from collections import defaultdict


''' Load json - testing purpose'''
data = (json.load(open('testjson.json')))

'''First, create set of available periods from our dataset - CREATED not PERIOD, which is 7 char string YYYY-MM'''
possible_periods = set(period["created"][:7] for period in data["items"])
print(possible_periods)
'''Sort the items by the "created" key'''
data["items"].sort(key=lambda x: x["created"])

'''Group the items by the "created" key with the "year-month" format'''
grouped_data = defaultdict(list)
for key, group in groupby(data["items"], key=lambda x: x["created"][:7]):
    group_list = list(group)
    grouped_data[key] = {
        "count": len(group_list),
        "items": group_list
    }

task_1_result_dict = {}

for created in sorted(possible_periods):
    count = grouped_data[created]['count'] if created in grouped_data else 0
    task_1_result_dict[created] = count

print(task_1_result_dict)