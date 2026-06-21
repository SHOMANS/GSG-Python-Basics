class Mobile:
    def __init__(self, brand, model, camera_resolution):
        self.brand = brand
        self.model = model
        self.camera_resolution = camera_resolution

    def turn_on(self):
        print("device is turned on")

    def take_picture(self):
        print(f"you took a picture with {self.camera_resolution} MP Camera")

    def call(self, mobile_number):
        print(f"you are calling {mobile_number} now ...")


mobile1 = Mobile("iphone", "17 pro max", 48)
mobile1.take_picture()
mobile1.call("059999999999")
