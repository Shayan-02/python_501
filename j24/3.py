class User:
    def __init__(self, name, national_code):
        """
        Purpose: one
        """

        self.name = name
        self.national_code = national_code

    @staticmethod
    def is10digits(national_code):
        return len(national_code) == 10


u1 = User("ali", "0987654321")
u2 = User("ali", "987654321")
print(u2.is10digits(u2.national_code))
