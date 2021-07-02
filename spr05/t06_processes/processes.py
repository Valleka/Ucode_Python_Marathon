from multiprocessing import Process
import datetime, time

def start_processes(jobs):
    for buf in reversed(jobs):
        p = Process(target=task_process, args=(buf['name'], buf['year'], buf['delay']))
        p.start()

def task_process(name, year, delay):
    date_now = datetime.datetime.now().year
    print(f"{name}, {date_now - year} years old")
    time.sleep(delay)

