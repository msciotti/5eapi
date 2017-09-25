import json
from pprint import pprint

with open('bard.json') as data_file:    
    class_json = json.load(data_file)

fixed = open('fixed_bard.json', 'w')
class_json = class_json['Bard']['Class Features']

modifier = 'CHA'
hit_dice = class_json['Hit Points']['content'][0]
first_level = class_json['Hit Points']['content'][1]
higher_level = class_json['Hit Points']['content'][2]

proficiencies = {}
proficiencies['Armor'] = class_json['Proficiencies']['content'][0]
proficiencies['Weapons'] = class_json['Proficiencies']['content'][1]
proficiencies['Tools'] = class_json['Proficiencies']['content'][2]
proficiencies['Saving Throws'] = class_json['Proficiencies']['content'][3]
proficiencies['Skills'] = []

starting_equipment = class_json['Equipment']['content']

level_table = class_json['The Bard']['table']
levels = []

for i in range (0, 20):
    level = {
        '{}'.format(i + 1): {
            #'Proficiency': level_table['Proficiency Bonus'][i],
            'Features': level_table['Features'][i],
            'Spells Known': level_table['Spells Known'][i],
            'Cantrips Known': level_table['Cantrips Known'][i]
        }
    }
    levels.append(level)

fixed_class = {
    'Bard': {
        'Modifier': modifier,
        'Hit Dice': hit_dice,
        'First Level': first_level,
        'Higher Levels': higher_level,
        'Proficiencies': proficiencies,
        'Starting Equipment': starting_equipment,
        'Levels': levels
    }
}

fixed.write(json.dumps(fixed_class, indent = 4 ))