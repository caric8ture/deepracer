from class_waypoint import *
from class_section import *

class Racer:
    
    def __init__(self, params):
        self.params = params
        self.waypoints = params['waypoints']
        self.closest_waypoints = params['closest_waypoints']
        self.track_width = params['track_width']
        self.look_ahead_distance = 8 # distance to look ahead this will need to be changed
        self.border_distance = self.track_width/2
        self.border_waypoints = self.look_ahead()
        self.track_sections = self.find_borders()

    def look_ahead(self):
        starting_vertex = self.closest_waypoints[0]
        vertex = starting_vertex
        all_waypoints = []
        has_maxed_look_ahead = False
        while not has_maxed_look_ahead:
            waypoint_obj = Waypoint(self.params, vertex)
            all_waypoints.append(waypoint_obj)
            if waypoint_obj.waypoint_distance_from_front_of_car >= self.look_ahead_distance:
                has_maxed_look_ahead = True
            vertex = self.find_next_waypoint(vertex)
        return all_waypoints

    def self.find_borders(self):
        for section 
            
        
        

        
    def find_previous_waypoint(self, point):
        num_of_waypoints = len(self.waypoints)
        if point == 0:
            previous_point = num_of_waypoints - 2 # The first and last points are the same
        else:
             previous_point = point - 1
        return previous_point

    def find_next_waypoint(self, point):
        num_of_waypoints = len(self.waypoints)
        if point == num_of_waypoints - 1:
            next_point = 1
        else:
            next_point = point + 1
        return next_point
