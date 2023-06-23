from ape import convert, networks
from pytest import fixture

MY_TOKEN = "0x..."

@fixture
def uniswap_quoter(project):
    with networks.polygon.mumbai.use_provider("alchemy"):
        return project.UniswapQuoter.at("0xb27308f9F90D607463bb33eA1BeBb41C27CE5AB6")


def test_price(uniswap_quoter):
    token0 = MY_TOKEN
    token1 = "0x468226e47738C470E07AAEAdbF44cEE3A869812F" # dUSDC
    fee = 3000
    amount = int(1e8)

    with networks.polygon.mumbai.use_provider("alchemy"):
        px = uniswap_quoter.quoteExactInputSingle(token0, token1, fee, amount, 0) / 1e18
    print(px)
    assert px > 0