from flask import Blueprint, render_template, session, abort
from services.authentication import sign_in_service, sign_up_service

sign_in = Blueprint('sign_in', __name__)
@sign_in.route('/sign_in')
def sign_in_route():
    # create GetSignInChallengeRequest
    return sign_in_service.sign_in()

sign_up = Blueprint('sign_up', __name__)
@sign_up.route('/sign_up', methods=['POST'])
def sign_up_route():
    try:
        # parse http request
        return sign_up_service.sign_up()
    except:
        # return http status code and error message
        return "Error during sign up"
