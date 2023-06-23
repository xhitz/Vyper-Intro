from ape import accounts, networks

def test_account():
    account = accounts.load('workshop')
    
    with networks.polygon.mumbai.use_provider("alchemy"):
        assert account.balance > 0