import unittest
from class_waypoint import *
from deepracer_test_utilities import *

class TestClassRacer(unittest.TestCase):
    def setUp(self):
        self.params = {}
        self.params['waypoints'] = get_waypoints('way_point_files/simple_track.txt')
        self.params['closest_waypoints'] = [1,3]
        self.params['track_width'] = 1
        self.params['heading'] = 0

    def test_borde_waypoints(self):
        class_under_test = Waypoint(self.params, 5)
        x_left = class_under_test.left_waypoint[0]
        self.assertEqual(class_under_test.left_waypoint[0], 8)

        self.params['waypoints'] = get_vertical_waypoints()
        self.params['closest_waypoints'] = [0,1]
        class_under_test = Waypoint(self.params, 4)
        x_left = class_under_test.left_waypoint[0]
        self.assertEqual(class_under_test.left_waypoint[0], 6.5)

        
        self.params['waypoints'] = get_vertical_down_waypoints()
        self.params['closest_waypoints'] = [0,1]
        class_under_test = Waypoint(self.params, 4)
        x_left = class_under_test.left_waypoint[0]
        self.assertEqual(class_under_test.left_waypoint[0], 7.5)


        self.params['waypoints'] = get_horizontal_left_waypoints()
        self.params['closest_waypoints'] = [0,1]
        class_under_test = Waypoint(self.params, 4)
        x_left = class_under_test.left_waypoint[0]
        self.assertEqual(class_under_test.left_waypoint[0], 2)


        self.params['waypoints'] = get_down_left_waypoints()
        self.params['closest_waypoints'] = [0,1]
        class_under_test = Waypoint(self.params, 4)
        x_left = class_under_test.left_waypoint[0]
        self.assertEqual(round(x_left, 3), -4.646)

        self.params['waypoints'] = get_up_left_waypoints()
        self.params['closest_waypoints'] = [0,1]
        class_under_test = Waypoint(self.params, 4)
        x_left = class_under_test.left_waypoint[0]
        self.assertEqual(round(x_left,3), -5.354)
        
        
    def test_index_values(self):
        class_under_test = Waypoint(self.params, 4)
        self.assertEqual(class_under_test.vertex_index, 4)
        self.assertEqual(class_under_test.index0, 3)
        self.assertEqual(class_under_test.index1, 5)

    def test_index_values_finish_start_position(self):
        class_under_test = Waypoint(self.params, 29)
        self.assertEqual(class_under_test.vertex_index, 29)
        self.assertEqual(class_under_test.index0, 28)
        self.assertEqual(class_under_test.index1, 1)

        class_under_test = Waypoint(self.params, 0)
        self.assertEqual(class_under_test.vertex_index, 0)
        self.assertEqual(class_under_test.index0, 28)
        self.assertEqual(class_under_test.index1, 1)

    def test_track_angle_waypoint0_vertex(self):
        class_under_test = Waypoint(self.params, 4)
        self.assertEqual(class_under_test.vertex_turn_angle , 180)
        self.assertEqual(class_under_test.vertex_turn_angle_at_min_distance, 180)

    def test_waypoint_str(self):
        class_under_test = Waypoint(self.params, 1)
        print(class_under_test.__str__())


 
if __name__ == '__main__':
    unittest.main()
