import random
from bill import Bill
from person import Person


class Friends:
    def __init__(self, friends_list: list):
        self.friends_list = friends_list

    def split_bill(self, bill: Bill):
        result = round(bill.total / len(self.friends_list), 2)

        return dict.fromkeys([friend.name for friend in self.friends_list], result)

    def choose_random_friend(self) -> Person:
        return random.choice(self.friends_list)
