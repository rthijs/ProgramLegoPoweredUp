# lower hub in my set has mac address: 90:84:2B:63:0E:6F

from pylgbst.hub import MoveHub
from pylgbst import get_connection_gatt

conn = get_connection_gatt(hub_mac='90:84:2B:63:0E:6F')

hub = MoveHub(conn)

for device in hub.peripherals:
    print(device)