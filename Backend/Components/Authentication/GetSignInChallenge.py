from __future__ import annotations
from flask import make_response, Response

from Components.Authentication.SignIn import SignInRequest, SignInResponse

class GetSignInChallengeRequest:

    def __init__(self, email: str = '', username: str = ''):
        self.__email = email
        self.__username = username

    @classmethod
    def fromHttpRequestBody(cls, body: dict) -> GetSignInChallengeRequest:
        email = body.get('email')
        if not isinstance(email, str) and email != None:
            raise TypeError(
                "Unsupported type found as value: {}".format(type(email))
            )
        username = body.get('username')
        if not isinstance(username, str) and username != None:
            raise TypeError(
                "Unsupported type found as value: {}".format(type(username))
            )
        return cls(email, username)

    def isValid(self) -> bool:
        return self.__email != None or self.__username != None

class GetSignInChallengeResponse(SignInResponse):

    def __init__(self, salt: bytes = None, nonce: bytes = None):
        super().__init__()
        self.__salt = salt
        self.__nonce = nonce

    def isValid(self) -> bool:
        return self.__salt != None and self.__nonce != None

    def getPasswordSalt(self) -> bytes:
        return self.__salt

    def setPasswordSalt(self, salt: bytes) -> GetSignInChallengeResponse:
        self.__salt = salt
        return self

    def getNonce(self) -> bytes:
        return self.__nonce

    def setNonce(self, nonce: bytes) -> GetSignInChallengeResponse:
        self.__nonce = nonce
        return self

    def toFlaskResponse(self) -> Response:
        responseBody = {}
        responseBody['message'] = self.__message
        responseBody['email'] = self.__email
        responseBody['username'] = self.__username

        return make_response(jsonify(responseBody), self.__statuscode)
