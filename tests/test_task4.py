from pytest import fixture


@fixture(scope="session")
def signer(accounts):
    return accounts[0]

@fixture(scope="session")
def token(project, signer):
    return signer.deploy(project.Token, "MyToken", "TKN")


def test_name(token):
    assert token.name() == "MyToken"


def test_symbol(token):
    assert token.symbol() == "TKN"


def test_decimals(token):
    assert token.decimals() == 8


def test_total_supply(token, signer):
    assert token.totalSupply() == 5000e8
    assert token.balanceOf(signer) == 5000e8