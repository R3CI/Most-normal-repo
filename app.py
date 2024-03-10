import os
import concurrent.futures
from random import randint
import ctypes

def set_cmd_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def commit_random(commit_count):
    d = str(randint(1, 10))
    os.system(f'git commit --allow-empty -m "{d}"')
    set_cmd_title(f'Current Commits: {commit_count}')

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i in range(10000):
            executor.submit(commit_random, i + 1)

    os.system('git push -u origin main')
