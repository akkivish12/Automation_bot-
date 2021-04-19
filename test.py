#import neccesary libraries
import pyautogui 
from PIL import Image, ImageGrab,ImageOps 
import time
import ClointFusion as cf
import numpy as np

#launching dino game
def launch_game():
    cf.launch_any_exe_bat_application("chrome")
    cf.key_write_enter("chrome://dino")
    cf.key_hit_enter()
    cf.key_press("space") 
    return

launch_game()
class cordinates():
	# coordinates of replay button to start the game 
	replaybutton =(380, 222)
	# this coordinates represent the top-right coordinates
	# that will be used to define the front box
	dinasaur = (140, 240 )
	
def restartGame():

	# using pyautogui library, we are clicking on the
	# replay button without any user interaction
	pyautogui.click(cordinates.replaybutton)

	# we will keep our Bot always down that
	# will prevent him to get hit by bird
	pyautogui.keyDown('down')

def press_space():

	# releasing the Down Key
	pyautogui.keyUp('down')

	# pressing Space to overcome Bush
	pyautogui.keyDown('space')

	# so that Space Key will be recognized easily
	time.sleep(0.05)

	# printing the "Jump" statement on the
	# terminal to see the current output
	print("jump")
	time.sleep(0.10)

	# releasing the Space Key
	pyautogui.keyUp('space')

	# again pressing the Down Key to keep my Bot always down
	pyautogui.keyDown('down')

def imageGrab():
	# defining the coordinates of box in front of dinosaur
	box = (cordinates.dinasaur[0]+35, cordinates.dinasaur[1],
		cordinates.dinasaur[0]+350, cordinates.dinasaur[1]+5)

	# grabbing all the pixels values in form of RGB tupples
	image = ImageGrab.grab(box)

	# converting RGB to Grayscale to
	# make processing easy and result faster
	grayImage = ImageOps.grayscale(image)

	# using numpy to get sum of all grayscale pixels
	a = np.array(grayImage.getcolors())

	# returning the sum
	print(a.sum())
	return a.sum()
	
	
 
# function to restart the game
restartGame()
while True:
	# 435 is the sum of white pixels values of box.
 	# You may get different value is you are taking bigger
 	# or smaller box than the box taken in this article.
 	# if value returned by "imageGrab" function is not equal to 435,
 	# it means either bird or bush is coming towards dinosaur
 	if(imageGrab()!= 435):
 		press_space()
 		# time to recognize the operation performed by above function
 		time.sleep(0.1)
              