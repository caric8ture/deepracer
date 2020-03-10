import unittest
from track_boundries_1 import *
from deepracer_test_utilities import *
import matplotlib.pyplot as plt 
 
class TrackBoundries(unittest.TestCase):
    def setUp(self):
        self.params = {}
        self.params['waypoints'] = get_waypoints('way_point_files/simple_track.txt')
        self.params['closest_waypoints'] = [1,3]
        self.params['track_width'] = 1
 
    def test_get_track_angle(self):
        waypoints = self.params['waypoints']
        point0 = [0,1]
        point1 = [0,7]
        boundries = Boundries(self.params)
        track_direction = boundries.get_track_angle(point0, point1)
        self.assertEqual(track_direction, 90)
 
        point0 = [1,0]
        point1 = [7,0]
        boundries = Boundries(self.params)
        track_direction = boundries.get_track_angle(point0, point1)
        self.assertEqual(track_direction, 0)
 
        point0 = [1,1]
        point1 = [7,7]
        boundries = Boundries(self.params)
        track_direction = boundries.get_track_angle(point0, point1)
        self.assertEqual(track_direction, 45)
 
    def test_get_angle_of_track_sections(self):
        angle0 = 0
        angle1 = 90
        boundries = Boundries(self.params)
        track_turn_angle = boundries.get_angle_of_track_sections(angle0,angle1)
        self.assertEqual(track_turn_angle, 90)
 
    def test_left_and_right_boundries(self):
        self.params['waypoints'] = get_horizontal_waypoints()
        point0 = 1
        vertex = 2
        point1 = 3
        boundries = Boundries(self.params)
        left_right = boundries.get_left_and_right_boundries(point0, vertex, point1)
        left = left_right[0]
        right = left_right[1]
        self.assertEqual(left[0], 3)
        self.assertEqual(left[1], 7.5)
        self.assertEqual(right[0], 3)
        self.assertEqual(right[1], 6.5)
 
        self.params['waypoints'] = get_vertical_waypoints()
        point0 = 1
        vertex = 2
        point1 = 3
        boundries = Boundries(self.params)
        left_right = boundries.get_left_and_right_boundries(point0, vertex, point1)
        left = left_right[0]
        right = left_right[1]
        self.assertEqual(round(left[0],5), 6.5)
        self.assertEqual(round(left[1],5), 3)
        self.assertEqual(round(right[0],5), 7.5)
        self.assertEqual(round(right[1],5), 3)

    def test_find_previuos_point(self):
        boundries = Boundries(self.params)
        point = boundries.find_previous_waypoint(10)
        self.assertEqual(point, 9)

        boundries = Boundries(self.params)
        point = boundries.find_previous_waypoint(0)
        self.assertEqual(point, 28)

        boundries = Boundries(self.params)
        point = boundries.find_previous_waypoint(29)
        self.assertEqual(point, 28)

    def test_find_next_point(self):
        boundries = Boundries(self.params)
        point = boundries.find_next_waypoint(10)
        self.assertEqual(point, 11)

        boundries = Boundries(self.params)
        point = boundries.find_next_waypoint(29)
        self.assertEqual(point, 1)

        boundries = Boundries(self.params)
        point = boundries.find_next_waypoint(0)
        self.assertEqual(point, 1)

    def test_look_ahead(self):
        boundries = Boundries(self.params)
        borders = boundries.look_ahead()
        self.assertEqual(len(borders), 1)

    def test_distance(self):
        point0 = [3,7]
        point1 = [7,7]
        boundries = Boundries(self.params)
        distance = boundries.distance(point0, point1)
        self.assertEqual(distance, 4)

    def test_look_ahead(self):
        boundries = Boundries(self.params)
        left_right = boundries.border_waypoints
##        self.plot_points(left_right)
        self.assertEqual(len(left_right), 6)
        
        

    def plot_points(self, boundries):
        waypoints = self.params['waypoints']
        plot_xl=[]
        plot_yl = []
        plot_xr=[]
        plot_yr = []
        plot_xw = []
        plot_yw = []
        
        for points in boundries:
            left = points[0]
            right = points[1]
            plot_xl.append(left[0])
            plot_yl.append(left[1])
            plot_xr.append(right[0])
            plot_yr.append(right[1])

        for i in range(0, 30):
            plot_xw.append(waypoints[i][0])
            plot_yw.append(waypoints[i][1])
        
        plt.scatter(plot_xl, plot_yl)
        plt.scatter(plot_xw, plot_yw)
        plt.scatter(plot_xr, plot_yr)
        plt.show()

    def test_find_point_of_intersection(self):
        boundries = Boundries(self.params)
        x = 5.6
        y = 0
        heading = 36.869
        intersect = boundries.find_point_of_intersection(x,y,heading)
        x_int = intersect[0]
        y_int = intersect[1]
        self.assertEqual(y_int, .75)
        self.assertEqual(round(x_int, 2), 6.6)
        
        self.params['closest_waypoints'] = [3,4]
        boundries = Boundries(self.params)
        x = 6.6
        y = 0
        heading = 12.68
        intersect = boundries.find_point_of_intersection(x,y,heading)
        x_int = intersect[0]
        y_int = intersect[1]
##        left_right = boundries.border_waypoints
##        self.plot_points(left_right)
        self.assertEqual(round(y_int,2), .85)
        self.assertEqual(round(x_int, 2), 10.36)


    def test_find_point_of_intersection_verticle_heading(self):
        self.params['closest_waypoints'] = [22, 24]
        boundries = Boundries(self.params)
        x = .7
        y = 4
        heading = 270
        intersect = boundries.find_point_of_intersection(x,y,heading)
        x_int = intersect[0]
        y_int = intersect[1]
##        left_right = boundries.border_waypoints
##        self.plot_points(left_right)
        self.assertEqual(round(y_int,2), 2)
        self.assertEqual(round(x_int, 2), .7)

    def test_find_point_of_intersection_none_found(self):
        self.params['closest_waypoints'] = [1, 2]
        boundries = Boundries(self.params)
        x = 2.6
        y = .25
        heading = 0
        intersect = boundries.find_point_of_intersection(x,y,heading)
        x_int = intersect[0]
        y_int = intersect[1]
        left_right = boundries.border_waypoints
        self.plot_points(left_right)
        self.assertEqual(round(y_int,2), -8888)
        self.assertEqual(round(x_int, 2), -8888)
 
 
if __name__ == '__main__':
    unittest.main()
 
