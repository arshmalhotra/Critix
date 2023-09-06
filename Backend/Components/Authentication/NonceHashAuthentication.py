from __future__ import annotations
from flask import make_response, Response

from Components.Authentication.SignIn import SignInRequest, SignInResponse

class NonceHashAuthenticationRequest(SignInRequest):

    def __init__(self, email: str = '', username: str = '',
        nonceHash: bytes = b'', clientNonce: bytes = b''
    ):
        super().__init__(email, username)
        self.__nonceHash = nonceHash
        self.__clientNonce = clientNonce

    @classmethod
    def fromHttpRequestBody(cls, body: dict) -> NonceHashAuthenticationRequest:
        email = body.get('email')
        if not isinstance(email, str) and email != None:
            raise TypeError(
                "Unsupported type for email: {}".format(type(email))
            )
        username = body.get('username')
        if not isinstance(username, str) and username != None:
            raise TypeError(
                "Unsupported type for username: {}".format(type(username))
            )
        if email == None and username == None:
            raise ValueError("No values found for email or username.")

        nonceHash = body.get('nonce_hash')
        if not isinstance(nonceHash, bytes):
            raise TypeError(
                "Unsupported type for nonce hash: {}".format(type(nonceHash))
            )
        clientNonce = body.get('client_nonce')
        if not isinstance(clientNonce, bytes):
            raise TypeError(
                "Unsupported type for client nonce: {}".format(type(clientNonce))
            )
        return cls(email, username, nonceHash, clientNonce)

    def getNonceHash(self) -> bytes:
        return self.__nonceHash

    def getClientNonce(self) -> bytes:
        return self.__clientNonce

class NonceHashAuthenticationResponse(SignInResponse):

    def __init__(self):
        super().__init__()
        self.__authToken = None

    def getAuthToken(self) -> str:
        return self.__authToken

    def setAuthToken(self, authToken: str) -> NonceHashAuthenticationResponse:
        self.__authToken = authToken
        return self

    def toFlaskResponse(self) -> Response:
        responseBody = {}
        responseBody['message'] = self.__message
        responseBody['authToken'] = self.__authToken

        return make_response(jsonify(responseBody), self.__statuscode)
