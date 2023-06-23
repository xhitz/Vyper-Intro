# @version ^0.3.6

from vyper.interfaces import ERC20

FAUCET_VALUE: constant(uint256) = as_wei_value(1000, "ether")

has_received: public(HashMap[address, bool])
token: public(ERC20)

@external
def __init__(_token: address):
    self.token = ERC20(_token)

@external
@view
def getBalance() -> uint256:
    return self.token.balanceOf(self)

@external
def deposit(_amount: uint256):
    self.token.transferFrom(msg.sender, self, _amount)

@external
def withdraw():
    assert self.token.balanceOf(self) >= FAUCET_VALUE, "Not enough balance"
    assert self.has_received[msg.sender] == False, "Has already received"
    self.token.transfer(msg.sender, FAUCET_VALUE)
    self.has_received[msg.sender] = True