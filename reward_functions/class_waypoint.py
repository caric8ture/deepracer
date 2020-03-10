import math

class Waypoint:

    def __init__(self, params, index):
        self.waypoints = params['waypoints']
        self.closest_waypoints = params['closest_waypoints']
        self.track_width = params['track_width']
        self.vertex_index = index
        self.center_waypoint = self.waypoints[self.vertex_index]
        self.look_ahead_distance = 5 # distance to look ahead this will need to be changed
        self.border_distance = self.track_width/2
        self.border_waypoints = self.find_borders()
        self.distance_from_front_of_car() = track_distance_from_car()
        

    def find_borders(self):
        index0 = find_previous_waypoint(self.vertex_index)
        index1 = find_next_waypoint(self.vertex_index)
        borders = self.get_left_and_right_boundries(index0, index1)

        
    def get_left_and_right_boundries(self, index0, index1):
        point0 = self.waypoints(index0)
        point1 = self.waypoints(index1)
        left_point = self.get_boundry(point0, point1, "left")
        right_point = self.get_boundry(point0, point1, "right")
        boundries = [left_point, right_point]
        return boundries

    def track_distance_from_car(self):
        start_index = closest_waypoints[1]
        

    def get_boundry(self, point0, point1, side):
        if side == "right":
            direction = -1
        else:
            direction = 1
        in_center = self.get_incenter(point0, point1)
        x0 = point0[0]
        y0 = point0[1]
        xv = self.center_waypoint[0]
        yv = self.center_waypoint[1]
        x1 = point1[0]
        y1 = point1[1]
        x_in = in_center[0]
        y_in = in_center[1]

        if x_in - xv == 0:  # verticle bisector
            if x0 < xv :          # moving from left to right
                y_new = yv + direction * self.border_distance
            else:                   # moving from right to left
                y_new = yv - direction * self.border_distance
            border = [xv, y_new]
        else:
            m = (y_in - yv)/(x_in - xv)
            constant = self.border_distance/math.sqrt(1 + math.pow(m,2))
            if y1 >= yv :   # direction of travel upish
                x_new = xv - direction * constant
            else:           # direction of travel downward
                x_new = xv + direction * constant
            y_new = self.get_y_given_two_points_and_new_x(vertex, [x_in, y_in], x_new)
            border = [x_new, y_new]
        return border
        
    def get_incenter(self, point0, vertex, point1):
        distance_a = self.distance(point0, vertex)
        distance_b = self.distance(vertex, point1)
        distance_c = self.distance(point1, point0)    
        p = distance_a + distance_b + distance_c
        
        Ax = point0[0]
        Ay = point0[1]
        Bx = vertex[0]
        By = vertex[1]
        Cx = point1[0]
        Cy = point1[1]
        if distance_a + distance_b == distance_c: # for straight lines
            if Cx - Ax == 0:  # if bisector is verticle
                Ox = Bx + 1
                Oy = By
                in_center = [Ox,Oy]
            elif Cy-Ay == 0:  # if bisector is horizontal
                Ox = Bx
                Oy = By +1
                in_center = [Ox, Oy]
            else:                   # everything else
                q = (Cy-Ay)/(Cx-Ax)
                m = -1*1/q
                b = By - m * Bx
                Ox = Bx + 1
                Oy = self.get_y_given_m_x_b(m, Ox, b)            
                in_center = [Ox, Oy]
        else:                                   # curves
            Ox = (distance_a * Cx + distance_b * Ax + distance_c * Bx)/p
            Oy = (distance_a * Cy + distance_b * Ay + distance_c * By)/p
            in_center = [Ox, Oy]
        return in_center

    def get_y_given_two_points_and_new_x(self, point0, point1, new_x):
        x0 = point0[0]
        y0 = point0[1]
        x1 = point1[0]
        y1 = point1[1]
        m = (y1 - y0)/(x1-x0)
        b = y1 - m*x1
        y_new = m * new_x + b
        return y_new


    def find_previous_waypoint(self, index):
        num_of_waypoints = len(self.waypoints)
        if index == 0:
            previous_index = num_of_waypoints - 2 # The first and last points are the same
        else:
             previous_index = index - 1
        return previous_index

    def find_next_waypoint(self, index):
        num_of_waypoints = len(self.waypoints)
        if index == num_of_waypoints - 1:
            next_index = 1
        else:
            next_index = index + 1
        return next_index
