from flask import Blueprint, render_template, session, abort, request, make_response
from services.authentication import sign_up_service
from services.authentication.sign_in_service import SignInService

get_sign_in_challenge = Blueprint('get_sign_in_challenge', __name__)
@get_sign_in_challenge.route('/get_sign_in_challenge', methods=['POST'])
def get_sign_in_challenge_route():
    req_body = request.form
    if not req_body:
        return make_response('Request Error: No request body provided.', 400)
    # Create request object
    try:
        challengeRequest = GetSignInChallengeRequest
            .fromHttpRequestBody(req_body)
    except Exception as e:
        return make_response(e, 400)

    # Execute request and get response
    challengeResponse = SignInService
        .executeGetSignInChallengeRequest(challengeRequest)
    res = challengeResponse.toFlaskResponse()

    return res

sign_in = Blueprint('sign_in', __name__)
@sign_in.route('/sign_in')
def sign_in_route():
    pass

sign_up = Blueprint('sign_up', __name__)
@sign_up.route('/sign_up', methods=['POST'])
def sign_up_route():
    try:
        # parse http request
        return sign_up_service.sign_up()
    except:
        # return http status code and error message
        return "Error during sign up"
