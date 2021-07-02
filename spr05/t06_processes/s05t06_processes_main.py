from processes import task_process, start_processes


if __name__ == '__main__':
	jobs = [
	    {'name': 'John', 'year': 1990, 'delay': 10},
	    {'name': 'Chris', 'year': 1993, 'delay': 5},
	    {'name': 'Matthew', 'year': 2010, 'delay': 3},
	]

	start_processes(jobs)