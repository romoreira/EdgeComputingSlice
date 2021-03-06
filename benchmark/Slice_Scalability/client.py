from __future__ import print_function

import random
import logging

import grpc

import slice_create_pb2_grpc
import slice_create_pb2

def run(SID_NAME, method):
  channel = grpc.insecure_channel('192.168.0.251:50051')
  stub = slice_create_pb2_grpc.SliceManagerStub(channel)
  if method == "CREATE":
    response = stub.CreateSlice(slice_create_pb2.CreateRequest(SID=SID_NAME))
    print("Creation: " + response.message)
  elif method == "DELETE":
    response = stub.DeleteSlice(slice_create_pb2.DeleteRequest(SID=SID_NAME))
    print("Deletion: " + response.message)
  else:
    print("Unavailable METHOD")



if __name__ == '__main__':
    print("Teste")
    logging.basicConfig()
    run()
