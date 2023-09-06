from __future__ import annotations
from flask import make_response

class NonceHashAuthenticationRequest:

    def __init__(self, email: str = '', username: str = '',
        nonceHash: bytes = b'', clientNonce: bytes = b''
    ):
        self.__email = email
        self.__username = username
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

    def getEmail(self) -> str:
        return self.__email

    def getUsername(self) -> str:
        return self.__username

    def getNonceHash(self) -> bytes:
        return self.__nonceHash

    def getClientNonce(self) -> bytes:
        return self.__clientNonce

class NonceHashAuthenticationResponse:
    pass
