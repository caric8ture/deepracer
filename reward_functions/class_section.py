import math

class Section:

    def __init__(self, params, waypoint0, waypoint1):
        self.params = params
        self.back_waypoint = waypoint0
        self.front_waypoint = waypoint1
        self.x = params['x']
        self.y = params['y']
        self.heading = params['heading']
        self.track_angle = self.front_waypoint.track_angle_waypoint0_vertex
        
    
        
