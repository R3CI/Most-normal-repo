import os
from random import randint
import ctypes
from concurrent.futures import ThreadPoolExecutor

def set_cmd_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def commit_random(day):
    for _ in range(randint(1, 10)):
        d = str(day) + ' days ago'
        with open('file.txt', 'a') as f:
            f.write(d)
        os.system('git add .')
        os.system('git commit --date="' + d +'" -m "commit"')
        set_cmd_title(f'Current Commits: {cnt}')

if __name__ == "__main__":
    cnt = 0
    with ThreadPoolExecutor() as executor:
        for i in range(1, 365):
            cnt += 1
            executor.submit(commit_random, i)

    os.system('git push -u origin main')
