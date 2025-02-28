class TransportLayer:
    def __init__(self):
        self.sequence_number = 0  # initialize sequence number

    def encapsulate(self, data):
        # add sequence number to simulate tcp-like transmission
        segment = f"{self.sequence_number}|{data}"  
        print("[Transport Layer] Encapsulating:", segment)  
        self.sequence_number += 1  # increment sequence number
        return segment  

    def decapsulate(self, segment):
        # remove sequence number and extract original data
        parts = segment.split("|", 1)  
        if len(parts) == 2:
            data = parts[1]  
            print("[Transport Layer] Decapsulating:", data)  
            return data  
        else:
            print("[Transport Layer] Error: Invalid segment")  
            return None  
