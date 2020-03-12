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
        self.intersects_track =
        self.left_intersection = find_point_of_intersection


    def find_point_of_intersection(self):
        intersect = [-8888, -8888]
        heading_radians = math.radians(self.heading)
        if self.heading == 90 or self.heading == -90:
            intersect = self.find_vertical_intersect()
            seen_all_points = True
        else:
        
    
    def find_vertical_intersect(self, near_x, far_x):
        near_left = self.waypoint0.left_waypoint
        near_right = self.waypoint0.right_waypoint
        far_left = self.waypoint1.left_waypoint
        far_right = self.waypoint1.right_waypoint
        left_found = self.is_between(self.x, near_left[0], far_left[0])


        

    def 
