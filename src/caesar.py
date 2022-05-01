class CaesarDecryptor:
    def __init__(self):
        self.letters =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def check(self, password, salt, mode):
        if type(password) != str:
            try:
                password = str(password)
            except:
                raise ValueError("Argument Password must be a string")

        if type(salt) != int:
            try:
                salt = int(salt)
            except:
                raise ValueError("Argument Password must be a string")

        if type(mode) != bool:
            try:
                salt = bool(salt)
            except:
                raise ValueError("Argument Password must be a string")

        return {
            "password": password,
            "salt": salt,
            "mode": mode,
        }

    def calculate(self, password, salt, mode):
        is_correct = self.check(password, salt, mode)
        password = is_correct["password"]
        salt = is_correct["salt"]
        mode = is_correct["mode"]

        result = ""

        for pwd in password:
            pwd = pwd.lower()
            index = self.letters.index(pwd)
            letter = self.letters[index]
            if pwd.upper() == letter.upper():
                if mode:
                    result += self.letters[index + salt]
                else:
                    result += self.letters[index - salt]

        return result

