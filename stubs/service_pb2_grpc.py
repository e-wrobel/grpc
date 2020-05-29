# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import stubs.service_pb2 as service__pb2

# Inherited in client
class GreeterStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/Greeter/SayHello',
                request_serializer=service__pb2.HelloRequest.SerializeToString,
                response_deserializer=service__pb2.HelloReply.FromString,
                )
        self.SayHelloAgain = channel.unary_unary(
                '/Greeter/SayHelloAgain',
                request_serializer=service__pb2.HelloRequest.SerializeToString,
                response_deserializer=service__pb2.HelloReply.FromString,
                )

# Inherited in server
class GreeterServicer(object):
    """Missing associated documentation comment in .proto file"""

    def SayHello(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHelloAgain(self, request, context):
        """Sends another greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=service__pb2.HelloRequest.FromString,
                    response_serializer=service__pb2.HelloReply.SerializeToString,
            ),
            'SayHelloAgain': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHelloAgain,
                    request_deserializer=service__pb2.HelloRequest.FromString,
                    response_serializer=service__pb2.HelloReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Greeter/SayHello',
            service__pb2.HelloRequest.SerializeToString,
            service__pb2.HelloReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayHelloAgain(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Greeter/SayHelloAgain',
            service__pb2.HelloRequest.SerializeToString,
            service__pb2.HelloReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
