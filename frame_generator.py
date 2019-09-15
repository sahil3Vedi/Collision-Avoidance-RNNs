import random

class obstacle():
    
    def __init__(self,n):
        self.index = n
        self.W = width/10
        self.H = height/10
        self.posX = (self.index*width/10)+self.W/2
        self.posY = 0
        
    def show(self,posY):
        self.posY = posY
        #rectMode(CENTER)
        fill(155,0,0)
        #rect(self.posX,self.posY,self.W,self.H)
        ellipseMode(CENTER)
        ellipse(self.posX,self.posY,10,10)
        

class subFrame():
    
    def __init__(self,subVal,subHeight):
        self.jump = 2
        self.obstacleFlag = 0
        self.numObstacles = 2
        self.obstacles = []
        self.subHeight = subHeight
        self.index = subVal
        self.posX = 0
        self.posY = self.index*self.subHeight
        
    def shift(self,instructions):
        if(instructions == "moveDroneLeft"):
            for eachObs in self.obstacles:
                eachObs.posX += self.jump
                if(eachObs.posX>width):
                    eachObs.posX = 10
        if(instructions == "moveDroneRight"):
            for eachObs in self.obstacles:
                eachObs.posX -= self.jump
                if(eachObs.posX<0):
                    eachObs.posX = width-10
        
    def update(self):
        self.posY += 0.8
        
        if (self.posY>height):
            self.obstacleFlag = 1
            self.obstacles = []
            for o in range(self.numObstacles):
                tempO = obstacle(random.randint(1,10))
                self.obstacles.append(tempO)
            self.posY = 0
        
    def show(self):
        fill(self.index*100%255,self.index*100%255,self.index*100%255,122)
        rectMode(CORNER)
        rect(self.posX,self.posY,width, self.subHeight)
        fill(255)
        textMode(CENTER)
        text(str(self.index),width/2,self.posY+10)
        if (self.obstacleFlag == 1):
            for each_obstacle in self.obstacles:
                each_obstacle.show(self.posY-(self.subHeight/2))
                

class viewFrame():
     
    def __init__(self):
        self.bgcolor = [223, 252, 3]
        self.numSubFrames = 10
        self.subFrameHeight = int(height/self.numSubFrames)
        self.subFrames = []
        for i in range(self.numSubFrames):
            temp = subFrame(i,self.subFrameHeight)
            self.subFrames.append(temp)
            
    def shift(self,instruction):
        if(instruction=="moveDroneLeft"):
            for eachSubFrame in self.subFrames:
                eachSubFrame.shift("moveDroneLeft")
        elif(instruction=="moveDroneRight"):
            for eachSubFrame in self.subFrames:
                eachSubFrame.shift("moveDroneRight")
         
    def show(self):
        rectMode(CENTER)
        fill(self.bgcolor[0],self.bgcolor[1],self.bgcolor[2])
        rect(width/2, height/2, width,height)
        for each_subFrame in self.subFrames:
            each_subFrame.update()
            each_subFrame.show()
