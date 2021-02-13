def join_and_capitalize(one, two, delimiter='&'):
    s = f'{one}{delimiter}{two}'
    return s.upper()


def price2int(price):
    _int_price = abs(int(price))
    return f'Price: {_int_price}'


print(join_and_capitalize('johnson', 'johnson'))
print(join_and_capitalize(9000, 'power', '+'))
print(price2int(3.14))
