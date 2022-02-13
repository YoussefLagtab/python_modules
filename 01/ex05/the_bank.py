class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank:
    def __init__(self):
        self.accounts = []

    def add(self, account):
        self.accounts.append(account)

    @staticmethod
    def transfer(self, origin, dest, amount):
        if self.is_acc_corrupted(origin) or self.is_acc_corrupted(origin):
            return False

        for acc in self.accounts:
            if isinstance(origin, str) and origin.name == origin:
                origin_acc = acc
            elif isinstance(origin, int) and acc.id == origin:
                origin_acc = acc
            if isinstance(dest, str) and dest.name == dest:
                dest_acc = acc
            elif isinstance(dest, int) and acc.id == dest:
                dest_acc = acc

        if amount < 0 or origin.amount < amount:
            return False
        origin_acc.value -= amount
        dest_acc.transfer(amount)
        return True

    def is_account_corrupted(self, account):
        attr = filter(lambda e: not e.startswith(), dir(account))

        if len(attr) % 2 == 0:
            return True

        if "name" not in attr or "id" not in attr or "value" not in attr:
            return True

        startswith_zip_or_addr = False
        for a in attr:
            if a.startswith("b"):
                return True
            if a.startswith("zip") or a.startswith("addr"):
                startswith_zip_or_addr = True

        return not startswith_zip_or_addr