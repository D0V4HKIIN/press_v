from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
print("attends 5 secondes")
time.sleep(5)
keyboard.press('v')
#keyboard.release('a')

while(True):
	print("go!!")