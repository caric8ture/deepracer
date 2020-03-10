import math
 
class Boundries:
 
    def __init__(self, params):
        self.waypoints = params['waypoints']
        self.closest_waypoints = params['closest_waypoints']
        self.track_width = params['track_width']
        self.look_ahead_distance = 5 # distance to look ahead this will need to be changed
        self.border_distance = self.track_width/2
        self.border_waypoints = self.look_ahead()
        
 
    def look_ahead(self):
        starting_vertex = self.closest_waypoints[0]
        has_max_look_ahead = False
        vertex = starting_vertex
        waypoint0 = self.find_previous_waypoint(starting_vertex)
        distance = 0
        distance -= self.distance(self.waypoints[vertex], self.waypoints[waypoint0])
        left_right_waypoints = []
        #print("start")
        while not has_max_look_ahead:
            waypoint0 = self.find_previous_waypoint(vertex)
            waypoint1 = self.find_next_waypoint(vertex)
            borders = self.get_left_and_right_boundries(waypoint0, vertex, waypoint1)
            left_right_waypoints.append(borders)
            distance += self.distance(self.waypoints[waypoint0], self.waypoints[vertex])
            left = borders[0]
            right = borders[1]
            vertex_point = self.waypoints[vertex]
            distance_across = self.distance(left,right)
            #print(f"waypoint ({vertex_point[0]},{vertex_point[1]})")
            #print(f"left ({left[0]},{left[1]}) right({right[0]},{right[1]})")
            #print(f"distance across {distance_across}")
            #print(f"{vertex_point[0]},{vertex_point[1]},{left[0]},{left[1]},{right[0]},{right[1]}")
            if distance >= self.look_ahead_distance:
                has_max_look_ahead = True
            else:
                vertex = self.find_next_waypoint(vertex)
        return left_right_waypoints
    
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
    
    def get_track_angle(self, point0, point1):
        radians = math.atan2(point1[1] - point0[1], point1[0] - point0[0])
        angle = math.degrees(radians)
        return angle
 
    def get_angle_of_track_sections(self, angle0, angle1):
        track_turn_angle = angle1 - angle0
        if abs(track_turn_angle) > 180:
            track_turn_angle = 360 - abs(track_turn_angle)
        return track_turn_angle
 
    def get_left_and_right_boundries(self, waypoint0, vertex_position, waypoint1):
        point0 = self.waypoints[waypoint0]
        vertex = self.waypoints[vertex_position]
        point1 = self.waypoints[waypoint1]
        left_point = self.get_boundry(point0, vertex, point1, "left")
        right_point = self.get_boundry(point0, vertex, point1, "right")
        boundries = [left_point, right_point]
        return boundries
 
    def get_boundry(self, point0, vertex, point1, side):
        if side == "right":
            direction = -1
        else:
            direction = 1
        x = 0
        y = 1
        in_center = self.get_incenter(point0, vertex, point1)
        x0 = point0[x]
        y0 = point0[y]
        xv = vertex[x]
        yv = vertex[y]
        x1 = point1[x]
        y1 = point1[y]
        x_in = in_center[x]
        y_in = in_center[y]
        
        if x_in - xv == 0:
            #print(f"x0 = {x0} : x1 = {x1}")
            if x0 < xv :
                y_new = yv + direction * self.border_distance
            else:
                y_new = yv - direction * self.border_distance
            #print(f"x1 = {x1} : y_left = {y}")
            border = [xv, y_new]
        else:
            #print(f"x0 = {x0} : y0 = {y0}")
            #print(f"x1 = {x1} : y1 = {y1}")
            m = (y_in - yv)/(x_in - xv)
            constant = self.border_distance/math.sqrt(1 + math.pow(m,2))
            #print(f"side: {side}, y0: {y0}, yv{yv}")
            #if y1 >= yv :
            if y1 >= yv :
                x_new = xv - direction * constant
            else:
                x_new = xv + direction * constant
            y_new = self.get_y_given_two_points_and_new_x(vertex, [x_in, y_in], x_new)
            border = [x_new, y_new]
        return border
 
    def get_y_given_m_x_b(self, m, x, b):
        y = m * x + b
        return y

    def get_y_given_two_points_and_new_x(self, point0, point1, new_x):
        x = 0
        y =1
        x0 = point0[x]
        y0 = point0[y]
        x1 = point1[x]
        y1 = point1[y]
        m = (y1 - y0)/(x1-x0)
        b = y1 - m*x1
        y_new = m * new_x + b
        return y_new
            


    def get_incenter(self, point0, vertex, point1):
        x = 0
        y = 1
        distance_a = self.distance(point0, vertex)
        distance_b = self.distance(vertex, point1)
        distance_c = self.distance(point1, point0)    
        p = distance_a + distance_b + distance_c
        
        Ax = point0[x]
        Ay = point0[y]
        Bx = vertex[x]
        By = vertex[y]
        Cx = point1[x]
        Cy = point1[y]
        if distance_a + distance_b == distance_c:
            if Cx - Ax == 0:
                Ox = Bx + 1
                Oy = By
                in_center = [Ox,Oy]
            elif Cy-Ay == 0:
                Ox = Bx
                Oy = By +1
                in_center = [Ox, Oy]
            else:
                q = (Cy-Ay)/(Cx-Ax)
                m = -1*1/q
                b = By - m * Bx
                Ox = Bx + 1
                Oy = self.get_y_given_m_x_b(m, Ox, b)            
                in_center = [Ox, Oy]
        else:
            Ox = (distance_a * Cx + distance_b * Ax + distance_c * Bx)/p
            Oy = (distance_a * Cy + distance_b * Ay + distance_c * By)/p
            in_center = [Ox, Oy]
        return in_center

    def distance(self, point0, point1):
        distance = math.sqrt((point1[0] - point0[0])**2 + (point1[1] - point0[1])**2 )
        return distance

    def find_point_of_intersection(self, position_x, position_y, heading):
        intersect = [-8888, -8888]
        heading_radians = math.radians(heading)
        seen_all_points = False
        if heading == 90 or heading == -90:
            intersect = self.find_vertical_intersect(position_x, heading)
            seen_all_points = True
        else:
            m1 = math.tan(heading_radians)
            b1 = position_y - m1 * position_x
            print(f"m1: {m1}, b1: {b1}")
        print(f"({position_x},{position_y}), heading: {heading}")
        border_points = len(self.border_waypoints)  # delete this line
        print(f"number of border points {border_points}")
        if len(self.border_waypoints) <= 1 :
            seen_all_points = True
            intersect = [-9999, -9999]
        index = 0
        while not seen_all_points:
            #print(f"border: {self.border_waypoints}")
            near_border = self.border_waypoints[index]
            print(f"index: {index}, near_border{near_border}")
            near_left = near_border[0]
            near_right = near_border[1]
            far_border = self.border_waypoints[index + 1]
            far_left = far_border[0]
            far_right = far_border[1]
            print(f"near_left: {near_left}, far_left: {far_left}, near_right: {near_right}, far_right: {far_right}")
            left_is_parallel = self.parallel(m1, near_left, far_left)
            print(f"left is parallel {left_is_parallel}")
            if not left_is_parallel:
                x_left_intersection = self.find_x_of_intersection(m1, b1, near_left, far_left)
                #print(f"x_left_intersection: {x_left_intersection}")
                left_found = self.is_between(x_left_intersection, near_left[0], far_left[0], heading, position_x)
                #print(f"left_found: {left_found}")
            else:
                left_found = False
            right_is_parallel = self.parallel(m1, near_right, far_right)
            print(f"right is parallel {right_is_parallel}")
            if not right_is_parallel:
                x_right_intersection = self.find_x_of_intersection(m1, b1, near_right, far_right)
                print(f"x_right_intersection: {x_right_intersection}")
                right_found = self.is_between(x_right_intersection, near_right[0], far_right[0], heading, position_x)
                print(f"right_found: {right_found}")
            else:
                right_found = False

            print(f"left_found: {left_found}, right_found: {right_found}")
            if left_found or right_found or index + 2 == len(self.border_waypoints):
                print(f"Found it! left found {left_found}, right found {right_found}")
                seen_all_points = True
                print(f"should change here {seen_all_points}")
                if left_found:
                    found_x = x_left_intersection
                elif right_found:
                    found_x = x_right_intersection
            else:   
                #seen_all_points = True
                index = index +1
                print(f"should index {index} seen all points {seen_all_points}")
        if (heading != 90 and heading != -90) and (left_found or right_found):
            y_intersect = self.get_y_given_m_x_b(m1, found_x, b1)
            print(f"y_intersect: {y_intersect}")
            intersect = [found_x, y_intersect]
        return intersect
    
    def parallel(self, m1, point0, point1):
        m2 = self.m_slope(point0, point1)
        if m2 == m1 :
            parallel = True
        else:
            parallel = False
        return parallel

    def find_vertical_intersect(self, position_x, heading):
        seen_all_points = False
        if len(self.border_waypoints) <= 1 :
            seen_all_points = True
        index = 0
        while not seen_all_points:
            near_border = self.border_waypoints[index]
            near_left = near_border[0]
            near_right = near_border[1]
            far_border = self.border_waypoints[index + 1]
            far_left = far_border[0]
            far_right = far_border[1]
            left_found = self.is_between(position_x, near_left[0], far_left[0])
            right_found = self.is_between(position_x, near_right[0], far_right[0])
            if left_found or right_found or index + 1 == len(self.border_waypoints):
                seen_all_points = True
                if left_found :
                    end0 = near_left
                    end1 = far_left
                elif right_found:
                    end0 = near_right
                    end1 = far_right
            else:
                index = index + 1
        y_intersect = self.get_y_given_two_points_and_new_x(end0, end1, position_x)
        intersect = [position_x, y_intersect]
        return intersect
                
        
            
    def is_between(self, x, point0, point1, heading, x_position):
        is_between = False
        x0 = float(point0)
        x1 = float(point1)
        x = float(x)
        if (x0 >= x and x >= x1) or (x1 >= x and x >= x0):
            print(f"{x0} >= {x} >= {x1} or {x1} >= {x} >= {x0}")
            is_between = True
            if heading > -90 and heading < 90:
                if x < x_position :
                    is_between = False
            elif x > x_position:
                is_between = False
        return is_between

    def find_x_of_intersection(self,m1, b1, point0, point1):
        m2 = self.m_slope(point0, point1)
        b2 = self.y_intercept_b(point0, point1)
        x = (b2 - b1) / (m1 - m2)
        print(f"find x intersect: {x} ({point0},{point1}) b1: {b1}, b2: {b2}, m1: {m1}, m2: {m2}")
        return x
    
    def y_intercept_b(self, point0, point1):
        m = self.m_slope(point0, point1)
        b = point0[1] - m * point0[0]
        print(f"b: {b}")
        return b

    def m_slope(self, point0, point1):
        x0 = point0[0]
        y0 = point0[1]
        x1 = point1[0]
        y1 = point1[1]
        m = (y1 - y0) / (x1 - x0)
        return m
        
    
            
            

    
            
        
 
