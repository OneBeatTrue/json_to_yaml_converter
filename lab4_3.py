import re

f = open('timetable.json', 'r', encoding='utf-8')
f = list(map(lambda x: x.strip(), f.readlines()))
data = dict()

begin_pattern = re.compile(r'\S*:')
end_pattern = re.compile(r':.*')

tab_count = 0

stack = ['data']

# видим { - добавляем в стек слово перед {
# видим } - удаляем из стека последний элемент
# при максимальной глубине рекурсии получим максимальную строку с путем
# после этого из строки eval

for line in f:
    if begin_pattern.search(line):
        begin_line = begin_pattern.search(line).group(0)[1:-2]
        end_line = end_pattern.search(line).group(0)[2:]
        if end_line[-1] == ',':
            eval(stack[-1])[begin_line] = end_line[1:-2]
        elif end_line[-1] == '"':
            eval(stack[-1])[begin_line] = end_line[1:-1]
        else:
            eval(stack[-1])[begin_line] = dict()
            stack.append(stack[-1] + f"['{begin_line}']")  # углубление рекурсии
    else:
        if '}' in line:
            stack.pop()  # откат рекурсии


def find_item(dictionary):
    global tab_count
    keys = dictionary.keys()
    for key_ in keys:
        if isinstance(dictionary[key_], dict):
            yaml_file.write(tab_count * '  ' + key_ + ':' + '\n')
            tab_count += 1
            find_item(dictionary[key_])
        else:
            yaml_file.write(tab_count * '  ' + key_ + ':' + ' ' + dictionary[key_] + '\n')
    tab_count -= 1
    return


yaml_file = open('timetable.yaml', 'w', encoding='utf-8')
yaml_file.write('---' + '\n')
find_item(data)
