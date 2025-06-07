# mydevices.py



class Device:
    def __init__(self, name: str, ipaddress: str, hostname: str):

        """
        We initialize a Device object, give it a name, an IP address, and a hostname.
        We set the device status to 'offline' by default.
        """
        
        self.name = name
        self.ipaddress = ipaddress
        self.hostname = hostname
        self.status = "offline"  # Default initial status

    def isOnline(self):
        
        """
        Changing the device's status between 'online' and 'offline'.

        - If the current status is neither 'online' nor 'offline', it 
          is treated as unknown and reset to 'offline' with a message
          printing too screen.
        - If the status is 'offline', we change to 'online' and notify.
        - If the status is 'online', we change to 'offline' and notify.
        """
        
        if self.status not in ["online", "offline"]:
            print("The device status is unknown, setting to offline")
            self.status = "offline"

        if self.status == "offline":
            print("The device is currently offline setting status to online")
            self.status = "online"
        elif self.status == "online":
            print("The device is currently online setting status to offline")
            self.status = "offline"

    def device_properties(self):
        
        """
        We display the current device's name, IP address, and hostname.
        By conting, we can assume the device is online when this is called.
        """
        
        print(
            f"The device {self.name} is currently online with ip address {self.ipaddress} and hostname {self.hostname}"
        )
