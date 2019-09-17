class pSensor():
    
    
    def __init__(self, x, y):
        self.posX = (width/2)+x
        self.posY = (height/2)+y
        self.obst_dist = "No input detected"
        
    def plot_tracker(self,tracker_line):
        stroke(5)
        line(self.posX,self.posY,tracker_line[0],tracker_line[1])
        fill(255)
        ellipse(tracker_line[0],tracker_line[1],10,10)
        noStroke()
        
    def findObstDist(self,list_of_obstacles):
        min_distance = 10000
        tracker_line = [100,100]
        for each_sFrame in list_of_obstacles:
            for each_obstacle in each_sFrame:
                deltaX = self.posX - each_obstacle.posX
                deltaY = self.posY - each_obstacle.posY
                obs_distance = sqrt(deltaX**2+deltaY**2)
                if obs_distance < min_distance:
                    min_distance = obs_distance
                    tracker_line = [each_obstacle.posX,each_obstacle.posY]
        self.obst_dist = round(min_distance,2)
        self.plot_tracker(tracker_line)
        return self.obst_dist
            
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
        #real time sensor position for distance estimation
        self.nearestObs = []
        
        #abstracting Proximity Sensors
        self.sensors = []
        for xcomp in [-self.hbradius/4,self.hbradius/4]:
            for ycomp in [-self.hbradius/4,self.hbradius/4]:
                proxySensor = pSensor(xcomp,ycomp)
                self.sensors.append(proxySensor)
                
        
        
        
    def show(self,obst_list):
        fill(200,200,200,100)
        ellipse(self.posX, self.posY, self.hbradius,self.hbradius)
        imageMode(CENTER)
        image(self.droneImage, self.posX, self.posY,self.imgWidth,self.imgHeight)
        sensor_counter = 1
        for all_sensors in self.sensors:
            all_sensors.findObstDist(obst_list)
            all_sensors.show(sensor_counter)
            sensor_counter += 1
        return 1
        
