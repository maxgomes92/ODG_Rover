import inspect, os, subprocess, sys

def start():
	# Finds out its own path
	python_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	
	while True:
		try:
			cmd = "python " + python_path + "/__init__.py" 
			subprocess.call([cmd],
			shell=True, stdin=None, stdout=None, 
			stderr=None)
		except KeyboardInterrupt:
			sys.exit()

start()
