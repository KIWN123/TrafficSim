from vehicle import *

class VehicleGenerator:
    def __init__(self, road_network, road_piece_list, x_vehicle_point_list, y_vehicle_point_list):
        self.road_network = road_network
        self.road_piece_list = road_piece_list
        self.vehicle_list = []

        for i in range(1, 6):
            new_vehicle = Vehicle(self.road_piece_list[0], self.road_piece_list, self.road_network)
            self.vehicle_list.append(new_vehicle)

        self.x_vehicle_point_list = x_vehicle_point_list
        self.y_vehicle_point_list = y_vehicle_point_list

    def simulate(self, i):
        for vehicle in self.vehicle_list:
            if vehicle.check_journey_state() != True:
                x_pos, y_pos = vehicle.get_vehicle_pos()
                vehicle.advance_vehicle(i)

    def draw_vehicle_paths(self, plt):
        for idx, vehicle in enumerate(self.vehicle_list):
            plt.scatter(vehicle.get_x_points(), vehicle.get_y_points(), color=vehicle.get_color())
            vehicle.finished_journey_timestep(idx + 1)