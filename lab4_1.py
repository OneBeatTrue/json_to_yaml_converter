f = open('timetable.json', 'r', encoding='utf-8')
f = ''.join(f.readlines())

data = eval(f)

yaml_file = open('timetable.yaml', 'w', encoding='utf-8')
yaml_file.write('---' + '\n')

tab_count = 0


def find_item(dictionary):
    global tab_count
    keys = dictionary.keys()
    for key in keys:
        if isinstance(dictionary[key], dict):
            yaml_file.write(tab_count * '  ' + key + ':' + '\n')
            tab_count += 1
            find_item(dictionary[key])
        else:
            yaml_file.write(tab_count * '  ' + key + ':' + ' ' + dictionary[key] + '\n')
    tab_count -= 1
    return


find_item(data)
