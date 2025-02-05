# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import points_pb2 as points__pb2


class PointsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Upsert = channel.unary_unary(
                '/qdrant.Points/Upsert',
                request_serializer=points__pb2.UpsertPoints.SerializeToString,
                response_deserializer=points__pb2.PointsOperationResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/qdrant.Points/Delete',
                request_serializer=points__pb2.DeletePoints.SerializeToString,
                response_deserializer=points__pb2.PointsOperationResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/qdrant.Points/Get',
                request_serializer=points__pb2.GetPoints.SerializeToString,
                response_deserializer=points__pb2.GetResponse.FromString,
                )
        self.SetPayload = channel.unary_unary(
                '/qdrant.Points/SetPayload',
                request_serializer=points__pb2.SetPayloadPoints.SerializeToString,
                response_deserializer=points__pb2.PointsOperationResponse.FromString,
                )
        self.OverwritePayload = channel.unary_unary(
                '/qdrant.Points/OverwritePayload',
                request_serializer=points__pb2.SetPayloadPoints.SerializeToString,
                response_deserializer=points__pb2.PointsOperationResponse.FromString,
                )
        self.DeletePayload = channel.unary_unary(
                '/qdrant.Points/DeletePayload',
                request_serializer=points__pb2.DeletePayloadPoints.SerializeToString,
                response_deserializer=points__pb2.PointsOperationResponse.FromString,
                )
        self.ClearPayload = channel.unary_unary(
                '/qdrant.Points/ClearPayload',
                request_serializer=points__pb2.ClearPayloadPoints.SerializeToString,
                response_deserializer=points__pb2.PointsOperationResponse.FromString,
                )
        self.CreateFieldIndex = channel.unary_unary(
                '/qdrant.Points/CreateFieldIndex',
                request_serializer=points__pb2.CreateFieldIndexCollection.SerializeToString,
                response_deserializer=points__pb2.PointsOperationResponse.FromString,
                )
        self.DeleteFieldIndex = channel.unary_unary(
                '/qdrant.Points/DeleteFieldIndex',
                request_serializer=points__pb2.DeleteFieldIndexCollection.SerializeToString,
                response_deserializer=points__pb2.PointsOperationResponse.FromString,
                )
        self.Search = channel.unary_unary(
                '/qdrant.Points/Search',
                request_serializer=points__pb2.SearchPoints.SerializeToString,
                response_deserializer=points__pb2.SearchResponse.FromString,
                )
        self.SearchBatch = channel.unary_unary(
                '/qdrant.Points/SearchBatch',
                request_serializer=points__pb2.SearchBatchPoints.SerializeToString,
                response_deserializer=points__pb2.SearchBatchResponse.FromString,
                )
        self.Scroll = channel.unary_unary(
                '/qdrant.Points/Scroll',
                request_serializer=points__pb2.ScrollPoints.SerializeToString,
                response_deserializer=points__pb2.ScrollResponse.FromString,
                )
        self.Recommend = channel.unary_unary(
                '/qdrant.Points/Recommend',
                request_serializer=points__pb2.RecommendPoints.SerializeToString,
                response_deserializer=points__pb2.RecommendResponse.FromString,
                )
        self.RecommendBatch = channel.unary_unary(
                '/qdrant.Points/RecommendBatch',
                request_serializer=points__pb2.RecommendBatchPoints.SerializeToString,
                response_deserializer=points__pb2.RecommendBatchResponse.FromString,
                )
        self.Count = channel.unary_unary(
                '/qdrant.Points/Count',
                request_serializer=points__pb2.CountPoints.SerializeToString,
                response_deserializer=points__pb2.CountResponse.FromString,
                )


class PointsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Upsert(self, request, context):
        """
        Perform insert + updates on points. If a point with a given ID already exists - it will be overwritten.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """
        Delete points
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """
        Retrieve points
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetPayload(self, request, context):
        """
        Set payload for points
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OverwritePayload(self, request, context):
        """
        Overwrite payload for points
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeletePayload(self, request, context):
        """
        Delete specified key payload for points
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearPayload(self, request, context):
        """
        Remove all payload for specified points
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateFieldIndex(self, request, context):
        """
        Create index for field in collection
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteFieldIndex(self, request, context):
        """
        Delete field index for collection
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Search(self, request, context):
        """
        Retrieve closest points based on vector similarity and given filtering conditions
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchBatch(self, request, context):
        """
        Retrieve closest points based on vector similarity and given filtering conditions
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Scroll(self, request, context):
        """
        Iterate over all or filtered points points
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Recommend(self, request, context):
        """
        Look for the points which are closer to stored positive examples and at the same time further to negative examples.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RecommendBatch(self, request, context):
        """
        Look for the points which are closer to stored positive examples and at the same time further to negative examples.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Count(self, request, context):
        """
        Count points in collection with given filtering conditions
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PointsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Upsert': grpc.unary_unary_rpc_method_handler(
                    servicer.Upsert,
                    request_deserializer=points__pb2.UpsertPoints.FromString,
                    response_serializer=points__pb2.PointsOperationResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=points__pb2.DeletePoints.FromString,
                    response_serializer=points__pb2.PointsOperationResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=points__pb2.GetPoints.FromString,
                    response_serializer=points__pb2.GetResponse.SerializeToString,
            ),
            'SetPayload': grpc.unary_unary_rpc_method_handler(
                    servicer.SetPayload,
                    request_deserializer=points__pb2.SetPayloadPoints.FromString,
                    response_serializer=points__pb2.PointsOperationResponse.SerializeToString,
            ),
            'OverwritePayload': grpc.unary_unary_rpc_method_handler(
                    servicer.OverwritePayload,
                    request_deserializer=points__pb2.SetPayloadPoints.FromString,
                    response_serializer=points__pb2.PointsOperationResponse.SerializeToString,
            ),
            'DeletePayload': grpc.unary_unary_rpc_method_handler(
                    servicer.DeletePayload,
                    request_deserializer=points__pb2.DeletePayloadPoints.FromString,
                    response_serializer=points__pb2.PointsOperationResponse.SerializeToString,
            ),
            'ClearPayload': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearPayload,
                    request_deserializer=points__pb2.ClearPayloadPoints.FromString,
                    response_serializer=points__pb2.PointsOperationResponse.SerializeToString,
            ),
            'CreateFieldIndex': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFieldIndex,
                    request_deserializer=points__pb2.CreateFieldIndexCollection.FromString,
                    response_serializer=points__pb2.PointsOperationResponse.SerializeToString,
            ),
            'DeleteFieldIndex': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteFieldIndex,
                    request_deserializer=points__pb2.DeleteFieldIndexCollection.FromString,
                    response_serializer=points__pb2.PointsOperationResponse.SerializeToString,
            ),
            'Search': grpc.unary_unary_rpc_method_handler(
                    servicer.Search,
                    request_deserializer=points__pb2.SearchPoints.FromString,
                    response_serializer=points__pb2.SearchResponse.SerializeToString,
            ),
            'SearchBatch': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchBatch,
                    request_deserializer=points__pb2.SearchBatchPoints.FromString,
                    response_serializer=points__pb2.SearchBatchResponse.SerializeToString,
            ),
            'Scroll': grpc.unary_unary_rpc_method_handler(
                    servicer.Scroll,
                    request_deserializer=points__pb2.ScrollPoints.FromString,
                    response_serializer=points__pb2.ScrollResponse.SerializeToString,
            ),
            'Recommend': grpc.unary_unary_rpc_method_handler(
                    servicer.Recommend,
                    request_deserializer=points__pb2.RecommendPoints.FromString,
                    response_serializer=points__pb2.RecommendResponse.SerializeToString,
            ),
            'RecommendBatch': grpc.unary_unary_rpc_method_handler(
                    servicer.RecommendBatch,
                    request_deserializer=points__pb2.RecommendBatchPoints.FromString,
                    response_serializer=points__pb2.RecommendBatchResponse.SerializeToString,
            ),
            'Count': grpc.unary_unary_rpc_method_handler(
                    servicer.Count,
                    request_deserializer=points__pb2.CountPoints.FromString,
                    response_serializer=points__pb2.CountResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'qdrant.Points', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Points(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Upsert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Points/Upsert',
            points__pb2.UpsertPoints.SerializeToString,
            points__pb2.PointsOperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Points/Delete',
            points__pb2.DeletePoints.SerializeToString,
            points__pb2.PointsOperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Points/Get',
            points__pb2.GetPoints.SerializeToString,
            points__pb2.GetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetPayload(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Points/SetPayload',
            points__pb2.SetPayloadPoints.SerializeToString,
            points__pb2.PointsOperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OverwritePayload(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Points/OverwritePayload',
            points__pb2.SetPayloadPoints.SerializeToString,
            points__pb2.PointsOperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeletePayload(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Points/DeletePayload',
            points__pb2.DeletePayloadPoints.SerializeToString,
            points__pb2.PointsOperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClearPayload(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Points/ClearPayload',
            points__pb2.ClearPayloadPoints.SerializeToString,
            points__pb2.PointsOperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateFieldIndex(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Points/CreateFieldIndex',
            points__pb2.CreateFieldIndexCollection.SerializeToString,
            points__pb2.PointsOperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteFieldIndex(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Points/DeleteFieldIndex',
            points__pb2.DeleteFieldIndexCollection.SerializeToString,
            points__pb2.PointsOperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Search(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Points/Search',
            points__pb2.SearchPoints.SerializeToString,
            points__pb2.SearchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchBatch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Points/SearchBatch',
            points__pb2.SearchBatchPoints.SerializeToString,
            points__pb2.SearchBatchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Scroll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Points/Scroll',
            points__pb2.ScrollPoints.SerializeToString,
            points__pb2.ScrollResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Recommend(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Points/Recommend',
            points__pb2.RecommendPoints.SerializeToString,
            points__pb2.RecommendResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RecommendBatch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Points/RecommendBatch',
            points__pb2.RecommendBatchPoints.SerializeToString,
            points__pb2.RecommendBatchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Count(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Points/Count',
            points__pb2.CountPoints.SerializeToString,
            points__pb2.CountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
