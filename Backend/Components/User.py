
class User:

    def __init__(self,
        userId: int, email: str = None, username: str = None,
        phoneNumber: str = None, passwordHash: bytes = None,
        passwordSalt: bytes = None, profilePicture: Dict = dict()
    ):
        self.__userId = userId
        self.__email = email
        self.__username = username
        self.__phoneNumber = phoneNumber
        self.__passwordHash = passwordHash
        self.__passwordSalt = passwordSalt
        self.__profilePicture = profilePicture

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

    def setPasswordHash(self, passwordHash: bytes, passwordSalt: bytes) -> User:
        if not (passwordHash or passwordSalt):
            raise ValueError('Requires at least one paramater')
        self.__passwordHash = passwordHash
        self.__passwordSalt = passwordSalt
        return self

    def getProfilePicture(self) -> dict:
        return self.__profilePicture

    def setProfilePicture(self, profilePicture: Dict) -> User:
        self.__profilePicture = profilePicture
        return self
