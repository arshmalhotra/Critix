from __future__ import annotations
import bcrypt
from typing import Tuple, Any
import jwt

class User:

    def __init__(self,
        userId: int = None, email: str = None, username: str = None,
        phoneNumber: str = None, passwordHash: bytes = None,
        passwordSalt: bytes = None, name: str = '', profilePicture: str = ''
    ):
        self.__userId = userId
        self.__email = email
        self.__username = username
        self.__phoneNumber = phoneNumber
        self.__passwordHash = passwordHash
        self.__passwordSalt = passwordSalt
        self.__name = name
        self.__profilePicture = profilePicture
        self.__temporaryNonce = None

    @classmethod
    def fromGetSignInChallengeRequest(
        cls,
        request: GetSignInChallengeRequest
    ) -> User:
        if not request.isValid():
            raise ValueError('No values found for email or username.')

        newUser = User(email=request.getEmail(), username=request.getUsername())
        return newUser

    def getUserId(self) -> int:
        return self.__userId

    def setUserId(self, userId: int) -> User:
        self.__userId = userId
        return self

    def getEmail(self) -> str:
        return self.__email

    def setEmail(self, email: str) -> User:
        self.__email = email
        return self

    def getUsername(self) -> str:
        return self.__username

    def setUsername(self, username: str) -> User:
        self.__username = username
        return self

    def getPhoneNumber(self) -> str:
        return self.__phoneNumber

    def setPhoneNumber(self, phoneNumber: str) -> User:
        self.__phoneNumber = phoneNumber
        return self

    def getPasswordDetails(self) -> dict:
        return {
            'passwordHash': self.__passwordHash,
            'passwordSalt': self.__passwordSalt
        }

    def setPasswordHash(self, passwordHash: bytes = None,
        passwordSalt: bytes = None
    ) -> User:
        if not (passwordHash or passwordSalt):
            raise ValueError('Requires at least one paramater')
        self.__passwordHash = passwordHash or self.__passwordHash
        self.__passwordSalt = passwordSalt or self.__passwordSalt
        return self

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str = '') -> User:
        self.__name = name
        return self

    def getProfilePicture(self) -> str:
        return self.__profilePicture

    def setProfilePicture(self, profilePicture: str) -> User:
        self.__profilePicture = profilePicture
        return self

    def getTemporaryNonce(self) -> bytes:
        return self.__temporaryNonce

    def setTemporaryNonce(self, serverNonce: bytes) -> User:
        self.__temporaryNonce = serverNonce
        return self

    def createNonceHash(self, clientNonce: bytes) -> bytes:
        if self.__passwordHash == None:
            raise ValueError('No password hash found.')
        if self.__temporaryNonce == None:
            raise ValueError('No server nonce found.')
        if clientNonce == None:
            raise ValueError('No client nonce found.')
        combination = self.__temporaryNonce + self.__passwordHash + clientNonce
        serverNonceHash = bcrypt.kdf(
            password=combination,
            salt=b'nonce_hash', # TODO replace with app.config.get('SECRET_KEY')
            desired_key_bytes=64,
            rounds=100
        )
        return serverNonceHash

    def encodeAuthToken(self) -> str:
        if self.__userId == None:
            raise ValueError('No user ID found.')

        payload = {
            'uid': self.__userId,
            'email': self.__email,
            'user': self.__username,
            'phone': self.__phoneNumber,
            'hash': self.__passwordHash,
            'salt': self.__passwordSalt,
            'name': self.__name
        }
        return jwt.encode(
            payload,
            'auth_token_key' # app.config.get('SECRET_KEY'),
        )

    def decodeAuthToken(self, authToken) -> User:
        if self.__userId == None:
            raise ValueError('No user ID found.')

        payload = jwt.decode(
            auth_token,
            'auth_token_key' # app.config.get('SECRET_KEY')
        )
        return User(**payload)

    @classmethod
    def cleanJsonBytes(cls, jsonByteString: str) -> bytes:
        return jsonByteString.encode().decode('unicode_escape').encode('raw_unicode_escape')
