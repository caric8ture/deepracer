import math
from class_waypoint import *

class Section:

    def __init__(self, params, index):
        self.params = params
        self.index = index
        self.back_waypoint = Waypoint(self.params, self.index)
        self.front_waypoint = Waypoint(self.params, self.back_waypoint.index1)
        self.x = params['x']
        self.y = params['y']
        self.heading = params['heading']
        self.track_angle = self.front_waypoint.track_angle_waypoint0_vertex
  #      self.intersects_track =
        self.left_intersection = self.find_point_of_intersection
        
    def find_point_of_intersection(self):
        intersect = [-8888, -8888]
        heading_radians = math.radians(self.heading)
        if self.heading == 90 or self.heading == -90:
            intersect = self.find_vertical_intersect()
        else:
            m1 = math.tan(heading_radians)
            b1 = position_y - m1 * position_x
            near_left = self.back_waypoint.left_waypoint
            near_right = self.back_waypoint.right_waypoint
            far_left = self.front_waypoint.left_waypoint
            far_right = self.front_waypoint.right_waypoint
            left_is_parallel = self.parallel(m1, near_left, far_left)
    
    def find_vertical_intersect(self):
        near_left = self.waypoint0.left_waypoint
        near_right = self.waypoint0.right_waypoint
        far_left = self.waypoint1.left_waypoint
        far_right = self.waypoint1.right_waypoint
        left_found = self.is_between(self.x, near_left[0], far_left[0])

    def parallel(self, m1, point0, point1):
        m2 = self.m_slope(point0, point1)
        if m2 == m1 :
            parallel = True
        else:
            parallel = False
        return parallel

    def m_slope(self, point0, point1):
        x0 = point0[0]
        y0 = point0[1]
        x1 = point1[0]
        y1 = point1[1]
        m = (y1 - y0) / (x1 - x0)
        return m


        

    def is_between(self, x, point0, point1):
        is_between = False
        x0 = point0[0]
        x1 = point1[0]
        if (x0 >= x and x >= x1) or (x1 >= x and x >= x0):
            print(f"{x0} >= {x} >= {x1} or {x1} >= {x} >= {x0}")
            is_between = True
            if self.heading > -90 and self.heading < 90:
                if x < self.x :
                    is_between = False
            elif x > self.x:
                is_between = False
        return is_between 
        
