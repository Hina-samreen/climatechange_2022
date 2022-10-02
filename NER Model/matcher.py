import pandas as pd

import spacy
import numpy as np

from spacy.matcher import Matcher, PhraseMatcher

df = pd.read_csv("Climate_articles_new-website.csv")
print(df.columns)

print(df.head())

print(df.count())
titles = (_.lower() for _ in df['title'])

nlp = spacy.load("en_core_web_sm")

print(nlp.pipe_names)
# print(random.choices(titles, k=20))
pattern_climate = [
    [{'LOWER': 'climate'}, {'IS_PUNCT': True, 'OP': '?'}, {'POS': 'NOUN', 'OP': '?'}],
    [{'LOWER': 'ozone'}, {'IS_PUNCT': True, 'OP': '?'}, {'POS': 'NOUN', 'OP': '?'}],
    [{'LOWER': {
        'IN': ['atmosphere', 'conservation', 'pollution','ice','glacier', 'ecostress', 'cryosphere', 'energy', 'greenpeace', 'green', 'weather',
               'satellite', 'albedo', 'u.s.', 'biodiversity', 'plastic','methane','air'
               'iceberg', 'planet', 'europe', 'nature', 'reserve','climatologist','energy', 'PMM', 'amazon', 'earth', 'greenland',
               'arctic', 'temperature', 'wildlife', 'water']}}],
    [{'LOWER': {'REGEX': '[A-Z]*forest[?]*'}}, {'IS_PUNCT': True, 'OP': '?'}, {'POS': {'IN': ['PROPN', 'NOUN']}, 'OP': '?'}],
    [{'LOWER': 'atmospheric'}, {'IS_PUNCT': True, 'OP': '?'}, {'TEXT': {'REGEX': '[A-Z]*'}}],
    [{'LOWER': {'REGEX': '[a-z]*'}}, {'LOWER': 'warming'}, {'POS': {'IN': ['PROPN', 'NOUN']}, 'OP': '?'}],
    [{'LOWER': 'heat'}, {'IS_PUNCT': True, 'OP': '?'},{'LOWER': {'REGEX': 'wave[s]?'}}],
    [{'LOWER': 'el'}, {'LOWER': 'niño'}],
    [{'LOWER': 'changing'}, {'LOWER': 'planet'}],
    [{'LOWER': 'sea'}, {'LOWER': {'REGEX': 'level[s]?'}}],
    [{'LOWER': {'REGEX': 'bio?'}}],
    [{'LOWER': 'global'}, {'POS': {'IN': ['PROPN', 'NOUN']}}],
    [{'LOWER': 'warmest'}, {'POS': {'IN': ['PROPN', 'NOUN']}}],
    [{'LOWER': 'sustainable'}, {'POS': {'IN': ['PROPN', 'NOUN']}}],
    [{'LOWER': 'solar'}, {'POS': {'IN': ['PROPN', 'NOUN']}}],
    [{'LOWER': 'fossil'}, {'POS': {'IN': ['PROPN', 'NOUN']}}],
    [{'LOWER': {'REGEX': 'ecosystem[s]?'}}],
    [{'LOWER': {'REGEX': 'glacier[s]?'}}],
    [{'LOWER': {'REGEX': 'climate[s]?'}}],
    [{'LOWER': {'REGEX': 'emission[s]?'}}],
    [{'LOWER': {'REGEX': 'environment[a-z]*'}}],
    [{'LOWER': {'REGEX': 'antarctic[a]?'}}],
    [{'LOWER': {'REGEX': 'temperature[s]?'}}],
    [{'LOWER': {'REGEX': 'aerosol[s]?'}}],
    [{'LOWER': {'REGEX': 'precipitation'}},{'LOWER': {'REGEX': 'measurement'}},{'LOWER': {'REGEX': 'mission[s]?'}}],
    [{'LOWER': {'REGEX': '[a-z]*fire[a-z]*'}}],
    [{'POS': {'IN': ['PROPN', 'NOUN']}, 'OP': '?'}, {'LOWER':  {'REGEX': 'ocean[s]?'}}],
    [{'LOWER': 'carbon'}, {'IS_PUNCT': True, 'OP': '?'},
     {'POS': {'IN': ['PROPN', 'NOUN']}, 'LOWER': {'REGEX': '[a-z]*'}}]]

print(pattern_climate)

matcher = Matcher(nlp.vocab)
matcher.add("climate", pattern_climate)
# matcher.add("climate_change", [pattern_climate_change])

string = 'Spring-like'
print(string.lower())

label_df = (pd.read_csv('label_it_tab_seperated_new.txt', delimiter="\t"))[['label', 'title']] \
    .assign(Pred=lambda d: [len(matcher(d)) > 0 for d in nlp.pipe(d['title'])]) \
    .assign(Pred=lambda d: d['Pred'].astype(np.int8))

mistakes = label_df.loc[lambda d: d['Pred'] == 0].loc[lambda d: d['label'] == 1]['title']

doc = nlp('carbon dioxide')
for i in doc:
    print(i.text, i.pos_)
print(len(mistakes))

j = 1
for i in range(50):
    print(mistakes.iloc[i])


# for idx, start, end in matcher(doc):
# print(doc[start:end])
