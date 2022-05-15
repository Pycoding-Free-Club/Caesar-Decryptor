class CaesarDecryptor:
    def __init__(self):
        self.letters =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def check(self, password, salt):
        if type(password) != str:
            try:
                password = str(password)
            except:
                raise ValueError("Argument Password must be a string")

        if type(salt) != int:
            try:
                salt = int(salt)
            except:
                raise ValueError("Argument Salt must be a string")

        return {
            "password": password,
            "salt": salt,
        }

    def calculate(self, password, salt):
        is_correct = self.check(password, salt)
        password = is_correct["password"]
        salt = is_correct["salt"]

        result = ""

        for pwd in password:
            if pwd == " ":
                result += " "
            else:
                pwd = pwd.lower()
                index = self.letters.index(pwd)
                letter = self.letters[index]
                if pwd.upper() == letter.upper():
                    result += self.letters[index + salt]

        return result
