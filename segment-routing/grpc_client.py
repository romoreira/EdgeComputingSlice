"""
Preserving the rights of the creator. Adapted from:
https://github.com/netgroup/srv6-controller/blob/master/grpc/grpc_client.py
"""


"""
This is a South-Bound Interface (SBI) of the End-To-End Edge Slice Environment Router.
From here, we can perform inter-domain data-plane to Slice (it comes from the edge of a domain and spans to other edge of the other domain).
It was chosen because it performs better than other SBI Methods such as
RestAPI, SSH/CLI, and, NetConf. The paper: "SDN Architecture and Southbound APIs for IPv6
Segment Routing Enabled Wide Area Networks" shows that.
"""


#Useful links:
#https://grpc.io/docs/tutorials/basic/python/
#https://developers.google.com/protocol-buffers/docs/pythontutorial
#Adding via to: https://pypi.org/project/pyroute2/

import grpc
import json

import logging
logging.basicConfig(level=logging.DEBUG)

import srv6_explicit_path_pb2_grpc
import srv6_explicit_path_pb2

# Define wheter to use SSL or not
SECURE = False
# SSL cerificate for server validation
CERTIFICATE = 'cert_client.pem'

class gRPC_Route():

  REMOTE_SERVER_IP = ""
  REMOTE_SERVER_PORT = ""
  data = ""

  def __init__(self, server, port, data):
    self.REMOTE_SERVER_IP = server
    self.REMOTE_SERVER_PORT = port
    self.data = data

  # Build a grpc stub
  def get_grpc_session(self,ip_address, port, secure):
    # If secure we need to establish a channel with the secure endpoint
    if secure:
      # Open the certificate file
      with open(CERTIFICATE) as f:
        certificate = f.read()
      # Then create the SSL credentials and establish the channel
      grpc_client_credentials = grpc.ssl_channel_credentials(certificate)
      channel = grpc.secure_channel("%s:%s" %(ip_address, port), grpc_client_credentials)
    else:
      channel = grpc.insecure_channel("%s:%s" %(ip_address, port))
    return srv6_explicit_path_pb2_grpc.SRv6ExplicitPathStub(channel), channel

  def main(self):

    print("Tentando conectar na porta: "+str(self.REMOTE_SERVER_PORT))
    print("HOST: "+str(self.REMOTE_SERVER_IP))

    # Get the reference of the stub
    srv6_stub,channel = self.get_grpc_session(self.REMOTE_SERVER_IP, self.REMOTE_SERVER_PORT, SECURE)

    # Create message request
    #path_request = srv6_explicit_path_pb2.SRv6EPRequest()
    # Create a new path
    #path = path_request.path.add()
    # Set destination, device, encapmode
    #path.destination = "1111:4::2/128"
    #path.device = "eth1"
    #path.encapmode = "encap"
    # Create a new segment
    #srv6_segment = path.sr_path.add()
    #srv6_segment.segment = "1111:3::2"
    # Single add
    #response = srv6_stub.Create(path_request)
    #print response

    path_request = srv6_explicit_path_pb2.SRv6EPRequest()
    path = path_request.path.add()
    #path.destination = "2222:4::2/128"
    #path.device = "eth1"
    #path.encapmode = "inline"

    #srv6_segment = path.sr_path.add()
    #srv6_segment.segment = "2222:3::2"
    #path = path_request.path.add()
    #path.destination = "3333:4::2/128"
    #path.device = "eth1"
    #path.encapmode = "encap"
    #srv6_segment = path.sr_path.add()
    #srv6_segment.segment = "3333:3::2"
    #srv6_segment = path.sr_path.add()
    #srv6_segment.segment = "3333:2::2"
    #srv6_segment = path.sr_path.add()
    #srv6_segment.segment = "3333:1::2"
    # Bulk add
    #response = srv6_stub.Create(path_request)
    #print response
    # Let's close the session
    #channel.close()

    # Delete all the routes created before
    if self.data == "":
      print("Data Vazia do NANO")

      json_data = json.loads(self.data)
      # Iterate over the array and delete one by one all the paths
      for data in json_data:
        # Each time we create a new session
        srv6_stub, channel = self.get_grpc_session(self.REMOTE_SERVER_IP, self.REMOTE_SERVER_PORT, SECURE)
        # print("Antes")
        path_request = srv6_explicit_path_pb2.SRv6EPRequest()
        # print(str(path_request))
        for jpath in data['paths']:
          path = path_request.path.add()
          path.destination = jpath['destination']
          path.device = jpath['device']
          path.encapmode = jpath['encapmode']
          path.via = jpath['via']
          for segment in jpath['segments']:
            srv6_segment = path.sr_path.add()
            srv6_segment.segment = segment
          # response = srv6_stub.Remove(path_request)
          response = srv6_stub.Create(path_request)
          print(str(response))
          channel.close()
    else:
      json_data = json.loads(self.data)
      # Iterate over the array and delete one by one all the paths
      for data in json_data:
        # Each time we create a new session
        srv6_stub,channel = self.get_grpc_session(self.REMOTE_SERVER_IP, self.REMOTE_SERVER_PORT, SECURE)
        #print("Antes")
        path_request = srv6_explicit_path_pb2.SRv6EPRequest()
        #print(str(path_request))
        for jpath in data['paths']:
          path = path_request.path.add()
          path.destination = jpath['destination']
          path.device = jpath['device']
          path.encapmode = jpath['encapmode']
          path.via = jpath['via']
          print("Passando...")
          for segment in jpath['segments']:
            srv6_segment = path.sr_path.add()
            srv6_segment.segment = segment
          #response = srv6_stub.Remove(path_request)
          response = srv6_stub.Create(path_request)
          print(str(response))
          channel.close()

if __name__ == '__main__':
    logging.debug('Running by IDE - grpc_client')

    route_agent = gRPC_Route("192.168.0.202",12345, "")
    route_agent.data = """
      [
        {
          "paths": [
            {
              "via": "1:2::2",
              "device": "eth2",
              "destination": "b::/64",
              "encapmode": "encap",
              "segments": [
                "2::AD6:F1"
              ]
            }
          ]
        }
      ]
      """
    route_agent.main()
else:
    logging.debug('Imported in somewhereplace - grpc_client')