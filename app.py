import os
from random import randint
import time

def do():
    days_to_commit = []
    for i in range(1, 365):
        for j in range(0, randint(1, 10)):
            days_to_commit.append(str(i))

    with open('file.txt', 'a') as f:
        f.write(''.join(days_to_commit))

    os.system('git add file.txt')
    os.system('git commit --date="now" -m "https://discord.gg/6dQN3cfrbY"')

def clear_file():
    while True:
        time.sleep(30)
        with open('file.txt', 'w') as f:
            f.truncate(0)

while True:
    do()
    clear_file()
