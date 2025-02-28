import base64  

class PresentationLayer:
    def __init__(self):
        pass  

    def encapsulate(self, data):
        # encode data in base64 (simulated encryption)
        encoded_data = base64.b64encode(data.encode()).decode()  
        print("[Presentation Layer] Encapsulating (Encoding):", encoded_data)  
        return encoded_data  

    def decapsulate(self, encoded_data):
        try:
            # decode base64 back to original text
            decoded_data = base64.b64decode(encoded_data.encode()).decode()  
            print("[Presentation Layer] Decapsulating (Decoding):", decoded_data)  
            return decoded_data  
        except Exception as e:
            print("[Presentation Layer] Error:", e)  
            return None  
