from physical import PhysicalLayer  
from data_link import DataLinkLayer  
from network import NetworkLayer  
from transport import TransportLayer  
from session import SessionLayer  
from presentation import PresentationLayer  
from application import ApplicationLayer  

#dynamic input from user
print("\n--- OSI Simulation Setup ---")
sender_mac = input("Enter sender MAC address (e.g., AA:BB:CC:DD:EE:FF): ")
sender_ip = input("Enter sender IP address (e.g., 192.168.1.1): ")
user_message = input("Enter a message to send: ")

#initialize layers 
physical = PhysicalLayer()
data_link = DataLinkLayer(mac_address=sender_mac)
network = NetworkLayer(ip_address=sender_ip)
transport = TransportLayer()
session = SessionLayer()
presentation = PresentationLayer()
application = ApplicationLayer()

#simulate sending data
print("\n--- Sending Data ---\n")
session.start_session()
app_data = application.send_request(user_message)
pres_data = presentation.encapsulate(app_data)
sess_data = session.encapsulate(pres_data)
trans_data = transport.encapsulate(sess_data)
net_data = network.encapsulate(trans_data)
dl_data = data_link.encapsulate(net_data)
phy_data = physical.transmit(dl_data)

#simulate receiving data
print("\n--- Receiving Data ---\n")
dl_received = physical.receive(phy_data)
net_received = data_link.decapsulate(dl_received)
trans_received = network.decapsulate(net_received)
sess_received = transport.decapsulate(trans_received)
pres_received = session.decapsulate(sess_received)
app_received = presentation.decapsulate(pres_received)
response = application.receive_response(app_received)
session.end_session()

""" Static ver
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
