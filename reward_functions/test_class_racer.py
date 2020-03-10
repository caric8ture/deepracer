import unittest
from class_waypoint import *
from deepracer_test_utilities import *

class TestClassRacer(unittest.TestCase):
    def setUp(self):
        self.params = {}
        self.params['waypoints'] = get_waypoints('way_point_files/simple_track.txt')
        self.params['closest_waypoints'] = [1,3]
        self.params['track_width'] = 1

    def test_
