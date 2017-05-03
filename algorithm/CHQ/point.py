class Point(object):
    """docstring for point"""
    
    def __init__(self, x, y):
        super(Point, self).__init__()
        self.x = x
        self.y = y
        self.polar = 0
        
    def set_polar(self, polar):
        self.polar = polar
