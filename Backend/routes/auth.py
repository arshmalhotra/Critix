from flask import Blueprint, render_template, session, abort, request, make_response

from components.authentication.get_sign_in_challenge import GetSignInChallengeRequest
from components.authentication.nonce_hash_authentication import NonceHashAuthenticationRequest
from services.authentication.sign_up_service import SignUpService
from services.authentication.sign_in_service import SignInService

"""
/get_sign_in_challenge
Request:
{
    email: str [optional]
    username: str [optional]
}
Response:
{
    message: str
    nonce: bytes
    salt: bytes
}
"""
get_sign_in_challenge = Blueprint('get_sign_in_challenge', __name__)
@get_sign_in_challenge.route('/get_sign_in_challenge', methods=['POST'])
def get_sign_in_challenge_route():
    req_body = request.get_json()
    if not req_body:
        return make_response('Request Error: No request body provided.', 400)

    # Create request object
    try:
        challengeRequest = GetSignInChallengeRequest.fromHttpRequestBody(req_body)
    except TypeError as e:
        return make_response('Could not create challenge request: ' + repr(e), 400)

    # Execute request and get response
    challengeResponse = SignInService.executeGetSignInChallengeRequest(challengeRequest)
    res = challengeResponse.toFlaskResponse()

    return res

"""
/sign_in
Request:
{
    email: str [optional]
    username: str [optional]
    nonceHash: bytes
    clientNonce: bytes
}
Response:
{
    message: str
    auth_token: str
}
"""
sign_in = Blueprint('sign_in', __name__)
@sign_in.route('/sign_in', methods = ['POST'])
def sign_in_route():
    req_body = request.get_json()
    if not req_body:
        return make_response('Request Error: No request body provided.', 400)

    # Create reqeust object
    try:
        authenticationRequest = NonceHashAuthenticationRequest.fromHttpRequestBody(req_body)
    except Exception as e:
        return make_response(e, 400)

    # Execute request and get response
    authenticationResponse = SignInService.executeNonceHashAuthenticationRequest(authenticationRequest)
    res = authenticationResponse.toFlaskResponse()

    return res

"""
/sign_up
Request:
{
    email: str
    phoneNumber: str
    passwordHash: bytes
    passwordSalt: bytes
    name: str
    username: str
    profilePicture: str [optional]
}
Response:
{
    message: str
    auth_token: str
}
"""
sign_up = Blueprint('sign_up', __name__)
@sign_up.route('/sign_up', methods=['POST'])
def sign_up_route():
    try:
        req_body = request.get_json()
        sign_up = SignUpService(**req_body)
        sign_up.sign_up()
        res = sign_up.to_flask_response(res_body)
        return res
    except Exception as e:
        return {'Message': repr(e)}, 500

"""
/sign_up/validate
Request:
{
    email: str [optional]
    phoneNumber: str [optional]
    username: str [optional]
}
Response:
{
    message: str
}
"""
@sign_up.route('/sign_up/validate', methods=['POST'])
def check_valid_email_route():
    try:
        req_body = request.get_json()
        sign_up = SignUpService(**req_body)
        sign_up.validate_new_user()
        res = sign_up.to_flask_response()
        return res
    except Exception as e:
        return {'Message': repr(e)}, 500
