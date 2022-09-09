class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount

    def __str__(self):
            data = [f"{key}: {value}" for key, value in self.__dict__.items()]
            return ', '.join(data)

class Bank(object):
    """The bank"""

    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        """ Add new_account in the Bank
            @new_account: Account() new account to append
            @return True if success, False if an error occured
        """
        if not isinstance(new_account, Account):
            return False
        if new_account in self.accounts:
            return False
        
        self.accounts.append(new_account)
        return True


     
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        # ... Your code ...
        self.accounts.append(new_account)

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
            @origin: str(name) of the first account
            @dest: str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        """
        if not isinstance(origin, str) or not isinstance(dest, str):
            return False
        if not isinstance(amount, (float, int)) or amount < 0:
            return False

        origin_account = next((account for account in self.accounts if account.name == origin), None)
        dest_account = next((account for account in self.accounts if account.name == dest), None)
        if origin_account is None or dest_account is None:
            return False

        if (origin_account.value - amount) < 0:
            return False

        for account in (origin_account, dest_account):
            if not len (account.__dict__) & 1:
                return False
            if (any([key.startswith('b') for key in account.__dict__])):
                return False
            if all([not key.startswith(('zip', 'addr')) for key in account.__dict__]):
                return False
            if not hasattr(account, 'value') or not hasattr(account, 'id'):
                return False
            if not isinstance(account.name, str) or not isinstance(account.id, (int, float)):
                return False

        origin_account.transfer(-amount)
        dest_account.transfer(amount)
        return True

    # ... Your code ...

    def fix_account(self, name):
        """ fix account associated to name if corrupted
            @name: str(name) of the account
            @return True if success, False if an error occured
        """
        if not isinstance(name, str):
            return False
        account = next((account for account in self.accounts if account.name == name), None)
        if account is None:
            return False
        
        for key in [key for key in account.__dict__ if key.startswith('b')]:
                account.__dict__.pop(key)

        if all([not key.startswith(('zip', 'addr')) for key in account.__dict__]):
            account.zip = '123-456'

        if not len (account.__dict__) & 1:
            if ('fix' in account.__dict__.keys()):
                account.__dict__.pop('fix')
            else:
                account.__dict__["fix"] = True
        return True