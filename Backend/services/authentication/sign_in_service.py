import os
import base64

from components.user import User
from components.authentication.get_sign_in_challenge import GetSignInChallengeRequest, GetSignInChallengeResponse
from components.authentication.nonce_hash_authentication import NonceHashAuthenticationRequest, NonceHashAuthenticationResponse
import database.queries as dbQueries

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
                dbQueries.getUserSpecificSalt(user)
            except Exception as e:
                print(e, "No user was found.")
                response.setMessage(repr(e)).setStatusCode(404)
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
                    dbQueries.storeTemporaryNonce(user)
                except Exception as e:
                    print('Not able to store nonce.')
                    response.setMessage(repr(e)).setStatusCode(500)
        except Exception as e:
            print(e, "Error converting GetSignInChallengeRequest to User.")
            response.setMessage(repr(e)).setStatusCode(400)
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
        dbQueries.getUserPasswordHash(user)
        # Get server nonce from database (auto deletes)
        dbQueries.getTemporaryNonce(user)
        # hash(server nonce + password hash + client nonce), compare
        try:
            serverNonceHash = user.createNonceHash(request.getClientNonce())
            if serverNonceHash != request.getNonceHash():
                response.setMessage('Invalid credentials.').setStatusCode(401)
            else:
                # get user id
                try:
                    dbQueries.getFullUser(user)
                except ValueError as ve:
                    print(e, "No user found.")
                    response.setMessage(repr(ve)).setStatusCode(404)
                except mysql.connector.errors.InternalError as ie:
                    print(e, "Too many users found.")
                    response.setMessage(repr(ie)).setStatusCode(500)
                # auth token
                try:
                    authToken = user.encodeAuthToken()
                    response.setAuthToken(authToken
                            ).setMessage('Success: Retrieved auth token.'
                            ).setStatusCode(200)
                except ValueError as ve:
                    print(e, "Error encoding auth token.")
                    response.setMessage(repr(ve)).setStatusCode(404)
                except Exception as e:
                    response.setMessage(repr(e)).setStatusCode(500)
        except ValueError as e:
            print(e, "Error recreating nonce hash.")
            response.setMessage(repr(e)).setStatusCode(500)
        finally:
            return response
