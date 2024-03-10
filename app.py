import os
from random import randint
import threading
import time

def do():
    while True:
        for i in range(1, 365):
            for j in range(0, randint(1, 10)):
                d = str(i)
                with open('file.txt', 'a') as f:
                    f.write(d)
                os.system('git add .')
                os.system('git commit --date="' + d +'" -m "commit"')
        
        os.system('git push -u origin main')

def clear_file():
    while True:
        time.sleep(30)
        with open('file.txt', 'w') as f:
            f.truncate(0)

threading.Thread(target=clear_file).start()
threading.Thread(target=do).start()
