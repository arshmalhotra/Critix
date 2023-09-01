from flask import Blueprint, render_template, session, abort
from services.authentication import sign_in_service, sign_up_service

sign_in = Blueprint('sign_in', __name__)
@sign_in.route('/sign_in')
def sign_in_route():
    return sign_in_service.sign_in()

sign_up = Blueprint('sign_up', __name__)
@sign_up.route('/sign_up')
def sign_up_route():
    return sign_up_service.sign_up()