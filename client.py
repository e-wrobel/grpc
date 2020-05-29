from __future__ import print_function
import logging

import grpc

from stubs.service_pb2_grpc import GreeterStub
from stubs.service_pb2 import HelloRequest

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = GreeterStub(channel)
        response = stub.SayHello(HelloRequest(name='you'))
        response2 = stub.SayHelloAgain(HelloRequest(name='second you'))
    print("Greeter client received: " + response.message)
    print("Greeter client received: " + response2.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
