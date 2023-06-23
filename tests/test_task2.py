from pytest import fixture


@fixture(scope='session')
def glorioso(project, accounts):
    return project.Glorioso.deploy(sender=accounts[0])

def test_birth(glorioso):
    assert glorioso.get_birth() == 1904

def test_championships(glorioso, accounts):
    assert glorioso.championships() == 37
    assert glorioso.win.call(sender=accounts[0]) == 38

def test_points(glorioso, accounts):
    assert glorioso.points() == 0
    assert glorioso.add_points(3, sender=accounts[0])
    assert glorioso.points() == 3