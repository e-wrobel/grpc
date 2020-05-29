import logging

import grpc
from concurrent import futures
from stubs.service_pb2_grpc import GreeterServicer
from stubs.service_pb2_grpc import add_GreeterServicer_to_server
from stubs.service_pb2 import HelloReply


class Greeter(GreeterServicer):

  def SayHello(self, request, context):
    return HelloReply(message='Hello, %s!' % request.name)

  def SayHelloAgain(self, request, context):
    return HelloReply(message='Hello again, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
