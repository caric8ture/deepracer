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
        print(f"x_left {x_left}")
        self.assertEqual(class_under_test.left_waypoint[0], 8)

        self.params['waypoints'] = get_vertical_waypoints()
        self.params['closest_waypoints'] = [0,1]
        class_under_test = Waypoint(self.params, 4)
        x_left = class_under_test.left_waypoint[0]
        print(f"x_left {x_left}")
        self.assertEqual(class_under_test.left_waypoint[0], 6.5)

        
        self.params['waypoints'] = get_vertical_down_waypoints()
        self.params['closest_waypoints'] = [0,1]
        class_under_test = Waypoint(self.params, 4)
        x_left = class_under_test.left_waypoint[0]
        print(f"x_left {x_left}")
        self.assertEqual(class_under_test.left_waypoint[0], 7.5)


        self.params['waypoints'] = get_horizontal_left_waypoints()
        self.params['closest_waypoints'] = [0,1]
        class_under_test = Waypoint(self.params, 4)
        x_left = class_under_test.left_waypoint[0]
        print(f"x_left {x_left}")
        self.assertEqual(class_under_test.left_waypoint[0], 2)


        self.params['waypoints'] = get_down_left_waypoints()
        self.params['closest_waypoints'] = [0,1]
        class_under_test = Waypoint(self.params, 4)
        x_left = class_under_test.left_waypoint[0]
        print(f"x_left {x_left}")
        self.assertEqual(round(x_left, 3), -4.646)

        self.params['waypoints'] = get_up_left_waypoints()
        self.params['closest_waypoints'] = [0,1]
        class_under_test = Waypoint(self.params, 4)
        x_left = class_under_test.left_waypoint[0]
        print(f"x_left {x_left}")
        self.assertEqual(round(x_left), -2)
        
        
    


 
if __name__ == '__main__':
    unittest.main()
