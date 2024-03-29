# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import fileService_pb2 as fileService__pb2


class FileServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getFileContent = channel.unary_unary(
                '/FileServer/getFileContent',
                request_serializer=fileService__pb2.FileName.SerializeToString,
                response_deserializer=fileService__pb2.FileContent.FromString,
                )


class FileServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getFileContent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getFileContent': grpc.unary_unary_rpc_method_handler(
                    servicer.getFileContent,
                    request_deserializer=fileService__pb2.FileName.FromString,
                    response_serializer=fileService__pb2.FileContent.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'FileServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FileServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getFileContent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FileServer/getFileContent',
            fileService__pb2.FileName.SerializeToString,
            fileService__pb2.FileContent.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
