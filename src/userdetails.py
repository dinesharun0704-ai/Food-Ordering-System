class User:
    def __init__(self, name, ph, mail, password):
        self.name = name
        self.ph = ph
        self.mail = mail
        self.password = password

    def __str__(self):
        return f"User(name={self.name}, ph={self.ph}, mail={self.mail})"


class UserData:
    __PersonDetails = []

    @classmethod
    def AddDetails(cls, det):
        cls.__PersonDetails.append(det)

    @classmethod
    def UserVerify(cls, id, passkey):
        for users in cls.__PersonDetails:
            if users.mail == id and users.password == passkey:
                return users
        return None
