from ape import accounts, project

def main():
    account = accounts.load("workshop")

    registry = project.Registration.at("0xa6cb85062cf15c65398c33b8fb8268669e575310")

    registry.checkin("0xNathan", sender=account)