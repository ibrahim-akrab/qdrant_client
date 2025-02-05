import collections
from typing import Any, Callable, List, Optional, Tuple

import grpc


# type: ignore # noqa: F401
# Source <https://github.com/grpc/grpc/blob/master/examples/python/interceptors/headers/generic_client_interceptor.py>
class _GenericClientInterceptor(
    grpc.UnaryUnaryClientInterceptor,
    grpc.UnaryStreamClientInterceptor,
    grpc.StreamUnaryClientInterceptor,
    grpc.StreamStreamClientInterceptor,
):
    def __init__(self, interceptor_function: Callable):
        self._fn = interceptor_function

    def intercept_unary_unary(
        self, continuation: Any, client_call_details: Any, request: Any
    ) -> Any:
        new_details, new_request_iterator, postprocess = self._fn(
            client_call_details, iter((request,)), False, False
        )
        response = continuation(new_details, next(new_request_iterator))
        return postprocess(response) if postprocess else response

    def intercept_unary_stream(
        self, continuation: Any, client_call_details: Any, request: Any
    ) -> Any:
        new_details, new_request_iterator, postprocess = self._fn(
            client_call_details, iter((request,)), False, True
        )
        response_it = continuation(new_details, next(new_request_iterator))
        return postprocess(response_it) if postprocess else response_it

    def intercept_stream_unary(
        self, continuation: Any, client_call_details: Any, request_iterator: Any
    ) -> Any:
        new_details, new_request_iterator, postprocess = self._fn(
            client_call_details, request_iterator, True, False
        )
        response = continuation(new_details, new_request_iterator)
        return postprocess(response) if postprocess else response

    def intercept_stream_stream(
        self, continuation: Any, client_call_details: Any, request_iterator: Any
    ) -> Any:
        new_details, new_request_iterator, postprocess = self._fn(
            client_call_details, request_iterator, True, True
        )
        response_it = continuation(new_details, new_request_iterator)
        return postprocess(response_it) if postprocess else response_it


def create_generic_client_interceptor(intercept_call: Any) -> _GenericClientInterceptor:
    return _GenericClientInterceptor(intercept_call)


# Source:
# <https://github.com/grpc/grpc/blob/master/examples/python/interceptors/headers/header_manipulator_client_interceptor.py>
class _ClientCallDetails(
    collections.namedtuple("_ClientCallDetails", ("method", "timeout", "metadata", "credentials")),
    grpc.ClientCallDetails,
):
    pass


def header_adder_interceptor(new_metadata: List[Tuple[str, str]]) -> _GenericClientInterceptor:
    def intercept_call(
        client_call_details: _ClientCallDetails,
        request_iterator: Any,
        _request_streaming: Any,
        _response_streaming: Any,
    ) -> Tuple[_ClientCallDetails, Any, Any]:
        metadata = []
        if client_call_details.metadata is not None:
            metadata = list(client_call_details.metadata)
        for header, value in new_metadata:
            metadata.append(
                (
                    header,
                    value,
                )
            )
        client_call_details = _ClientCallDetails(
            client_call_details.method,
            client_call_details.timeout,
            metadata,
            client_call_details.credentials,
        )
        return client_call_details, request_iterator, None

    return create_generic_client_interceptor(intercept_call)


def get_channel(
    host: str, port: int, ssl: bool, metadata: Optional[List[Tuple[str, str]]] = None
) -> grpc.Channel:
    if ssl:
        if metadata:

            def metadata_callback(context: Any, callback: Any) -> None:
                # for more info see grpc docs
                callback(metadata, None)

            # build ssl credentials using the cert the same as before
            cert_creds = grpc.ssl_channel_credentials()

            # now build meta data credentials
            auth_creds = grpc.metadata_call_credentials(metadata_callback)

            # combine the cert credentials and the macaroon auth credentials
            # such that every call is properly encrypted and authenticated
            creds = grpc.composite_channel_credentials(cert_creds, auth_creds)
        else:
            creds = grpc.ssl_channel_credentials()

        # finally pass in the combined credentials when creating a channel
        return grpc.secure_channel(f"{host}:{port}", creds)
    else:
        if metadata:
            metadata_interceptor = header_adder_interceptor(metadata)
            channel = grpc.insecure_channel(f"{host}:{port}", metadata)
            return grpc.intercept_channel(channel, metadata_interceptor)
        else:
            return grpc.insecure_channel(f"{host}:{port}")
