# @version ^0.3.6

struct Person:
    owner: address
    name: String[64]

is_present: public(HashMap[address, bool])
info: public(DynArray[Person, 70])

@external
def checkin(_name: String[64]):
    if not self.is_present[msg.sender]:
        self.info.append(
            Person({owner: msg.sender, name: _name})
            )
        self.is_present[msg.sender] = True

@view
@external
def get() -> DynArray[Person, 70]:
    return self.info