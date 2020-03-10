def get_waypoints(path):
    with open(path, 'r') as file_object:
        waypoints = []
        for line in file_object:
            point = line.split()
            waypoints.append([float(point[0]), float(point[1])])
        return waypoints

def get_horizontal_waypoints():
    waypoints = []
    waypoints.append([1,7])
    waypoints.append([2,7])
    waypoints.append([3,7])
    waypoints.append([4,7])
    waypoints.append([5,7])
    waypoints.append([6,7])
    return waypoints

def get_vertical_waypoints():
    waypoints = []
    waypoints.append([7,1])
    waypoints.append([7,2])
    waypoints.append([7,3])
    waypoints.append([7,4])
    waypoints.append([7,5])
    waypoints.append([7,6])
    return waypoints
