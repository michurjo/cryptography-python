from sys import stdout
import time

def slowprint(text,pause):
  
  for character in text:
    stdout.write(character)
    stdout.flush()
    time.sleep(pause)
