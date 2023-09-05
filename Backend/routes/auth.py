from flask import Blueprint, render_template, session, abort, request
from services.authentication import sign_in_service, sign_up_service

sign_in = Blueprint('sign_in', __name__)
@sign_in.route('/sign_in')
def sign_in_route():
    return sign_in_service.sign_in()

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