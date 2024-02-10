import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

#config.read("..\\Configuration\\config.ini")

class Readconfig:
    @staticmethod
    def getUsername():
        Email = config.get('login data', 'Username')
        return Email

    @staticmethod
    def getPassword():
        Password = config.get('login data', 'password')
        return Password

