from key_logger import keyLogger
from frameRateTracker import FRTracker
from droneSim import simDrone
from droneSim import pSensor
from frame_generator import viewFrame

def setup():
    size(600, 600)
    global k_logger
    global fr_tracker
    global drone_sprite
    global vFrame
    k_logger = keyLogger()
    fr_tracker = FRTracker(10,20)
    drone_sprite = simDrone("droneimg.png",50,50)
    vFrame = viewFrame()
    
def draw():
    background(204, 134, 63)
    vFrame.show()
    fill(0, 12)
    rect(0, 0, width, height)
    fill(255)
    noStroke()
    ellipse(mouseX, mouseY, 60, 60)
    fr_tracker.show()
    drone_sprite.show()
    
def keyPressed():
    user_input = k_logger.logKey(key)
    if (user_input == 0):
        vFrame.shift('moveDroneLeft')
    elif (user_input == 1):
        vFrame.shift('moveDroneRight')
