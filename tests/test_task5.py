from ape import accounts, networks, project


def test_account():
    account = accounts.load('workshop')

    with networks.polygon.mumbai.use_provider("alchemy"):
        usdc = project.Token.at("0x468226e47738C470E07AAEAdbF44cEE3A869812F")
        assert usdc.balanceOf(account.address) > 0