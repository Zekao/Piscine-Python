import time
from random import randint
import os
import logging
from datetime import datetime, timezone

def logger(fn):

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