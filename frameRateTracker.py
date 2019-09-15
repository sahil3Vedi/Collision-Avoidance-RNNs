class FRTracker():
    
    def __init__(self, pX, pY):
        self.posX = pX
        self.posY = pY
        
    def show(self):
        fill(15)
        textSize(16)
        text("Frame rate: " + str(int(frameRate)), self.posX, self.posY)
