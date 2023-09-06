class SignUpService:
    def __init__(self, body):
        self.email = '' or body['email']
        self.phoneNum = '' or body['phoneNum']
        self.username = body['username']
        self.password = body['password']
        self.salt = '' or body['salt']
        self.name = '' or body['name']
        self.profilePic = '' or body['profilePic']
        self.statusCode = 200;
    
    def check_email(self):
        self.statusCode = 200
        #make db call
        # if db response is not empty return 409 'Email already exists'
        # else:
        return 'Email is valid'
        # pass

    def check_phoneNum(self):
        pass

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
            #send above info + salt, name and profile pic to db in try catch
            return ['inserting user data into db', 201]
        else:
            missing = []
            attrs = dir(self)
            attrs = [attr for attr in attrs if not attr.startswith('__')]
            for attr in attrs:
                val = getattr(self, attr)
                if val == '':
                    missing.append(attr)

            return [f'Empty fields: {missing}', 400]
        
        return ['general error', 500] # try to remove
    