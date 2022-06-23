from person import Person
from friends import Friends
from bill import Bill
from number_error import NumberError


def ask_friends_number() -> int:
    friends_number = int(input('Enter the number of friends joining (including you):' + '\n').strip())

    if friends_number <= 0:
        raise NumberError

    return friends_number


def ask_friends() -> Friends:
    friends_number = ask_friends_number()
    friends_list = []
    print('\n' + 'Enter the name of every friend (including you), each on a new line:')
    for _ in range(friends_number):
        name = input()
        friend = Person(name)
        friends_list.append(friend)

    return Friends(friends_list)


def ask_total_bill() -> Bill:
    total_bill = int(input('\n' + 'Enter the total bill value:' + '\n').strip())

    return Bill(total_bill)


def show_error(error) -> None:
    print(error)


def print_dict(_dict: dict):
    print(_dict)