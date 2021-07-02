import time, threading

def start_threads(jobs):
    for buf in jobs:
        #в target записываем нашу функцию task_thread, а в args указываем потоки
        thread = threading.Thread(target=task_thread, args=(buf['name'], buf['path'], buf['delay']))
        thread.start() #запускаем экземпляр потоков

def task_thread(name, path, delay):
    p = open(path, 'r')
    with p as buf: # все что прилетает в p записываем в buf
        for l in buf:
            print(f"[{name}]: {l[:-1]}") # выводим все, вкоме последнего элемента массива
            time.sleep(delay) # делаем паузу по значению из переменной delay

