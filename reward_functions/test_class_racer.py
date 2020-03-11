import unittest
from class_racer import *
from class_waypoint import *
from deepracer_test_utilities import *

class TestClassRacer(unittest.TestCase):
    def setUp(self):
        self.params = {}
        self.params['waypoints'] = get_waypoints('way_point_files/simple_track.txt')
        self.params['closest_waypoints'] = [0,1]
        self.params['track_width'] = 1
        self.params['heading'] = 0

    def test_look_ahead(self):
        class_under_test = Racer(self.params)
        waypoint_obj = class_under_test.border_waypoints
        self.assertEqual(len(waypoint_obj), 11)
        self.assertEqual(round(waypoint_obj[10].waypoint_distance_from_front_of_car, 3), 8.118)
        
 
if __name__ == '__main__':
    unittest.main()
