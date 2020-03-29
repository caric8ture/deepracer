import unittest
from class_section import *
from deepracer_test_utilities import *
from class_waypoint import *

class TestClassSection(unittest.TestCase):

    def setUp(self):
        self.params = {}
        self.params['waypoints'] = get_waypoints('way_point_files/simple_track.txt')
        self.params['closest_waypoints'] = [0,1]
        self.params['track_width'] = 1
        self.params['heading'] = 0
        self.params['x'] = 2
        self.params['y'] = 0

    def test_track_angle(self):
        class_under_test = Section(self.params, 1)
        track_angle = class_under_test.track_angle
        self.assertEqual(track_angle, 0)

    def test_is_between(self):
        self.params['waypoints'] = get_horizontal_waypoints()
        self.params['x'] = 2.5  # between points 1 and 2
        self.params['y'] = 7.2
        self.params['heading'] = 90
        class_under_test = Section(self.params, 1)
        is_btwn = class_under_test.is_between(2.5, class_under_test.back_waypoint.left_waypoint,class_under_test.front_waypoint.left_waypoint )
        self.assertTrue(is_btwn)
        
        
        


if __name__ == '__main__':
    unittest.main()
