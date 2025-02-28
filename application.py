class ApplicationLayer:
    def __init__(self):
        pass  

    def send_request(self, message):
        # simulate sending an http-like request
        request = f"REQUEST: {message}"  
        print("[Application Layer] Sending:", request)  
        return request  

    def receive_response(self, request):
        # simulate processing and sending a response
        if request.startswith("REQUEST: "):
            response = "RESPONSE: OK"  
            print("[Application Layer] Responding:", response)  
            return response  
        else:
            print("[Application Layer] Error: Invalid request")  
            return None  
