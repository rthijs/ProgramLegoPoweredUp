class Liebherr9800:

    def __init__(self, bottomHub):
        self._motor_left = bottomHub.motor_A
        self._motor_right = bottomHub.motor_B
        self._motor_left_position = 0
        self._motor_right_position = 0
        self._motor_left_speed = 0.0     # positive values for forward
        self._motor_right_speed = 0.0    # negative values for forward

    @property
    def motor_left_speed(self):
        return self._motor_left_speed

    @property
    def motor_right_speed(self):
        return self._motor_right_speed

    @motor_left_speed.setter
    def motor_left_speed(self, value):
        self._motor_left_speed = self.get_validated_speed_value(value)
        self._motor_left.start_power(self._motor_left_speed)

    @motor_right_speed.setter
    def motor_right_speed(self, value):
        self._motor_right_speed = self.get_validated_speed_value(value)
        self._motor_right.start_power(self._motor_right_speed)

    def get_validated_speed_value(self, value):
        if (value < -1):
            return -1 #motor speed can't be lower than -1.
        elif (value > 1) :
            return 1 #motor speed can't be higher than 1.
        else:
            return value

    def halt(self):
        self._motor_left.stop()
        self._motor_right.stop()
        self._motor_left_speed = 0.0
        self._motor_right_speed = 0.0

    def drive(self, speed=1):
        self.motor_left_speed = speed
        self.motor_right_speed = speed * -1
