import random

def Hello():
    print('Hello World')

#Hello()

def random_temperature():
    t=random.uniform(25,40)
    t = round(t,2)
    return t

def random_huumidity():
    h=random.uniform(25,40)
    h = round(h,2)
    return h

def check_temperature():
    temp = random_temperature()
    humid = random_huumidity()
    print('Temperature: {}'.format(temp))
    print('Humidity: {}%'.format(humid))

check_temperature()