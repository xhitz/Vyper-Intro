from ape import accounts, networks, project

def test_presence():
    account = accounts.load('workshop')
    attendants = project.Registration.at('0xa6cb85062cf15c65398c33b8fb8268669e575310')
    with networks.polygon.mumbai.use_provider("alchemy"):
        assert attendants.is_present(account.address)