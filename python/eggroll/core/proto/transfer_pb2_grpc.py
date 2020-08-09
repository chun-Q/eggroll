# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import transfer_pb2 as transfer__pb2


class TransferServiceStub(object):
    """TODO: use transfer lib
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.send = channel.stream_unary(
                '/com.webank.eggroll.core.transfer.TransferService/send',
                request_serializer=transfer__pb2.TransferBatch.SerializeToString,
                response_deserializer=transfer__pb2.TransferBatch.FromString,
                )
        self.recv = channel.unary_stream(
                '/com.webank.eggroll.core.transfer.TransferService/recv',
                request_serializer=transfer__pb2.TransferBatch.SerializeToString,
                response_deserializer=transfer__pb2.TransferBatch.FromString,
                )
        self.sendRecv = channel.stream_stream(
                '/com.webank.eggroll.core.transfer.TransferService/sendRecv',
                request_serializer=transfer__pb2.TransferBatch.SerializeToString,
                response_deserializer=transfer__pb2.TransferBatch.FromString,
                )


class TransferServiceServicer(object):
    """TODO: use transfer lib
    """

    def send(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def recv(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendRecv(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TransferServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'send': grpc.stream_unary_rpc_method_handler(
                    servicer.send,
                    request_deserializer=transfer__pb2.TransferBatch.FromString,
                    response_serializer=transfer__pb2.TransferBatch.SerializeToString,
            ),
            'recv': grpc.unary_stream_rpc_method_handler(
                    servicer.recv,
                    request_deserializer=transfer__pb2.TransferBatch.FromString,
                    response_serializer=transfer__pb2.TransferBatch.SerializeToString,
            ),
            'sendRecv': grpc.stream_stream_rpc_method_handler(
                    servicer.sendRecv,
                    request_deserializer=transfer__pb2.TransferBatch.FromString,
                    response_serializer=transfer__pb2.TransferBatch.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.webank.eggroll.core.transfer.TransferService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TransferService(object):
    """TODO: use transfer lib
    """

    @staticmethod
    def send(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/com.webank.eggroll.core.transfer.TransferService/send',
            transfer__pb2.TransferBatch.SerializeToString,
            transfer__pb2.TransferBatch.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def recv(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/com.webank.eggroll.core.transfer.TransferService/recv',
            transfer__pb2.TransferBatch.SerializeToString,
            transfer__pb2.TransferBatch.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def sendRecv(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/com.webank.eggroll.core.transfer.TransferService/sendRecv',
            transfer__pb2.TransferBatch.SerializeToString,
            transfer__pb2.TransferBatch.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
