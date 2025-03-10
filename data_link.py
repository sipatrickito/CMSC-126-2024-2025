class DataLinkLayer:
    def __init__(self, mac_address):
        self.mac_address = mac_address

    def encapsulate(self, data):
        # add mac address and frame structure
        frame = f"{self.mac_address}|{data}"
        print("[Data Link Layer] Encapsulating:", frame)  
        return frame  

    def decapsulate(self, frame):
        # remove mac address and extract original data
        parts = frame.split("|", 1)  
        if len(parts) == 2:
            data = parts[1]  
            print("[Data Link Layer] Decapsulating:", data)  
            return data  
        else:
            print("[Data Link Layer] Error: Invalid frame")  
            return None  
