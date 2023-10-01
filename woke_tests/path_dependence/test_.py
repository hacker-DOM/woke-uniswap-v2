import sys
import typing

from woke.testing import *
from woke.testing import default_chain as chain
import ipdb

from pytypes.src.UniswapV2Pair import UniswapV2Pair
from pytypes.src.UniswapV2Factory import UniswapV2Factory
from pytypes.src.UniswapV2Router02 import UniswapV2Router02
from pytypes.woke_tests.mocks.ERC20 import ERC20
# from pytypes.woke_tests.mocks.Factory import Factory

sys.excepthook = lambda *args: ipdb.pm()

# launch a new development chain (Anvil)
@chain.connect()
def test():
    acc_alice = chain.accounts[0]
    chain.set_default_accounts(acc_alice)
    # token0 candidate
    acc_token0_cand = ERC20.deploy(_totalSupply = 100 * 10 ** 18)
    # token1 candidate
    acc_token1_cand = ERC20.deploy(_totalSupply = 100 * 10 ** 18)
    acc_token0 = acc_token0_cand if acc_token0_cand.address < acc_token1_cand.address else acc_token1_cand
    acc_token1 = acc_token1_cand if acc_token0_cand.address < acc_token1_cand.address else acc_token0_cand
    # factory = Factory.deploy()
    acc_factory = UniswapV2Factory.deploy(acc_alice)
    # create pair
    tx = acc_factory.createPair(acc_token0, acc_token1)
    event = typing.cast(UniswapV2Factory.PairCreated, tx.events[-1])
    pair = UniswapV2Pair(event.pair)

    assert pair.address == tx.return_value, "pair address mismatch"

    acc_token0.transfer(pair, 10 * 10 ** 18)
    acc_token1.transfer(pair, 10 * 10 ** 18)
    tx = pair.mint(acc_alice)
    event = typing.cast(UniswapV2Pair.Mint, tx.events[-1])

    acc_weth = ERC20.deploy(0) # won't be needing deposit etc.
    acc_router = UniswapV2Router02.deploy(acc_factory, acc_weth)

    acc_bob = chain.accounts[1]
    chain.set_default_accounts(acc_bob)

    acc_token0.mint(acc_bob, 100 * 10 ** 18)
    acc_token1.mint(acc_bob, 100 * 10 ** 18)

    with chain.snapshot_and_revert():
        acc_token0.approve(acc_router, 2 ** 256 - 1)
        # acc_router.quote(10 * 10 ** 18, 10 * 10 ** 18, 10 * 10 ** 18,
                         # request_type='tx')
        print(chain.blocks[-1].transactions[-1])
        acc_router.swapExactTokensForTokens(
            10 * 10 ** 18,
            0,
            [acc_token0, acc_token1],
            acc_bob,
            2 ** 256 - 1,
        )

