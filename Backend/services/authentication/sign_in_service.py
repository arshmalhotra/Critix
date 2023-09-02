import os
import base64

import GetSignInChallengeRequest, GetSignInChallengeResponse from Components.Authentication.GetSignInChallenge
import getUserSpecificSalt from database.connector # TODO change into class?

class SignInService:

    def __init__(self):
        pass

    def executeGetSignInChallengeRequest(self,
        request: GetSignInChallengeRequest
    ) -> GetSignInChallengeResponse:
        response = GetSignInChallengeResponse()
        __getServerSalt(request, response) # sets it in response
        __generateServerNonce(response=response)

        return response

    def __getServerSalt(request: GetSignInChallengeRequest,
        response: GetSignInChallengeResponse
    ):
        user = User.createFromGetSignInChallengeRequest(request)
        getUserSpecificSalt(user, response)


    def __generateServerNonce(length: int = 16,
        response: GetSignInChallengeResponse
    ) -> bytes:
        response.setNonce(base64.b64encode(os.urandom(length), altchars=b'-_'))


    def nonceHashAuthenticationRequest(self):
        # return nonceHashAuthenticationResponse
        pass

    def __getPasswordHashRequest(self):
        # return __getPasswordHashResponse
        pass

    def __compareNonceHashes(self):
        pass
