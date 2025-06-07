from mydevices import *

net_device = Device("desktop","192.168.1.1","work_desktop")

net_device.isOnline()
net_device.isOnline()
net_device.isOnline()

net_device.status = "bad"
net_device.isOnline()
net_device.isOnline()

net_device.device_properties()
