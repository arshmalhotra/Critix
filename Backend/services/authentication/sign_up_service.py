from flask import make_response, Response, jsonify
from mysql.connector.errors import DatabaseError

from components.user import User
import database.queries as dbQueries

class SignUpService:

    def __init__(self, email: str = '', phoneNumber: str = '',
        username: str = '', passwordHash: str = '', passwordSalt: str = '',
        name: str = '', profilePicture: str = ''
    ):
        self.user = User(**{
            attr: val for attr, val in locals().items() if attr != 'self'
        })

        self.email = email
        self.phoneNumber = phoneNumber
        self.username = username
        self.password = User.cleanJsonBytes(passwordHash)
        self.salt = User.cleanJsonBytes(passwordSalt)
        self.name = name
        self.profilePic = profilePicture

        self.responseBody = {'message': 'Internal Server Error'}
        self.statusCode = 500;

    def validate_new_user(self) -> None:
        if not(self.email or self.phoneNumber or self.username):
            self.responseBody['message'] = 'Request Error: Invalid request body provided.'
            self.statusCode = 400
            return {}

        try:
            dbQueries.validateNewUser(self.user)
        except ValueError as ve:
            self.responseBody['message'] = 'Conflict: User already exists.'
            self.statusCode = 409
        except Exception as e:
            print(repr(e))
            self.responseBody['message'] = f'Internal Server Error: {repr(e)}'
            self.statusCode = 500
        else:
            self.responseBody['message'] = 'Success: No user found.'
            self.statusCode = 200

    def sign_up(self) -> None:
        if self.email and self.phoneNumber and self.username and self.name and self.password and self.salt:
            try:
                dbQueries.createNewUser(self.user)
                # User already filled out
                if self.user.getUserId():
                    authToken = self.user.encodeAuthToken()
                    self.responseBody['authToken'] = authToken
            except Exception as e:
                print(repr(e))
                self.responseBody['message'] = f'Internal Server Error: {repr(e)}'
                self.statusCode = 500
        else:
            self.responseBody['message'] = 'Request Error: Invalid request body provided.'
            self.statusCode = 500

    def to_flask_response(self, body: dict = {}) -> Response:
        self.responseBody.update(body)

        return make_response(jsonify(self.responseBody), self.statusCode)
