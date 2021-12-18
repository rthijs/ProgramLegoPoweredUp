from pylgbst import get_connection_gatt
from pylgbst.hub import MoveHub
from liebherr_9800 import Liebherr9800
from time import sleep

bottomHubMacAddress = '90:84:2B:63:0E:6F'
bottomHubConnection = get_connection_gatt(hub_mac=bottomHubMacAddress)
bottomHub = MoveHub(bottomHubConnection)

excavator = Liebherr9800(bottomHub)

excavator.drive()
sleep(1)
excavator.drive(speed=-0.5)
sleep(2)
excavator.halt()
