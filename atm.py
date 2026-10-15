import calc as ca

USER_DATA = {
    "username": "Sai",
    "Acc no": 123456789,
    "pin": 1234,
    "total bal": 100000,
}


def user_info():
    if USER_DATA and USER_DATA["username"]:
        return f"Hi Welcome User {USER_DATA['username']} Your acc.no is {USER_DATA['Acc no']}"
    else:
        return False


def withdraw(withdrawal_amount):
    if withdrawal_amount <= 0 or withdrawal_amount > USER_DATA["total bal"]:
        return False
    else:
        amount = ca.withdraw_calc(USER_DATA["total bal"], withdrawal_amount)
        USER_DATA["total bal"] = amount
        return amount


def deposit(deposit_amount):
    if deposit_amount > 0:
        amount = ca.deposit_calc(USER_DATA["total bal"], deposit_amount)
        USER_DATA["total bal"] = amount
        return amount
    else:
        return False


def check_balance():
    return USER_DATA["total bal"]


def read_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        return None


def main():
    print("Welcome to TP ATM")
    print("=" * 20)

    pin = read_int("Enter your pin no to proceed: ")

    if pin == USER_DATA["pin"]:
        print(user_info())

        while True:
            choice = read_int("1. Withdraw\n2. Deposit\n3. Check Balance\n4. Exit\nEnter your choice: ")

            match choice:

                case 1:
                    amount = read_int("Enter the amount to withdraw: ")
                    withdraw_resp = withdraw(amount) if amount is not None else False
                    if withdraw_resp is not False:
                        print("Withdrawal Successful")
                    else:
                        print("Withdrawal failed: invalid amount or insufficient balance")

                case 2:
                    amount = read_int("Enter the amount to deposit: ")
                    deposit_resp = deposit(amount) if amount is not None else False
                    if deposit_resp is not False:
                        print("Deposit Successful")
                    else:
                        print("Deposit failed: invalid amount")

                case 3:
                    print(f"Your total balance is: {check_balance()}")

                case 4:
                    print("Thank you for using TP ATM. Goodbye!")
                    break

                case _:
                    print("Invalid choice, please enter 1-4")
    else:
        print("Invalid PIN. Access denied.")


if __name__ == "__main__":
    main()
