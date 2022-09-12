import time
from random import randint
import os
import logging
from datetime import datetime, timezone

def log(fn):

    def test(*args, **kwargs):
        start_time = time.time()
        to_execute = fn(*args, **kwargs)
        called_at = datetime.now(timezone.utc)
        USER = os.getenv('USER')
        end = time.time()
        exec_time = end - start_time
        unit = "s"
        if exec_time < 1:
            exec_time *= 1000
            unit = "ms"
        
        string =  f'({USER}) Running: {fn.__name__}\t[ exec-time = {exec_time:.3f} {unit}]\n'

        with open('machine.log', 'a+') as f:
            f.write(string)
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