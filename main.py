import uuid
import socket
from physical import PhysicalLayer
from data_link import DataLinkLayer
from network import NetworkLayer
from transport import TransportLayer
from session import SessionLayer
from presentation import PresentationLayer
from application import ApplicationLayer

#get macadd and IP automatically

def get_mac_address():
    mac = uuid.getnode()
    mac_str = ':'.join(f"{(mac >> ele) & 0xff:02x}" for ele in range(40, -1, -8))
    return mac_str.upper()

def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Google DNS
        ip = s.getsockname()[0]
        s.close()
    except Exception:
        ip = "127.0.0.1"
    return ip

# setting up and message
print("\n--- OSI Simulation Setup ---")
sender_mac = get_mac_address()
sender_ip = get_ip_address()
print(f"Detected MAC address: {sender_mac}")
print(f"Detected IP address: {sender_ip}")
user_message = input("Enter a message to send: ")

# initialize layers
physical = PhysicalLayer()
data_link = DataLinkLayer(sender_mac)
network = NetworkLayer(sender_ip)
transport = TransportLayer()
session = SessionLayer()
presentation = PresentationLayer()
application = ApplicationLayer()

# simulation of sending data
print("\n--- Sending Data ---\n")
session.start_session()
app_data = application.send_request(user_message)
pres_data = presentation.encapsulate(app_data)
sess_data = session.encapsulate(pres_data)
trans_data = transport.encapsulate(sess_data)
net_data = network.encapsulate(trans_data)
dl_data = data_link.encapsulate(net_data)
phy_data = physical.transmit(dl_data)

# simulation of receiving data
print("\n--- Receiving Data ---\n")
dl_received = physical.receive(phy_data)
net_received = data_link.decapsulate(dl_received)
trans_received = network.decapsulate(net_received)
sess_received = transport.decapsulate(trans_received)
pres_received = session.decapsulate(sess_received)
app_received = presentation.decapsulate(pres_received)
response = application.receive_response(app_received)
session.end_session()

""" PREVIOUS VERSION: Static 
#create instances of all layers  
physical = PhysicalLayer()  
data_link = DataLinkLayer()  
network = NetworkLayer()  
transport = TransportLayer()  
session = SessionLayer()  
presentation = PresentationLayer()  
application = ApplicationLayer()  

# simulate sending data  
print("\n--- Sending Data ---\n")  
session.start_session()  
app_data = application.send_request("Hello, Network!")  
pres_data = presentation.encapsulate(app_data)  
sess_data = session.encapsulate(pres_data)  
trans_data = transport.encapsulate(sess_data)  
net_data = network.encapsulate(trans_data)  
dl_data = data_link.encapsulate(net_data)  
phy_data = physical.transmit(dl_data)  

print("\n--- Receiving Data ---\n")  
dl_received = physical.receive(phy_data)  
net_received = data_link.decapsulate(dl_received)  
trans_received = network.decapsulate(net_received)  
sess_received = transport.decapsulate(trans_received)  
pres_received = session.decapsulate(sess_received)  
app_received = presentation.decapsulate(pres_received)  
response = application.receive_response(app_received)  
session.end_session()  """
