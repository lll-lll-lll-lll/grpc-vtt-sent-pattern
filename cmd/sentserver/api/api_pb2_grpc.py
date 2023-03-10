# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from api import api_pb2 as api_dot_api__pb2


class VTTSentPatternServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Hello = channel.unary_unary(
                '/sent_vtt.VTTSentPatternService/Hello',
                request_serializer=api_dot_api__pb2.HelloRequest.SerializeToString,
                response_deserializer=api_dot_api__pb2.HelloResponse.FromString,
                )
        self.GetPattern = channel.unary_unary(
                '/sent_vtt.VTTSentPatternService/GetPattern',
                request_serializer=api_dot_api__pb2.GetPatternRequest.SerializeToString,
                response_deserializer=api_dot_api__pb2.GetPatternResponse.FromString,
                )


class VTTSentPatternServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Hello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPattern(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VTTSentPatternServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Hello': grpc.unary_unary_rpc_method_handler(
                    servicer.Hello,
                    request_deserializer=api_dot_api__pb2.HelloRequest.FromString,
                    response_serializer=api_dot_api__pb2.HelloResponse.SerializeToString,
            ),
            'GetPattern': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPattern,
                    request_deserializer=api_dot_api__pb2.GetPatternRequest.FromString,
                    response_serializer=api_dot_api__pb2.GetPatternResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sent_vtt.VTTSentPatternService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VTTSentPatternService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Hello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sent_vtt.VTTSentPatternService/Hello',
            api_dot_api__pb2.HelloRequest.SerializeToString,
            api_dot_api__pb2.HelloResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPattern(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sent_vtt.VTTSentPatternService/GetPattern',
            api_dot_api__pb2.GetPatternRequest.SerializeToString,
            api_dot_api__pb2.GetPatternResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
