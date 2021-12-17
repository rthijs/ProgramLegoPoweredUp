from time import sleep

from pylgbst import *
from pylgbst.hub import MoveHub
from pylgbst import get_connection_gatt

log = logging.getLogger("demo")

def demo_motors(hub):
    motor_left = hub.motor_A
    motor_right = hub.motor_B

    motor_left.start_power(1.0)
    motor_right.start_power(-1.0)
    sleep(1)
    motor_left.start_power(0.5)
    motor_right.start_power(-0.5)
    sleep(2)
    motor_left.stop()
    motor_right.stop()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(relativeCreated)d\t%(levelname)s\t%(name)s\t%(message)s')

    conn = get_connection_gatt (hub_mac='90:84:2B:63:0E:6F')
    hub = MoveHub(conn)

    demo_motors(hub)
    