import os


class TwilioConfig:
    def __init__(self, account_sid: str, auth_token: str, number: str):
        self.__account_sid = account_sid
        self.__auth_token = auth_token
        self.__number = number

    def get_account_sid(self):
        return self.__account_sid

    def get_auth_token(self):
        return self.__auth_token

    def get_number(self):
        return self.__number

    @staticmethod
    def from_env():
        return TwilioConfig(
            os.environ["ACCOUNT_SID"],
            os.environ["AUTH_TOKEN"],
            os.environ["NUMBER"],
        )

