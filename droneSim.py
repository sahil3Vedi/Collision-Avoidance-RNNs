class pSensor():
    
    def __init__(self, x, y):
        self.posX = (width/2)+x
        self.posY = (height/2)+y
        self.obst_dist = "No input detected"
        
    def show(self,counterVal):
        #fill(63, 204, 195)
        #ellipse(self.posX,self.posY,20,20)
        fill(15)
        text("Distance from Sensor " + str(counterVal) + " : " + str(self.obst_dist), 10, 15*counterVal+20)
        

class simDrone():
    
    def __init__(self,fileNameString,w,h):
        #abstracting Drone Body
        self.hbradius = sqrt(w**2 + h**2)
        self.syslocation = fileNameString
        self.imgWidth = w
        self.imgHeight = h
        self.posX = width/2
        self.posY = height/2
        self.droneImage = loadImage(fileNameString)
        
        #abstracting Proximity Sensors
        self.sensors = []
        for xcomp in [-self.hbradius/4,self.hbradius/4]:
            for ycomp in [-self.hbradius/4,self.hbradius/4]:
                proxySensor = pSensor(xcomp,ycomp)
                self.sensors.append(proxySensor)
                
        
        
        
    def show(self):
        fill(200)
        ellipse(self.posX, self.posY, self.hbradius,self.hbradius)
        imageMode(CENTER)
        image(self.droneImage, self.posX, self.posY,self.imgWidth,self.imgHeight)
        sensor_counter = 1
        for all_sensors in self.sensors:
            all_sensors.show(sensor_counter)
            sensor_counter += 1
        
