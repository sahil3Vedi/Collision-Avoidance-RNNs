import time

# Class that displays the frame rate
class FRTracker():
    
    def __init__(self, pX, pY):
        self.posX = pX
        self.posY = pY
        self.initial_time = time.time()
        self.current_time = self.initial_time
        
    def show(self):
        self.current_time = time.time()
        timegap = self.current_time - self.initial_time
        fill(15)
        textSize(16)
        text("Frame rate: " + str(int(frameRate)), self.posX, self.posY)
        if (int(timegap) % 1000 == 0):
            print(timegap)
