import pandas as pd
from collections import Counter
import datetime
import time

climate_string = "there is n effects of cilmate to be seen anywhere? Have you seen it?"

print(len(climate_string.split()))
i = 1

print(climate_string.split(' ', 3))
print(climate_string[0:15] + "...")
print("climate change")

df = pd.read_csv("climate_trial-error_version3.csv", usecols=["objects"])
df_new_weight = pd.read_csv("climate_trial-error_version3.csv")

N = ["climate", "climate", "junk", "junk", "junk", "mango", "mango"]
C = Counter(N)

print([[k, ] * v for k, v in C.items()])

# calculating weight for a relationship
print(len(df.values))
records = []
records_count = []
for value in [df.values]:
    count = 0
    for i in range(len(df.values)):
        if i < len(df.values):
            if value[i - 1] == value[i]:
                count = count + 1
                if value[i] == value[i + 1]:
                    count = count + 1
            else:
                count = 0
        else:
            break
        records.append(((value[i]), count))
        records_count.append(count)
print(records_count.__len__())
df_new_weight['weight'] = records_count
df_new_weight.to_csv("trial_error_count_for_weight_version2.csv")
print(len(records))

df1 = pd.DataFrame(records, columns=["title", "count"])
df1.to_csv("trial_error_count_for_weight.csv")

# calculating page rank - to show the importance of a node

df3 = pd.read_csv("climate_trial-error_version3.csv", usecols=["subjects", "objects"])
print("df3 raw values" + len(df3.values).__str__())
raw_values_subject = [_.lower() for _ in df3['subjects']]
raw_values_object = [_.lower() for _ in df3['objects']]
# raw_values = [_.lower() for _ in df3['subjects','objects']] - doesnt work

values_subject = set(df3["subjects"].values)
values_object = set(df3["objects"].values)

print(len(values_object))
print(values_object)
for object1 in values_object:
    print(object1[0], object1[1])
    print()
# values_intersection = values_subject.intersection(values_object)
# print(len(values_subject), len(values_object), len(values_intersection))

records_subject = []
community_subjects = []
records_object = []
id_label = 0
records = []
page_rank = 0
i = 1
community = 0
for subject in values_subject:
    subject1 = subject.lower()
    print(subject1)
    page_rank = raw_values_subject.count(subject1)
    print(page_rank)
    id_label = id_label + 1
    community = community + 1
    community_subjects.append((subject1, community))
    records_subject.append((subject1, id_label, page_rank, community))

for value in community_subjects:
    print(value[0], value[1])

for obj in values_object:
    if obj not in records:
        obj1 = obj.lower()
        community = 2
        page_rank = raw_values_object.count(obj1)
        id_label = id_label + 1
        records_subject.append((obj1, id_label, page_rank, community))

print(len(records_subject))
print(len(records_object))

df4 = pd.DataFrame(records_subject, columns=["name", "id", "page_rank", "community"])
df4.to_csv("names_message_version3_trial.csv")

df5 = pd.read_csv("names_message_version3_trial.csv", usecols=['name'])
