
class GetSignInChallengeRequest:

    def __init__(self, email: str = '', username: str = ''):
        self.__email = email
        self.__username = username

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
