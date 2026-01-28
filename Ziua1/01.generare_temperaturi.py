import random
import time

MIN_TEMP = 1
MAX_TEMP = 40

while True:
    temperatura = random.randint(MIN_TEMP, MAX_TEMP)
    print(temperatura)
    time.sleep(1)