from woke.testing import *
from woke.testing import default_chain as chain

from pytypes.woke_tests.mocks.ERC20 import ERC20
from pytypes.woke_tests.mocks.Factory import Factory


# launch a new development chain (Anvil)
@chain.connect()
def test():
    # token0 candidate
    token0_cand = ERC20.deploy(_totalSupply = 100 * 10 ** 18, from_ = chain.accounts[0])
    # token1 candidate
    token1_cand = ERC20.deploy(_totalSupply = 100 * 10 ** 18, from_ = chain.accounts[0])
    token0 = token0_cand if token0_cand.address < token1_cand.address else token1_cand
    token1 = token1_cand if token0_cand.address < token1_cand.address else token0_cand
    factory = Factory.deploy(from_ = chain.accounts[0])
    # create pair
    tx = factory.createPair(token0, token1, from_ = chain.accounts[0])
    pair = tx.events['PairCreated']['pair']
    print('pair', pair)
