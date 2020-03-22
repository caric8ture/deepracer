import math

class Waypoint:

    def __init__(self, params, index):
        self.params = params
        self.min_angle_waypoint_distance = .2
        self.waypoints = params['waypoints']
        self.closest_waypoints = params['closest_waypoints']
        self.track_width = params['track_width']
        self.heading = params['heading']
        self.vertex_index = index
        self.center_waypoint = self.waypoints[self.vertex_index]
        self.index0 = self.find_previous_waypoint(self.vertex_index)
        self.waypoint0 = self.waypoints[self.index0]
        self.track_angle_waypoint0_vertex = self.get_track_angle(self.waypoint0, self.center_waypoint)
        self.index1 = self.find_next_waypoint(self.vertex_index)
        self.waypoint1 = self.waypoints[self.index1]
        self.track_angle_vertex_waypoint1 = self.get_track_angle(self.center_waypoint, self.waypoint1)
        self.look_ahead_distance = 5 # distance to look ahead this will need to be changed
        self.border_distance = self.track_width/2
        self.border_waypoints = self.get_left_and_right_boundries()
        self.left_waypoint = self.border_waypoints[0]
        self.right_waypoint = self.border_waypoints[1]
        self.waypoint_distance_from_front_of_car = self.waypoint_distance_from_car()
        self.vertex_turn_angle = self.get_waypoint_track_angle()
        self.vertex_turn_angle_at_min_distance = self.get_track_angle_at_min_distance() # ensure that the angle is measured at a reasonable distance
    
    def __str__(self):
        obj = ""
        obj += "waypoints: " + str(self.vertex_index)
        return obj



    def get_track_angle_at_min_distance(self):
        calc_distance = 0
        waypoint_index = self.vertex_index
        while calc_distance < self.min_angle_waypoint_distance:
            previous_index = self.find_previous_waypoint(waypoint_index)
            section_distance = self.distance(self.waypoints[previous_index], self.waypoints[waypoint_index])
            calc_distance += section_distance
            if calc_distance >= self.min_angle_waypoint_distance:
                back_index = previous_index
            else:
                waypoint_index = previous_index
        angle0 = self.get_track_angle(self.waypoints[back_index], self.waypoints[self.vertex_index])
        calc_distance = 0.0
        waypoint_index = self.vertex_index
        while calc_distance < self.min_angle_waypoint_distance:
            next_index = self.find_next_waypoint(waypoint_index)
            section_distance = self.distance(self.waypoints[next_index], self.waypoints[waypoint_index])
            calc_distance += section_distance
            if calc_distance >= self.min_angle_waypoint_distance:
                front_index = next_index
            else:
                waypoint_index = next_index
        angle1 = self.get_track_angle(self.waypoints[self.vertex_index], self.waypoints[front_index])
        track_angle = self.get_angle_of_track_sections(angle0, angle1)
        return track_angle

    def get_track_angle(self, point0, point1):
        radians = math.atan2(point1[1] - point0[1], point1[0] - point0[0])
        angle = math.degrees(radians)
        return angle

    def get_waypoint_track_angle(self):
        angle0 = self.track_angle_waypoint0_vertex
        angle1 = self.track_angle_vertex_waypoint1
        angle_between_track_section = self.get_angle_of_track_sections(angle0, angle1)
        
        return angle_between_track_section


    def get_angle_of_track_sections(self, angle0, angle1):
        track_turn_angle = angle1 - angle0
        if abs(track_turn_angle) > 180:
            track_turn_angle = 360 - abs(track_turn_angle)
        if track_turn_angle == 0:
            track_turn_angle = 180
        return track_turn_angle


    def find_borders(self):
        index0 = self.find_previous_waypoint(self.vertex_index)
        index1 = self.find_next_waypoint(self.vertex_index)
        borders = self.get_left_and_right_boundries(index0, index1)
        return borders

        
    def get_left_and_right_boundries(self):
        point0 = self.waypoints[self.index0]
        point1 = self.waypoints[self.index1]
        left_point = self.get_boundry(point0, point1, "left")
        right_point = self.get_boundry(point0, point1, "right")
        boundries = [left_point, right_point]
        return boundries

    def waypoint_distance_from_car(self):
        forward_of_car = self.is_in_front_of_car(self.center_waypoint)
        total_distance = 0
        direction = 1
        distance_found = False
        if not forward_of_car:
            start_index = self.vertex_index # if behind car start at waypoint
            end_index = self.closest_waypoints[1] # ends in front of the car
            direction = -1
        else:
            start_index = self.closest_waypoints[1] # start at the front of the car
            end_index = self.vertex_index # end at the waypoint
        if start_index == end_index:
            distance_found = True
        current_index = start_index
        while not distance_found:
            next_index = self.find_next_waypoint(current_index)
            point0 = self.waypoints[current_index]
            point1 = self.waypoints[next_index]
            distance = self.distance(point0, point1)
            total_distance += distance
            current_index = next_index
            if current_index == end_index:
                distance_found = True
        return total_distance * direction     

    def get_boundry(self, point0, point1, side):
        direction = 1
        if side == "right":
            direction = -1
        print(f"direction: {direction}, side: {side}")
        in_center = self.get_incenter(point0, point1)
        x0 = point0[0]
        y0 = point0[1]
        xv = self.center_waypoint[0]
        yv = self.center_waypoint[1]
        x1 = point1[0]
        y1 = point1[1]
        x_in = in_center[0]
        y_in = in_center[1]
        print(f"x_in: {x_in}, xv: {xv}, x0: {x0}, direction: {direction}")
        if x_in == xv:  # verticle bisector
            if x0 < xv :          # moving from left to right
                print("left to right")
                
                y_new = yv + direction * self.border_distance
                print(f"y_new = yv + direction * border_distance: {y_new} = {yv} + {direction} * {self.border_distance}")
            else:                   # moving from right to left
                print("right to left")
                
                y_new = yv - direction * self.border_distance
                print(f"y_new = yv + direction * border_distance: {y_new} = {yv} - {direction} * {self.border_distance}")
            print(f"vertical y_new : {y_new}, side: {side}")
            border = [xv, y_new]
        else:
            m = (y_in - yv)/(x_in - xv)
            constant = self.border_distance/math.sqrt(1 + math.pow(m,2))
            if y1 >= yv :   # direction of travel upish
                x_new = xv - direction * constant
            else:           # direction of travel downward
                x_new = xv + direction * constant
            y_new = self.get_y_given_two_points_and_new_x(self.center_waypoint, [x_in, y_in], x_new)
            border = [x_new, y_new]
        return border
        
    def get_incenter(self, point0, point1):
        distance_a = self.distance(point0, self.center_waypoint)
        distance_b = self.distance(self.center_waypoint, point1)
        distance_c = self.distance(point1, point0)    
        p = distance_a + distance_b + distance_c
        
        Ax = point0[0]
        Ay = point0[1]
        Bx = self.center_waypoint[0]
        By = self.center_waypoint[1]
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
    def is_in_front_of_car(self, point):
        front_of_car = self.waypoints[self.closest_waypoints[1]]
        in_front_of_car = False
        if self.heading > -90 and self.heading < 90:
            if point[0] > front_of_car[0]:
                in_front_of_car = True
        elif self.heading == 90:
            if point[1] > front_of_car[1]:
                in_front_of_car = True
        elif self.heading == -90:
            if point[1] < front_of_car[1]:
                in_front_of_car = True
        else:
            if point[0] < front_of_car[0]:
                in_front_of_car = True
        return in_front_of_car

    def distance(self, point0, point1):
        distance = math.sqrt((point1[0] - point0[0])**2 + (point1[1] - point0[1])**2 )
        return distance

    def get_y_given_m_x_b(self, m, x, b):
        y = m * x + b
        return y
