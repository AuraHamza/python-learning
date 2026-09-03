class UAV:
    def __init__(self,uav_id,model,battery_level):
        self.uav_id=uav_id
        self.model=model
        self.__battery_level=battery_level

    def set_battery_level(self,level):
        if 0<=level<=100:
            self.__battery_level=level
        else:
            print("Invalid battery level.")

    def get_battery_level(self):
        return self.__battery_level

    def display_info(self):
        print("\nUAV ID:",self.uav_id)
        print("Model:",self.model)
        print("Battery Level:",self.__battery_level)


uav1 = UAV("U001", "DJI Mavic",80)
uav2 = UAV("U002", "DJI Phantom",60)

uav1.set_battery_level(90)
uav2.set_battery_level(40)

print("UAV 1 Battery:", uav1.get_battery_level())
print("UAV 2 Battery:", uav2.get_battery_level())

uav1.display_info()
uav2.display_info()