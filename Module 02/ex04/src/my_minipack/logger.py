from getpass import getuser
import time

def log(fn):
	def inner(*args, **kwargs):
		start = time.time()
		result = fn(*args, **kwargs)
		elapsed = time.time() - start
		if (elapsed < 1):
			elapsed = elapsed * 1000
			format = "ms"
		else:
			format = "s"
		with open('log.log', 'a') as f:
			f.write('({user})Running: {task: <18} [ exec-time = {exectime:.3f} {format} ]\n'.format(
				user = getuser(),
				task = str(fn.__name__).replace("_", " ").title(),
				exectime = elapsed,
				format = format))
		return result

	return inner