class PhysicalLayer:
    def __init__(self):
        pass  # initialize the class

    def transmit(self, data):
        # convert each character to 8-bit binary
        binary_data = ''.join(format(ord(c), '08b') for c in data)
        print("[Physical Layer] Transmitting:", binary_data)  
        return binary_data  

    def receive(self, binary_data):
        # convert binary back to string
        text_data = ''.join(chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8))
        print("[Physical Layer] Received:", text_data)  
        return text_data  