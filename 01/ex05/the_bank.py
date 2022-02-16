from time import sleep


class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        for k, v in kwargs.items():
            setattr(self, k, v)
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank:
    def __init__(self):
        self.accounts = []

    def add(self, account):
        self.accounts.append(account)

    def transfer(self, origin, dest, amount):
        for acc in self.accounts:
            if isinstance(origin, str) and acc.name == origin:
                origin_acc = acc
            elif isinstance(origin, int) and acc.id == origin:
                origin_acc = acc
            if isinstance(dest, str) and acc.name == dest:
                dest_acc = acc
            elif isinstance(dest, int) and acc.id == dest:
                dest_acc = acc

        if self.__is_acc_corrupted__(dest_acc):
            return False
        if self.__is_acc_corrupted__(origin_acc):
            return False
        if amount < 0 or origin_acc.value < amount:
            return False

        origin_acc.value -= amount
        dest_acc.transfer(amount)
        return True

    def fix_account(self, account):
        acc = None
        for a in self.accounts:
            if isinstance(account, str) and a.name == account:
                acc = a
            elif isinstance(account, int) and a.id == account:
                acc = a
        if acc is None:
            return False

        i = 0
        while True:
            error = self.__is_acc_corrupted__(acc)
            if not error:
                break
            if error == 3:
                acc.name = None
            if error == 4:
                acc.id = None
            if error == 5:
                acc.value = None
            if error == 6:
                for a in dir(acc):
                    if a.startswith("b"):
                        delattr(acc, a)
            if error == 1:
                acc.zip1111 = None
                acc.addr1111 = None
            if error == 2:
                setattr(acc, f'hi{i}', '')
                i += 1

        return True

    def __is_acc_corrupted__(self, account):
        attr = list(filter(lambda e: not e.startswith("__"), dir(account)))

        if len(attr) % 2 == 0:
            return 2
        if "name" not in attr:
            return 3
        if "id" not in attr:
            return 4
        if "value" not in attr:
            return 5

        startswith_zip_or_addr = 0
        for a in attr:
            if a.startswith("b"):
                return 6
            if a.startswith("zip") or a.startswith("addr"):
                startswith_zip_or_addr = 1

        return not startswith_zip_or_addr
