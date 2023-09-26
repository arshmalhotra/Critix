from flask import Blueprint, render_template, session, abort, request, make_response
from components.authentication.get_sign_in_challenge import GetSignInChallengeRequest
from components.authentication.nonce_hash_authentication import NonceHashAuthenticationRequest
from services.authentication import sign_up_service
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
@get_sign_in_challenge.route('/get_sign_in_challenge', methods=['GET', 'POST'])
def get_sign_in_challenge_route():
    req_body = request.form
    if not req_body:
        return make_response('Request Error: No request body provided.', 400)

    # Create request object
    try:
        challengeRequest = GetSignInChallengeRequest.fromHttpRequestBody(req_body)
    except TypeError as e:
        return make_response('Could not create challenge request: ' + str(e), 400)

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
    nonceHash: bytes [required]
    clientNonce: bytes [required]
}
Response:
{
    message: str
    auth_token: str
}
"""
sign_in = Blueprint('sign_in', __name__)
@sign_in.route('/sign_in', methods = ['GET', 'POST'])
def sign_in_route():
    req_body = request.form
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

sign_up = Blueprint('sign_up', __name__)
@sign_up.route('/sign_up', methods=['POST'])
def sign_up_route():
    try:
        data = request.get_json() # python dict
        temp = sign_up_service.SignUpService(data)
        res_body = {'message': temp.sign_up()[0]}
        return res_body, temp.sign_up()[1]
    except Exception as e:
        res_body = {'Message': repr(e)}
        return res_body, 500

@sign_up.route('/sign_up/check_valid_email', methods=['POST'])
def check_valid_email_route():
    try:
        data = request.get_json()
        temp = sign_up_service.SignUpService(data)
        res_body = {'message': temp.check_email()[0]}
        return res_body, temp
    except Exception as e:
        return {'Message': repr(e)}, 500
