class CaesarDecryptor:
    def __init__(self, password, salt):
        self.password = password
        self.salt = salt
        self.letters =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        self.check()

    def check(self):
        if type(self.salt) != int:
            try:
                self.salt = int(self.salt)
            except:
                print("Argument Salt must be a number")

    def basic(self, mode):
        result = ""

        for pwd in self.password:
            for index, letter in enumerate(self.letters, 0):
                if pwd.upper() == letter.upper():
                    if mode:
                        result += self.letters[index + self.salt]
                    else:
                        result += self.letters[index - self.salt]
                else:
                    continue

        return result

    def decryption(self):
        # 복호화
        return self.basic(False)
        
    def encryption(self):
        # 암호화
        return self.basic(True)

