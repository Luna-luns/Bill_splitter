import random
from bill import Bill
from person import Person


class Friends:
    def __init__(self, friends_list: list):
        self.friends_list = friends_list

    def split_bill(self, bill: Bill) -> dict:
        result = round(bill.total / len(self.friends_list), 2)

        return dict.fromkeys([friend.name for friend in self.friends_list], result)

    def split_bill_lucky(self, bill: Bill, lucky_friend: Person) -> dict:
        result = round(bill.total / (len(self.friends_list) - 1), 2)
        new_dict = dict.fromkeys([friend.name for friend in self.friends_list], result)
        new_dict[lucky_friend.name] = 0

        return new_dict

    def choose_random_friend(self) -> Person:
        return random.choice(self.friends_list)
