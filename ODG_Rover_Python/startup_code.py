import inspect, os, subprocess, sys

def start():
	python_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) # script directory
	root_path = ""
	root_path = python_path[:len(root_path)-17]	
	
	while True:
		try:
			cmd = "python " + python_path + "/__init__.py" 
			print subprocess.call([cmd],
			shell=True, stdin=None, stdout=None, 
			stderr=None)
		except KeyboardInterrupt:
			sys.exit("\nExiting program...")

start()
