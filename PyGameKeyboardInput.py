from pylgbst import get_connection_gatt
from pylgbst.hub import MoveHub

import pygame

pygame.init()
display = pygame.display.set_mode((300, 300))

connection = get_connection_gatt(hub_mac='90:84:2B:63:0E:6F')
hub = MoveHub(connection)

motor_left = hub.motor_A
motor_right = hub.motor_B
motor_power = 0.0

def set_motors_power():
    motor_left.start_power(motor_power)
    motor_right.start_power(motor_power * -1)

def stop_motors():
    motor_left.stop()
    motor_right.stop()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("UP")
                motor_power += 0.1
                set_motors_power()
            if event.key == pygame.K_DOWN:
                print("DOWN")
                motor_power -= 0.1
                set_motors_power()
            if event.key == pygame.K_SPACE:
                print("BRAKE")
                motor_power = 0.0
                stop_motors()