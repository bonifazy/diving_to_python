class Value:  # data descriptor
    def __set__(self, obj, value):
        self.amount = int(value - obj.commission * value)

    def __get__(self, obj, obj_type):
        return self.amount


class Account:
    amount = Value()
    
    def __init__(self, commission):
        self.commission = commission


if __name__ == "__main__":
    new_account = Account(0.1)
    new_account.amount = 100
    print(new_account.amount)

# 90
