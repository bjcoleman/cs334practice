
class Config:

    def get_delay(self):
        return 100

    def get_secret(self):
        return 42

    def code_without_test(self):
        x = 42
        y = 73
        z = 93
        q = x + y + z
        return q