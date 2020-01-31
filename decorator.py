from timeit import default_timer as timer
import time

def timing(method):
  start = timer()
  method()
  end = timer()
  print(end - start)

@timing
def sleeper():
  time.sleep(5)