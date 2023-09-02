def sign_up(data):
    if data['email'] != '' and data['phoneNum'] == '' and data['username'] == '':
        # make db call and do if else
        return ['checking database for email', 200]

    if data['email'] == '' and data['phoneNum'] != '' and data['username'] == '':
        # make db call
        return ['checking database for phoneNum', 200]

    if data['email'] == '' and data['phoneNum'] == '' and data['username'] != '':
        # make db call
        return ['checking database for username', 200]

    if data['email'] != '' and data['phoneNum'] != '' and data['username'] != '' and data['password'] != '' and data['name'] != '':
        # make db call
        return ['inserting user data into db', 201]
    
    return ['general error', 500] # try to remove