import os

from ape import accounts, networks
from dotenv import load_dotenv
from pytest import fixture

load_dotenv()


@fixture(scope="session")
def workshop_user():
    user = accounts.load("workshop")
    user.set_autosign(True, passphrase=os.environ.get("PASS"))
    return user


@fixture
def price_feed(project, workshop_user):
    with networks.polygon.mumbai.use_provider("alchemy"):
        return project.MyFeed.deploy(sender=workshop_user)


def test_feed(price_feed):
    with networks.polygon.mumbai.use_provider("alchemy"):
        assert price_feed.get_description() == "BTC / USD"

def test_price(price_feed):
    with networks.polygon.mumbai.use_provider("alchemy"):
        assert 10e3 < (price_feed.get_latest_price() / 1e8) < 50e3