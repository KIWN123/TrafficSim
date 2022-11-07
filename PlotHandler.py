import matplotlib.pyplot as plt

class PlotHandler:
    def __init__(self, road_piece_list, x_vehicle_point_list, y_vehicle_point_list):
        self.plot = plt

        plt.figure()

        plt.xlim([0, 1280])
        plt.ylim([0, 720])
        plt.gca().invert_yaxis()

        for road_piece in road_piece_list:
            road_piece.generate_and_draw_road(plt)

    def get_plt_ptr(self):
        return self.plot