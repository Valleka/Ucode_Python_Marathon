from threads import task_thread, start_threads


if __name__ == '__main__':

    jobs = [
        {'name': 'Thread 1', 'path': 's05t05_threads_file1.txt', 'delay': 3},
        {'name': 'Thread 2', 'path': 's05t05_threads_file2.txt', 'delay': 1},
        {'name': 'Thread 3', 'path': 's05t05_threads_file1.txt', 'delay': 5},
    ]

    start_threads(jobs)
