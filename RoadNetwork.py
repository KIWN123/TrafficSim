import random

class RoadNetwork:
    def __init__(self, path_list, road_piece_list):
        self.path_list = path_list
        self.road_piece_list = road_piece_list

    def get_next_connecting_road(self, road_piece):
        current_node = road_piece.get_end_node()
        possible_next_roads = []

        for road in self.road_piece_list:
            new_start_node = road.get_start_node()
            if current_node == new_start_node:
                possible_next_roads.append(road)

        if len(possible_next_roads) == 0:
            return None
        else:
            next_road = random.choice(possible_next_roads)
            return next_road
