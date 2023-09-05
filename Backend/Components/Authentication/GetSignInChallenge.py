from flask import make_response

class GetSignInChallengeRequest:

    def __init__(self, email: str = '', username: str = ''):
        self.__email = email
        self.__username = username

    @classmethod
    def fromHttpRequestBody(cls, body: Dict) -> GetSignInChallengeRequest:
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

    def getEmail(self) -> str:
        return self.__email

    def setEmail(self, email: str) -> GetSignInChallengeRequest:
        self.__email = email
        return self

    def getUsername(self) -> str:
        return self.__username

    def setUsername(self, username: str) -> GetSignInChallengeRequest:
        self.__username = username
        return self

class GetSignInChallengeResponse:

    def __init__(self, salt: bytes = None, nonce: bytes = None):
        self.__salt = salt
        self.__nonce = nonce
        self.__message = 'OK'
        self.__statuscode = 200

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

    def getStatusCode(self) -> int:
        return self.__statuscode

    def setStatusCode(self, statusCode: int) -> GetSignInChallengeResponse:
        self.__statuscode = statusCode
        return self

    def setMessage(self, message: str) -> GetSignInChallengeResponse:
        self.__message = message
        return self

    def toFlaskResponse(self) -> Response:
        responseBody = {}
        responseBody['message'] = self.__message
        responseBody['email'] = self.__email
        responseBody['username'] = self.__username

        return make_response(responseBody, self.__statuscode)
