import math

class Section:

    def __init__(self, params, index):
        self.params = params
        self.index = index
        self.back_waypoint = Waypoint(self.params, self.index)
        self.front_waypoint = Waypoint(self.params, self.back_waypoint.index1)
        self.x = params['x']
        self.y = params['y']
        self.heading = params['heading']
        self.track_angle = self.get_track_angle()
        
    def get_track_angle(self):
        point0 = self.back_waypoint.center_waypoint
        point1 = self.front_waypoint.center_waypoint
        radians = math.atan2(point1[1] - point0[1], point1[0] - point0[0])
        angle = math.degrees(radians)
        return angle
        
