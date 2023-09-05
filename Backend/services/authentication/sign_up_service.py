class SignUpService:
    def __init__(self, body):
        self.email = body['email']
        self.phoneNum = body['phoneNum']
        self.username = body['username']
        self.password = body['password']
        self.name = body['name']

    def sign_up(self):
        if self.email != '' and self.phoneNum == '' and self.username == '':
            # make db call and do if else
            return ['checking database for email', 200]

        if self.email == '' and self.phoneNum != '' and self.username == '':
            # make db call
            return ['checking database for phoneNum', 200]

        if self.email == '' and self.phoneNum == '' and self.username != '':
            # make db call
            return ['checking database for username', 200]

        if self.email != '' and self.phoneNum != '' and self.username != '' and self.password != '' and self.name != '':
            # make db call
            return ['inserting user data into db', 201]
        
        return ['general error', 500] # try to remove
    