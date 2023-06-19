class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        if 5 <= len(username) <= 15:
            self.__username = username
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if len(value) > 7:
            flag = False
            for letter in value:
                if 64 < ord(letter) < 91:
                    flag = True
                    break
            second_flag = False
            for letter in value:
                if 47 < ord(letter) < 58:
                    second_flag = True
                    break
            if second_flag and flag:
                self.__password = value
            else:
                raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {len(self.__password) * "*"}'
