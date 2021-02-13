# --------------------------------------------------
# Operations with list
# --------------------------------------------------
_list = [3, 5, 7, 9, 10.5]
print('Create and initiate list', _list)

_list.append("P")
print('Append ("P") to list', _list)

print('Get first element of list', _list[0])
print('Get last element of list', _list[-1])
print('Get slice', _list[1:4])

_list.remove("P")
print('Remove element ("P")', _list)

print('-' * 20)

# --------------------------------------------------
# Operations with dict
# --------------------------------------------------
_dict = {"city": "Москва", "temperature": "20"}
print('Create and initiate list', _dict)

print('Get value from dict by key("city")', _dict['city'])

_dict['temperature'] = str(int(_dict['temperature']) - 5)
print('Change dict value (by key "temperature")', _dict)
print('Check "country" key in dict', 'country' in _dict)
print('Get default value if key not present in dict', _dict.get('country', 'Россия'))

_dict['date'] = '27.05.2019'
print('Add new key/value ("date")', _dict)
print('Get dict length', len(_dict))
print('Get dict', _dict)
