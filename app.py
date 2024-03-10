import os
from random import randint
import threading

def commit_data():
    while True:
        for i in range(1, 365):
            for j in range(0, randint(1, 10)):
                d = str(i) + ' days ago'
                with open('file.txt', 'a') as f:
                    f.write(d)
                os.system('git add .')
                os.system('git commit --date="' + d +'" -m "commit"')
        
        os.system('git push -u origin main')

threads = []
for _ in range(25):
    thread = threading.Thread(target=commit_data)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
