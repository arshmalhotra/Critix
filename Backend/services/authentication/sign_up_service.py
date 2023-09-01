def sign_up(email="", phoneNum="", username="", password="", name="", profilePic="default_pic"):
    if email != "" and phoneNum == "" and username == "":
        # make db call
        pass

    if email == "" and phoneNum != "" and username == "":
        # make db call
        pass

    if email == "" and phoneNum == "" and username != "":
        # make db call
        pass

    if email != "" and phoneNum != "" and username != "" and password != "" and name != "":
        # make db call
        pass

    return "did sign up"