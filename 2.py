from random import sample
from time import sleep


def generate(length):
    password = [str(i) for i in sample(range(0, 10), 6)]
    password = "".join(password)
    return password


counter = 0
time_left = 60

print("New Password :", generate(6))
print("-" * 30)

while True:
    time_left -= 1
    sleep(1)
    print("Time left : ", time_left)

    if time_left == 0:
        print("New Password :", generate(6))
        print("-" * 30)
        time_left = 6
