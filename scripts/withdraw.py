from ape import project, accounts

def main():
    user = accounts.load("workshop")
    faucet = project.Faucet.at("Faucet Address")

    faucet.withdraw(sender=user)