class coordinate (object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self,other):
        return((self.x-other.x)**2 + (self.x-other.x)**2)**0.5
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"