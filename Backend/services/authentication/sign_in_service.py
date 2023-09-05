import os
import base64

from Components.Authentication.GetSignInChallenge import GetSignInChallengeRequest, GetSignInChallengeResponse
from database.connector import getUserSpecificSalt

class SignInService:

    @classmethod
    def executeGetSignInChallengeRequest(
        cls,
        request: GetSignInChallengeRequest
    ) -> GetSignInChallengeResponse:
        response = GetSignInChallengeResponse()

        # Get salt from server
        try:
            user = User.fromGetSignInChallengeRequest(request)
            try:
                passwordSalt = getUserSpecificSalt(user)
            except Exception as e:
                print(e, "No user was found.")
                response.setMessage(e)
                response.setStatusCode(404)
            else:
                response.setPasswordSalt(passwordSalt) # TODO might need conversion
                response.setNonce(__generateServerNonce())
        except Exception as e:
            print(e, "Error converting GetSignInChallengeRequest to User.")
            response.setMessage(e)
            response.setStatusCode(400)
        finally:
            return response

    def __generateServerNonce(length: int = 16) -> bytes:
        return base64.b64encode(os.urandom(length), altchars=b'-_'))

    @classmethod
    def nonceHashAuthenticationRequest(cls):
        # return nonceHashAuthenticationResponse
        pass

    @classmethod
    def __getPasswordHashRequest(cls):
        # return __getPasswordHashResponse
        pass

    @classmethod
    def __compareNonceHashes(cls):
        pass
