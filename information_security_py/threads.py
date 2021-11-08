# This script will do multithreads

# Author: @andvsilva
# date 2021-11-07

# libraries
from threading import Thread
import time

def car(velocity, pilot):
    car_path = 0
    while car_path <= 100:
        car_path += velocity
        time.sleep(0.5)
        print(f'Pilot : {pilot} Km: {car_path}')
        
t_car1 = Thread(target=car, args=[1, 'andvsilva'])
t_car2 = Thread(target=car, args=[2, 'python'])

t_car1.start()
t_car2.start()


        