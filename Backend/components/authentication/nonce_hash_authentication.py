from __future__ import annotations
from flask import make_response, Response, jsonify

from components.authentication.sign_in import SignInRequest, SignInResponse
from components.user import User

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

        nonceHash = body.get('nonceHash')
        if not isinstance(nonceHash, str):
            raise TypeError(
                "Unsupported type for nonce hash: {}".format(type(nonceHash))
            )

        clientNonce = body.get('clientNonce')
        if not isinstance(clientNonce, str):
            raise TypeError(
                "Unsupported type for client nonce: {}".format(type(clientNonce))
            )

        encodedNonceHash = User.cleanJsonBytes(nonceHash)
        encodedClientNonce = User.cleanJsonBytes(clientNonce)

        return cls(email, username, encodedNonceHash, encodedClientNonce)

    def getNonceHash(self) -> bytes:
        return self.__nonceHash

    def getClientNonce(self) -> bytes:
        return self.__clientNonce

class NonceHashAuthenticationResponse(SignInResponse):

    def __init__(self):
        super().__init__()
        self.__authToken = None
        self.__message = 'Internal Server Error'
        self.__statusCode = 500

    def getAuthToken(self) -> str:
        return self.__authToken

    def setAuthToken(self, authToken: str) -> NonceHashAuthenticationResponse:
        self.__authToken = authToken
        return self

    def setMessage(self, message: str) -> NonceHashAuthenticationResponse:
        self.__message = message
        return self

    def setStatusCode(self, statusCode: int) -> NonceHashAuthenticationResponse:
        self.__statusCode = statusCode
        return self

    def toFlaskResponse(self) -> Response:
        responseBody = {}
        responseBody['message'] = self.__message
        responseBody['authToken'] = self.__authToken

        return make_response(jsonify(responseBody), self.__statusCode)
