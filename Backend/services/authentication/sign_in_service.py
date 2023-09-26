import os
import base64

from components.user import User
from components.authentication.get_sign_in_challenge import GetSignInChallengeRequest, GetSignInChallengeResponse
from components.authentication.nonce_hash_authentication import NonceHashAuthenticationRequest, NonceHashAuthenticationResponse
from database.queries import getUserSpecificSalt, storeTemporaryNonce, getTemporaryNonce, getUserPasswordHash, getUserId

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
                response.setMessage(str(e)).setStatusCode(404)
            else:
                response.setPasswordSalt(
                    user.getPasswordDetails()['passwordSalt']
                )
                serverNonce = cls.__generateServerNonce()
                response.setNonce(serverNonce
                        ).setMessage('Success: Retrieved salt and nonce.'
                        ).setStatusCode(200)
                user.setTemporaryNonce(serverNonce)
                try:
                    storeTemporaryNonce(user)
                except Exception as e:
                    print('Not able to store nonce.')
                    response.setMessage(str(e)).setStatusCode(500)
        except Exception as e:
            print(e, "Error converting GetSignInChallengeRequest to User.")
            response.setMessage(str(e)).setStatusCode(400)
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
                response.setMessage('Invalid credentials.').setStatusCode(401)
            else:
                # get user id
                try:
                    getUserId(user)
                except ValueError as ve:
                    print(e, "Error retrieving user ID.")
                    response.setMessage(str(ve)).setStatusCode(404)
                except mysql.connector.errors.InternalError as ie:
                    print(e, "Error retrieving user ID.")
                    response.setMessage(str(ie)).setStatusCode(500)
                # auth token
                try:
                    authToken = user.encodeAuthToken()
                    response.setAuthToken(authToken
                            ).setMessage('Success: Retrieved auth token.'
                            ).setStatusCode(200)
                except ValueError as ve:
                    print(e, "Error encoding auth token.")
                    response.setMessage(str(ve)).setStatusCode(404)
                except Exception as e:
                    response.setMessage(str(e)).setStatusCode(500)
        except ValueError as e:
            print(e, "Error recreating nonce hash.")
            response.setMessage(str(e)).setStatusCode(500)
        finally:
            return response
