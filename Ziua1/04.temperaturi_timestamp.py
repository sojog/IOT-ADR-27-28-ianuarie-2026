import random
import time



print(time.time())

time.sleep(0.3)

print(time.time())

print(time.strftime("%Y-%m-%d %H:%M:%S"))


MIN_TEMP = 1
MAX_TEMP = 40

temperatura = random.randint(MIN_TEMP, MAX_TEMP)
timestamp = time.strftime("%Y-%m-%d %H:%M:%S")


payload = f'''{{
    "timestamp" : "{timestamp}",
    "temperatura" : {temperatura}
}}'''

print(payload)





# while True:
#     temperatura = random.randint(MIN_TEMP, MAX_TEMP)
#     print(temperatura)
#     time.sleep(1)