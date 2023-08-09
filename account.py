class Account:
    def __init__(self, name: str) -> None:
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Adds amount of deposit to account balance
        :param amount: amount of deposit
        :return: returns True if successful or False if unsuccessful
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Subtracts amount of withdraw from account balance
        :param amount: amount of withdraw
        :return: returns True if successful or False if unsuccessful
        """
        if amount <= 0:
            return False
        elif amount >= self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Returns account balance
        :return: account balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Retrieves account holders name
        :return: account name
        """
        return self.__account_name

    # Just adding for the withdrawl test for positive withdraws so it's not 0
    def set_balance(self, amount: float) -> None:
        """
        Sets new account balance
        :return: account balance
        """
        self.__account_balance = amount
