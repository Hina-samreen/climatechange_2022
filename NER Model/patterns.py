
def create_patterns():

    pattern_climate = [
        [{'LOWER': 'climate'}, {'IS_PUNCT': True, 'OP': '?'}, {'POS': 'NOUN', 'OP': '?'}],
        [{'LOWER': 'ozone'}, {'IS_PUNCT': True, 'OP': '?'}, {'POS': 'NOUN', 'OP': '?'}],
        [{'LOWER': {
            'IN': ['atmosphere', 'conservation', 'pollution', 'ice', 'glacier', 'ecostress', 'cryosphere', 'energy',
                   'greenpeace', 'green', 'weather',
                   'satellite', 'albedo', 'u.s.', 'biodiversity', 'plastic', 'methane', 'air'
                                                                                        'iceberg', 'planet', 'europe',
                   'nature', 'reserve', 'climatologist', 'energy', 'PMM', 'amazon', 'earth', 'greenland',
                   'arctic', 'temperature', 'wildlife', 'water']}}],
        [{'LOWER': {'REGEX': '[A-Z]*forest[?]*'}}, {'IS_PUNCT': True, 'OP': '?'},
         {'POS': {'IN': ['PROPN', 'NOUN']}, 'OP': '?'}],
        [{'LOWER': 'atmospheric'}, {'IS_PUNCT': True, 'OP': '?'}, {'TEXT': {'REGEX': '[A-Z]*'}}],
        [{'LOWER': {'REGEX': '[a-z]*'}}, {'LOWER': 'warming'}, {'POS': {'IN': ['PROPN', 'NOUN']}, 'OP': '?'}],
        [{'LOWER': 'heat'}, {'IS_PUNCT': True, 'OP': '?'}, {'LOWER': {'REGEX': 'wave[s]?'}}],
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
        [{'LOWER': {'REGEX': 'precipitation'}}, {'LOWER': {'REGEX': 'measurement'}},
         {'LOWER': {'REGEX': 'mission[s]?'}}],
        [{'LOWER': {'REGEX': '[a-z]*fire[a-z]*'}}],
        [{'POS': {'IN': ['PROPN', 'NOUN']}, 'OP': '?'}, {'LOWER': {'REGEX': 'ocean[s]?'}}],
        [{'LOWER': 'carbon'}, {'IS_PUNCT': True, 'OP': '?'},
         {'POS': {'IN': ['PROPN', 'NOUN']}, 'LOWER': {'REGEX': '[a-z]*'}}]]

    return pattern_climate

