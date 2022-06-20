def ask_friends_number() -> int:
    number = input('Enter the number of friends joining (including you):' + '\n').strip()
    return int(number)


def validate_number(num: int) -> bool:
    return num <= 0


def ask_friend_name(_friends_number: int) -> dict:
    print('\n' + 'Enter the name of every friend (including you), each on a new line:')
    names_dict = {}

    for _ in range(_friends_number):
        names_dict[input()] = 0

    return names_dict


friends_number = ask_friends_number()
valid_number = validate_number(friends_number)
if valid_number:
    print('No one is joining for the party')
else:
    print(ask_friend_name(friends_number))
