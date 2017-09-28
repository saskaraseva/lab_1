def emps_with_children_elder_than_(emps, children_age):
    filtered_emps = []
    for emp in emps:
        if emp['children'] != ' ':
            for ch in emp['children']:
                if ch['age'] > children_age:
                    filtered_emps.append(emp['name'])
                    break
    return filtered_emps



ivan = {
    'name': 'ivan',
    'age': 34,
    'children': [{
        'name': 'vasja',
        'age': 12,
    }, {
        'name': 'petia',
        'age': 10,

    }]
}

darja = {
    'name': 'darja',
    'age': 41,
    'children': [{
        'name': 'kirill',
        'age': 21,
    }, {
        'name': 'pavel',
        'age': 15,
    }]
}

all_emps = [ivan, darja]

def main():
    print('emps with children elder 18:')
    print(emps_with_children_elder_than_(all_emps, 18))
main()