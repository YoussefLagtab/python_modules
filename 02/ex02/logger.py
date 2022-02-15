import time
from random import randint
import os


def log(func):

    def inner1(*args, **kwargs):
        begin = time.time()

        ret = func(*args, **kwargs)

        exec_time = time.time() - begin
        if exec_time < 1:
            exec_time = "%.10f" % (exec_time * 1000) + ' ms'
        else:
            exec_time = "%.10f" % exec_time + ' s '
        user = os.environ["USER"]
        func_name = str.replace(func.__name__, '_', ' ')
        func_name += ' ' * (19 - len(func_name))
        line = f'({user})Running: {func_name}[ exec-time = {exec_time} ]\n'

        log_file = open("machine.log", "a")
        log_file.write(line)
        log_file.close()

        return ret
    return inner1


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1

            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
