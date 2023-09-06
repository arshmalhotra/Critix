import os
import base64

from Components.Authentication.GetSignInChallenge import GetSignInChallengeRequest, GetSignInChallengeResponse
from Components.Authentication.NonceHashAuthentication import NonceHashAuthenticationRequest, NonceHashAuthenticationResponse
from database.connector import getUserSpecificSalt, storeTemporaryNonce, getTemporaryNonce, getUserPasswordHash, getUserId

class SignInService:

    @classmethod
    def executeGetSignInChallengeRequest(
        cls,
        request: GetSignInChallengeRequest
    ) -> GetSignInChallengeResponse:
        response = GetSignInChallengeResponse()

        # Get salt from database
        try:
            user = User.fromGetSignInChallengeRequest(request)
            try:
                getUserSpecificSalt(user)
            except Exception as e:
                print(e, "No user was found.")
                response.setMessage(e)
                response.setStatusCode(404)
            else:
                response.setPasswordSalt(user.getPasswordSalt()) # TODO might need conversion
                serverNonce = __generateServerNonce()
                response.setNonce(serverNonce)
                user.setTemporaryNonce(serverNonce)
                try:
                    storeTemporaryNonce(user)
                except Exception as e:
                    print('Not able to store nonce.')
                    response.setMessage(e)
                    response.setStatusCode(500)
        except Exception as e:
            print(e, "Error converting GetSignInChallengeRequest to User.")
            response.setMessage(e)
            response.setStatusCode(400)
        finally:
            return response

    def __generateServerNonce(length: int = 16) -> bytes:
        return base64.b64encode(os.urandom(length), altchars=b'-_')

    @classmethod
    def executeNonceHashAuthenticationRequest(
        cls,
        request: NonceHashAuthenticationRequest
    ) -> NonceHashAuthenticationResponse:
        response = NonceHashAuthenticationResponse()

        user = User(email=request.getEmail(), username=request.getUsername())
        # Get password hash from database
        getUserPasswordHash(user)
        # Get server nonce from database (auto deletes)
        getTemporaryNonce(user)
        # hash(server nonce + password hash + client nonce), compare
        try:
            serverNonceHash = user.createNonceHash(request.getClientNonce())
            if serverNonceHash != request.getNonceHash():
                response.setMessage('Invalid credentials.')
                response.setStatusCode(401)
            else:
                # get user id
                try:
                    getUserId(user)
                except ValueError as ve:
                    print(e, "Error retrieving user ID.")
                    response.setMessage(ve)
                    response.setStatusCode(404)
                except pymysql.InternalError as ie:
                    print(e, "Error retrieving user ID.")
                    response.setMessage(ie)
                    response.setStatusCode(500)
                # auth token
                try:
                    authToken = user.encodeAuthToken()
                    response.setAuthToken(authToken)
                except ValueError as ve:
                    print(e, "Error encoding auth token.")
                    response.setMessage(ve)
                    response.setStatusCode(404)
                except Exception as e:
                    response.setMessage(e)
                    response.setStatusCode(500)
        except ValueError as e:
            print(e, "Error recreating nonce hash.")
            response.setMessage(e)
            response.setStatusCode(500)
        finally:
            return response
