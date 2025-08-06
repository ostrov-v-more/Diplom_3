from faker import Faker


class DataHelper:
    _fake = Faker('ru_RU')

    @staticmethod
    def generate_name() -> str:
        return DataHelper._fake.first_name()

    @staticmethod
    def generate_email() -> str:
        return DataHelper._fake.email()

    @staticmethod
    def generate_password() -> str:
        return DataHelper._fake.password()
