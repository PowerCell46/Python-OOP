class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        email = email.split("@")
        name = self.__is_name_valid(email[0])
        email = email[1].split(".")
        mail = self.__is_mail_valid(email[0])
        domain = self.__is_domain_valid(email[1])
        if name and mail and domain:
            return True
        else:
            return False
