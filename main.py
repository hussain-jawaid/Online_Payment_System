class PaymentMethod:
    def pay(self, amount):
        pass


class CreditCard(PaymentMethod):
    def __init__(self, card_number, balance):
        self.__card_number = card_number
        self.__balance = balance

    def pay(self, amount):
        last_part_card_num = self.__card_number.split("-")[-1]
        if not amount > self.__balance:
            self.__balance -= amount
            print(f"Paid {amount}$ using CreditCard ending with ({last_part_card_num})")
        else:
            print(f"Insufficient funds in CreditCard ending with ({last_part_card_num})")


class PayPal(PaymentMethod):
    def __init__(self, email, balance):
        self.__email = email
        self.__balance = balance

    def pay(self, amount):
        if not amount > self.__balance:
            self.__balance -= amount
            print(f"Paid {amount}$ using PayPal account ({self.__email})")
        else:
            print(f"Insufficient funds in PayPal account ({self.__email})")

def process_payment(method, amount):
    method.pay(amount)

cc = CreditCard("1234-5678", 5000)
pp = PayPal("user@example.com", 2000)

process_payment(cc, 1500)
process_payment(pp, 2000)