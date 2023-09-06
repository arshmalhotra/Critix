from __future__ import annotations
from abc import ABC, abstractmethod

# Abstract classes for Sign In flow.

class SignInRequest(ABC):

    def __init__(self, email: str = '', username: str = ''):
        self.__email = email
        self.__username = username

    @abstractmethod
    def fromHttpRequestBody(cls, body: dict) -> SignInRequest:
        pass

    def getEmail(self) -> str:
        return self.__email

    def setEmail(self, email: str) -> SignInRequest:
        self.__email = email
        return self

    def getUsername(self) -> str:
        return self.__username

    def setUsername(self, username: str) -> SignInRequest:
        self.__username = username
        return self

class SignInResponse(ABC):

    def __init__(self):
        self.__message = 'OK'
        self.__statuscode = 200

    def getStatusCode(self) -> int:
        return self.__statuscode

    def setStatusCode(self, statusCode: int) -> SignInResponse:
        self.__statuscode = statusCode
        return self

    def getMessage(self) -> str:
        return self.__message

    def setMessage(self, message: str) -> SignInResponse:
        self.__message = message
        return self

    @abstractmethod
    def toFlaskResponse(self):
        pass
