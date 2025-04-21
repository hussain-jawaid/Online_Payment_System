from datetime import datetime


class PaymentMethod:
    def pay(self, amount):
        pass


class CreditCard(PaymentMethod):
    def __init__(self, card_number, balance):
        self.__card_number = card_number
        self.__balance = balance
        self.__history = []

    def pay(self, amount):
        last_part_card_num = self.__card_number.split("-")[-1]
        if not amount > self.__balance:
            self.__balance -= amount
            print(f"Paid {amount}$ using CreditCard ending with ({last_part_card_num})")

            # keep transactions in history
            now = datetime.now()
            formatted_time = now.strftime("%Y-%m-%d %H:%M")
            self.__history.append(
                {
                    "time": formatted_time,
                    "amount": amount,
                    "status": "Success",
                }
            )

        else:
            print(f"Insufficient funds in CreditCard ending with ({last_part_card_num})")

            # keep transactions in history
            now = datetime.now()
            formatted_time = now.strftime("%Y-%m-%d %H:%M")
            self.__history.append(
                {
                    "time": formatted_time,
                    "amount": amount,
                    "status": "Failed",
                    "reason": "Insufficient funds",
                }
            )

    def show_balance(self):
        print(f"Current balance: {self.__balance}$")

    def get_history(self):
        transaction = 1
        for i in self.__history:
            print(f"\nTransaction No. {transaction}")
            print(i)
            transaction += 1


class PayPal(PaymentMethod):
    def __init__(self, email, balance):
        self.__email = email
        self.__balance = balance
        self.__history = []

    def pay(self, amount):
        if not amount > self.__balance:
            self.__balance -= amount
            print(f"Paid {amount}$ using PayPal account ({self.__email})")

            # keep transactions in history
            now = datetime.now()
            formatted_time = now.strftime("%Y-%m-%d %H:%M")
            self.__history.append(
                {
                    "time": formatted_time,
                    "amount": amount,
                    "status": "Success",
                }
            )

        else:
            print(f"Insufficient funds in PayPal account ({self.__email})")

            # keep transactions in history
            now = datetime.now()
            formatted_time = now.strftime("%Y-%m-%d %H:%M")
            self.__history.append(
                {
                    "time": formatted_time,
                    "amount": amount,
                    "status": "Failed",
                    "reason": "Insufficient funds",
                }
            )

    def show_balance(self):
        print(f"Current balance: {self.__balance}$")

    def get_history(self):
        transaction = 1
        for i in self.__history:
            print(f"\nTransaction No. {transaction}")
            print(i)
            transaction += 1

# example usage
def process_payment(method, amount):
    method.pay(amount)

cc = CreditCard("1234-5678", 1000)
pp = PayPal("user@example.com", 2000)

if __name__ == '__main__':
    # for CreditCard method
    process_payment(cc, 300)
    process_payment(cc, 800) # fails
    cc.show_balance()
    cc.get_history()

    # for PayPal method
    process_payment(pp, 1000)
    process_payment(pp, 1200) # fails
    pp.show_balance()
    pp.get_history()