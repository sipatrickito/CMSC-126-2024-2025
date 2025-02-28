class SessionLayer:
    def __init__(self):
        self.session_active = False  # track session state

    def start_session(self):
        self.session_active = True  
        print("[Session Layer] Session started")  

    def end_session(self):
        self.session_active = False  
        print("[Session Layer] Session ended")  

    def encapsulate(self, data):
        if self.session_active:
            message = f"SESSION_START|{data}|SESSION_END"  
            print("[Session Layer] Encapsulating:", message)  
            return message  
        else:
            print("[Session Layer] Error: No active session")  
            return None  

    def decapsulate(self, message):
        if "SESSION_START|" in message and "|SESSION_END" in message:
            data = message.replace("SESSION_START|", "").replace("|SESSION_END", "")  
            print("[Session Layer] Decapsulating:", data)  
            return data  
        else:
            print("[Session Layer] Error: Invalid session data")  
            return None  
