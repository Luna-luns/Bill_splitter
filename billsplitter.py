import user_interface
from number_error import NumberError


try:
    friends = user_interface.ask_friends()
    bill = user_interface.ask_total_bill()
    split_bill = friends.split_bill(bill)
    user_interface.print_dict(split_bill)

except NumberError as error:
    user_interface.show_error(error)
