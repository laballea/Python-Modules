from getpass import getuser
import time
from random import randint


def log(fn):
    def inner(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        elapsed = time.time() - start
        if (elapsed < 1):
            elapsed = elapsed * 1000
            format = "ms"
        else:
            format = "s"
        with open('machine.log', 'a') as f:
            f.write('({user})Running: {task: <18} [ exec-time = {exectime:.3f} {format} ]\n'.format(
                user=getuser(),
                task=str(fn.__name__).replace("_", " ").title(),
                exectime=elapsed,
                format=format))
        return result

    return inner


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
