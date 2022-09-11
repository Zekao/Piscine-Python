import time
from random import randint
import os
import logging
from datetime import datetime, timezone

def log(fn):

    USER = os.getenv('USER')
    def test(*args, **kwargs):
        called_at = datetime.now(timezone.utc)
        to_execute = fn(*args, **kwargs)
        with open('machine.log', 'a+') as f:
            f.write(f'USER: {USER}\t')
            f.write(f'PID: {os.getpid()}\t')
            f.write(f'DATETIME: {called_at}\t')
            f.write(f'FUNCTION: {fn.__name__}\t')
            f.write(f'INPUTS: {args}\t')

            # start_time = time.time()
            # f.write(f'({USER})Running: {fn.__name__} [ exec_time: {time.time() - start_time} ]\n')
            # f.write( '(' + str(USER) + ')Running: (to_execute, {0})  ''[exec-time ='  + str(time.time() - start_time) + ']\n')
        return to_execute
    
    return test

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