# @version ^0.3.6


# Define public state variables
championships: public(uint8)
points: public(uint256)

    # Define non-public state variable
birth: uint256

@external
    # Initialize the variables on contract creation
def __init__():
    self.birth = 1904
    self.championships = 37


    # Define function to add 1 to the state variable championships
    # and return the new value
@external
def win() -> uint8:
    self.championships += 1
    return self.championships
    
@external
    # Define function to add points to the state variable points
def add_points(step: uint256):
    self.points += step


@view
@external
    # Define function to return the value of the state variable birth
def get_birth() -> uint256:
    return self.birth
