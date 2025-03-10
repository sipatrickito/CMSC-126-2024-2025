class NetworkLayer:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def encapsulate(self, data):
        # add ip address and packet structure
        packet = f"{self.ip_address}|{data}"  
        print("[Network Layer] Encapsulating:", packet)  
        return packet  

    def decapsulate(self, packet):
        # remove ip address and extract original data
        parts = packet.split("|", 1)  
        if len(parts) == 2:
            data = parts[1]  
            print("[Network Layer] Decapsulating:", data)  
            return data  
        else:
            print("[Network Layer] Error: Invalid packet")  
            return None  
