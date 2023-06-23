from ape import accounts

def main():
    user = accounts.load("user")
    print(user.address)