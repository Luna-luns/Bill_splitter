import user_interface
from number_error import NumberError


try:
    friends = user_interface.ask_friends()
    bill = user_interface.ask_total_bill()
    lucky = user_interface.confirm_lucky_one()

    if lucky:
        random_friend = friends.choose_random_friend()
        user_interface.print_lucky_one(random_friend)
        new_dict_lucky = friends.split_bill_lucky(bill, random_friend)
        user_interface.print_dict(new_dict_lucky)
    else:
        user_interface.print_nobody_lucky()
        new_dict = friends.split_bill(bill)
        user_interface.print_dict(new_dict)

except NumberError as error:
    user_interface.show_error(error)
