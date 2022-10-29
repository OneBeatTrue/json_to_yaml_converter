import json
import yaml

f = open('timetable.json', 'r', encoding='utf-8')
f = ''.join(f.readlines())
data = json.loads(f)
with open('timetable.yaml', 'w', encoding='utf-8') as yaml_file:
    yaml.dump(data, yaml_file, allow_unicode=True)
