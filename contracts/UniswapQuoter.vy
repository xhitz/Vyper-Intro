# @version ^0.3.6

@external
@view
def quoteExactInputSingle(tokenIn: address, tokenOut: address, fee: uint24, amountIn: uint256, sqrtPriceLimitX96: uint160) -> uint256:
    return 1