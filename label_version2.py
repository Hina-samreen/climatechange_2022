#using imports
import pandas as pd
from patterns import create_patterns
from spacy.matcher import Matcher
import spacy
from spacy import displacy
from spacy.training import Example
import datetime as dt
from spacy.util import minibatch, compounding

#using create_patterns() from patterns.py file
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab, validate=True)
matcher.add("climate", create_patterns())

#creating a method to parse the training data
def parse_train_data(text1):
    doc1 = nlp(text1)
    detections = [(doc1[start:end].start_char, doc1[start:end].end_char, 'climate') for idx, start, end in
                  matcher(doc1)]
    return doc1.text, {'entities': detections}


df = (pd.read_csv("Wiki-Doc-Train.txt", sep='\t', usecols=['label', 'sentence']))
titles = df.loc[lambda d: d['label'] == 1]['sentence']

#creating training data
TRAIN_DATA = [parse_train_data(d) for d in nlp.pipe(titles) if len(matcher(d)) == 1]

#method for training the blank NLP
def create_blank_nlp(train_data):
    nlp1 = spacy.blank("en")
    nlp1.add_pipe("ner")
    ner = nlp1.get_pipe("ner")
    for _, annotations1 in train_data:
        for ent in annotations1.get("entities"):
            ner.add_label(ent[2])
    return nlp1

nlp2 = create_blank_nlp(TRAIN_DATA)

#training has begun
optimizer = nlp2.begin_training()
for i in range(20):
    losses = {}
    batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.001))
    for batch in batches:
        for text, annotations in batch:
            doc = nlp2.make_doc(text)
            example = Example.from_dict(doc, annotations)
            nlp2.update(
                [example],  # batch of texts
                drop=0.1,  # dropout - make it harder to memorise data
                losses=losses
            )
    print(f"Losses at iteration {i} - {dt.datetime.now()} {losses} ")

print(nlp2.pipeline)

df1 = pd.read_csv("climate_articles_new_withYear.csv", usecols=['date', 'title', 'URL', 'Year'])

values = df1.values.tolist()

# for value in values:
# print(value[0])

# nlp = spacy.load("en_core_web_sm")
entities = []

for title in values:
    doc2 = nlp2(title[1])
    if not len(doc2.ents) == 0:
        entities.append([doc2.ents, title[1], title[2], title[0], title[3]])  # ents,title, URL, date,Year
for entity in entities:
    print(entity[0])

records = []
new_records = []
for value in entities:
    j = 1
    for i in range(len(value[0])):
        subjects = value[0][i]
        objects = (value[1].__str__())[0:15] + "..."
        titles = value[1]
        relationships = value[2]
        dates = value[3]
        Year = value[4]
        new_records.append((subjects, objects, relationships, dates, titles, Year))
    j = j + 1

df2 = pd.DataFrame(new_records, columns=['subjects', 'objects', 'relationships', 'dates', "titles", "Year"])
df2.to_csv("relationships_version4_sept29.csv")

df3 = pd.read_csv("relationships_version4_sept29.csv", usecols=["subjects", "objects"])

raw_values_subject = [_.lower() for _ in df3['subjects']]
raw_values_object = [_.lower() for _ in df3['objects']]
# raw_values = [_.lower() for _ in df3['subjects','objects']] - doesnt work

values_subject = set(df3["subjects"].values)
values_object = set(df3["objects"].values)

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
    page_rank = raw_values_subject.count(subject1)
    id_label = id_label + 1
    community = 1
    community_subjects.append((subject1, community))
    records_subject.append((subject1, id_label, page_rank, community))

for obj in values_object:
    if obj not in records:
        obj1 = obj.lower()
        community = 2
        page_rank = raw_values_object.count(obj1)
        id_label = id_label + 1
        records_subject.append((obj1, id_label, page_rank, community))

df4 = pd.DataFrame(records_subject, columns=["name", "id", "page_rank", "community"])
df4.to_csv("names_version4_sept29.csv")
