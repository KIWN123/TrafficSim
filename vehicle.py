import random

from RoadNetwork import *
from utils.ColorPicker import get_rand_color

class Vehicle:
    def __init__(self, start_road_piece, road_piece_list, road_network):
        self.current_road_piece = start_road_piece
        self.road_piece_list = road_piece_list
        self.road_network = road_network
        self.x_pos, self.y_pos = start_road_piece.get_start_node().get_loc()
        self.end_x, self.end_y = start_road_piece.get_end_node().get_loc()

        rand_vel = random.randint(40, 70)

        self.desired_velocity = rand_vel
        self.velocity = 0
        self.acceleration = 5
        self.journey_finished = False
        self.finish_timestep = None

        #plot vars
        self.color = get_rand_color()
        self.x_points = [self.x_pos]
        self.y_points = [self.y_pos]

    def get_vehicle_pos(self):
        return self.x_pos, self.y_pos

    def advance_vehicle(self, i):
        if self.velocity < self.desired_velocity:
            self.velocity = self.velocity + self.acceleration

        if self.x_pos + self.velocity > self.end_x:
            self.switch_to_new_road_piece(i)
        else:
            self.x_pos = self.x_pos + self.velocity
            self.y_pos = self.current_road_piece.get_center_eq()(self.x_pos)

            self.x_points.append(self.x_pos)
            self.y_points.append(self.y_pos)

    def switch_to_new_road_piece(self, i):
        next_road = self.road_network.get_next_connecting_road(self.current_road_piece)

        if next_road == None:
            self.journey_finished = True
            self.finish_timestep = i
        else:
            self.current_road_piece = next_road
            self.x_pos, self.y_pos = self.current_road_piece.get_start_node().get_loc()
            self.end_x, self.end_y = self.current_road_piece.get_end_node().get_loc()

    def check_journey_state(self):
        return self.journey_finished

    def get_x_points(self):
        return self.x_points

    def get_y_points(self):
        return self.y_points

    def get_color(self):
        return self.color

    def finished_journey_timestep(self, num):
        print(f"Vehicle {num} finished journey at timestep {self.finish_timestep}.")