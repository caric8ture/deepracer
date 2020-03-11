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
        waypoint0 = Waypoint(self.params, 1)
        waypoint1 = Waypoint(self.params, 2)
        class_under_test = Section(self.params, waypoint0, waypoint1)
        track_angle = class_under_test.track_angle
        self.assertEqual(track_angle, 0)


if __name__ == '__main__':
    unittest.main()
