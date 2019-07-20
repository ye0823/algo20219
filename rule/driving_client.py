from drive_controller import DrivingController


class DrivingClient(DrivingController):
    def __init__(self):
        # =========================================================== #
        #  Area for member variables =============================== #
        # =========================================================== #
        # Editing area starts from here
        #

        self.is_debug = True
        self.collision_flag = True

        #
        # Editing area ends
        # ==========================================================#
        super().__init__()

    # input값
    # sensing_info.to_middle: 도로의 중앙차선부터 차량까지 직선거리. +이면 오른쪽, -면 왼쪽(float형)
    # sensing_info.collided: 충돌중이면 True임. 정지거나 충돌상태에서 벗어나면 False
    # sensing_info.speed: 현재 차량의 속도(km/h이고 floag형)
    # sensing_info.moving_forwad: 정주행중이면 True, 역주행이면 False
    # sensing_info.moving_angle: 도로랑 평행하게 주행하면 0. 오른쪽 방향으로 가면 +각도, 왼쪽으로 치우쳐지면 -각도
    # sensing_info.track_forward_angles: 전방 10개 구간 도로의 기울기 int배열(10m간격) 
    # sensing_info.lap_progress: 진행상태. 100%면 완주(float형)
    # sensing_info.track_forward_obstacles: 전방 100미터까지 장애물 정보 배열. 장애물과의 거리와 장애물의 to_middle 정보. 
    #                                       장애물은 전부 고정길이 2m이며 to_middle값 기준 좌우 1m. list[dict], dist, to_middle 다 float
    # sensing_info.opponent_cars_info: 전방 100m, 후방 100m 상대편 차량 정보. 가까이 있는 놈부터 들어옴
    #                                  상대차량이름(car_name: string), 중앙선 기준 내 차와의 거리 차이(dist: float). 차량의 to_middle(to_middle: float), 차량의 속도(speed: float)
    # sensing_info.distance_to_way_points: 전방 10개의 way_point와 차량의 직선거리 제공

    # 상수값
    # self.half_road_limit: 도로 절반 폭에 차량 절반 폭을 더한 값. 도로가 10m라면 도로절반5+차량절반1.25 해서 6.25임
    
    # 차량제어
    # car_controls.steering: +면 오른쪽, -면 왼쪽. -1~1까지 가능
    # car_controls.throttle: +면 전진, -면 후진. -1~1까지 가능
    # car_controls.brake: 1이면 감속. 0이면 그대로

    def control_driving(self, car_controls, sensing_info):

        # =========================================================== #
        # Area for writing code about driving rule ================= #
        # =========================================================== #
        # Editing area starts from here
        #

        if self.is_debug:
            print("=========================================================")
            print("to middle: {}".format(sensing_info.to_middle))

            print("collided: {}".format(sensing_info.collided))
            print("car speed: {} km/h".format(sensing_info.speed))

            print("is moving forward: {}".format(sensing_info.moving_forward))
            print("moving angle: {}".format(sensing_info.moving_angle))
            print("lap_progress: {}".format(sensing_info.lap_progress))

            print("track_forward_angles: {}".format(sensing_info.track_forward_angles))
            print("track_forward_obstacles: {}".format(sensing_info.track_forward_obstacles))
            print("opponent_cars_info: {}".format(sensing_info.opponent_cars_info))
            print("distance_to_way_points: {}".format(sensing_info.distance_to_way_points))
            print("=========================================================")

        ###########################################################################

        # Moving straight forward
        car_controls.steering = 0
        car_controls.throttle = 1
        car_controls.brake = 0

        if self.is_debug:
            print("steering:{}, throttle:{}, brake:{}".format(car_controls.steering, car_controls.throttle, car_controls.brake))

        #
        # Editing area ends
        # ==========================================================#
        return car_controls


    # ============================
    # If you have NOT changed the <settings.json> file
    # ===> player_name = ""
    #
    # If you changed the <settings.json> file
    # ===> player_name = "My car name" (specified in the json file)  ex) Car1
    # ============================
    def set_player_name(self):
        player_name = ""
        return player_name


if __name__ == '__main__':
    client = DrivingClient()
    client.run()
