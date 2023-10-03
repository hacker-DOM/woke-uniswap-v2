import sys
import typing
from contextlib import contextmanager

from woke.testing import *
from woke.testing import default_chain as chain
import ipdb

from pytypes.src.UniswapV2Pair import UniswapV2Pair
from pytypes.src.UniswapV2Factory import UniswapV2Factory
from pytypes.src.UniswapV2Router02 import UniswapV2Router02
from pytypes.woke_tests.mocks.ERC20 import ERC20
# from pytypes.woke_tests.mocks.Factory import Factory

sys.excepthook = lambda *args: ipdb.pm()

# def on_revert_handler(e: TransactionRevertedError):
#     if e.tx is not None:
#         print(e.tx.call_trace)
#         print(e.tx.console_logs)

@contextmanager
def snapshot_and_revert_fix(chain: Chain):
    # anvil bug, need to put the timestamp back where it was, snapshot_revert doesn't correctly restore ts
    # when this ticket is closed, we can remove this block and just use snapshot_and_revert decorator
    # https://github.com/foundry-rs/foundry/issues/5518
    ts = chain.blocks[-1].timestamp
    with chain.snapshot_and_revert():
        yield
    chain.set_next_block_timestamp(ts + 1)

import pathlib
csv = pathlib.Path('gitignore/flows_and_txns.csv')
# this overwrites the file
_ = csv.write_text('sequence_number,flow_number,flow_name,block_number,block_timestamp,from,to,return_value,events,console_logs\n')
def tx_callback(tx: TransactionAbc):
    print("\n")
    print(f"Trasaction console logs: {tx.console_logs}")
    print(tx.console_logs)
    print(f"Executed transaction in block #{tx.block_number}\nFrom: {tx.from_}\nTo: {tx.to}\nReturn value: {tx.return_value}")
    print(f"Trasaction events: {tx.events}")
    print(tx.events)
    print("\n")
    with open(csv, 'a') as f:
        f.write(f",,,{tx.block_number},{tx.block.timestamp},{tx.from_},{tx.to},{tx.return_value},{tx.events},{tx.console_logs}\n")

# launch a new development chain (Anvil)
@chain.connect()
# @on_revert(on_revert_handler)
def main():
    chain.tx_callback = tx_callback
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
    acc_pair = UniswapV2Pair(event.pair)

    assert acc_pair.address == tx.return_value, "pair address mismatch"

    acc_token0.transfer(acc_pair, 10 * 10 ** 18)
    acc_token1.transfer(acc_pair, 10 * 10 ** 18)
    tx = acc_pair.mint(acc_alice)
    event = typing.cast(UniswapV2Pair.Mint, tx.events[-1])

    acc_weth = ERC20.deploy(0) # won't be needing deposit etc.
    acc_router = UniswapV2Router02.deploy(acc_factory, acc_weth)

    acc_bob = chain.accounts[1]
    chain.set_default_accounts(acc_bob)

    acc_token0.mint(acc_bob, 100 * 10 ** 18)
    acc_token1.mint(acc_bob, 100 * 10 ** 18)

    # with snapshot_and_revert_fix(chain):
    #     acc_token1.approve(acc_router, 2 ** 256 - 1)
    #     path1_tx1_fee = acc_router.swapExactTokensForTokens(
    #         5 * 10 ** 18,
    #         0,
    #         [acc_token1, acc_token0],
    #         acc_bob,
    #         2 ** 256 - 1,
    #     )
    #     path1_tx2_fee = acc_router.swapExactTokensForTokens(
    #         5 * 10 ** 18,
    #         0,
    #         [acc_token1, acc_token0],
    #         acc_bob,
    #         2 ** 256 - 1,
    #     )
    #
    # with snapshot_and_revert_fix(chain):
    #     acc_token1.approve(acc_router, 2 ** 256 - 1)
    #     path2_tx1_no_fee = acc_router.swapExactTokensForTokens_noFee(
    #         5 * 10 ** 18,
    #         0,
    #         [acc_token1, acc_token0],
    #         acc_bob,
    #         2 ** 256 - 1,
    #     )
    #     path2_tx2_fee = acc_router.swapExactTokensForTokens(
    #         5 * 10 ** 18,
    #         0,
    #         [acc_token1, acc_token0],
    #         acc_bob,
    #         2 ** 256 - 1,
    #     )
    #
    # print(f"path1_tx1_fee: {path1_tx1_fee.return_value}")
    # print(f"path1_tx2_fee: {path1_tx2_fee.return_value}")
    # print(f"path2_tx1_no_fee: {path2_tx1_no_fee.return_value}")
    # print(f"path2_tx2_fee: {path2_tx2_fee.return_value}")

    with snapshot_and_revert_fix(chain):
        acc_token1.approve(acc_router, 2 ** 256 - 1)
        path1_tx1_fee = acc_router.swapTokensForExactTokens(
            3333333333333333333,
            2 ** 256 - 1,
            [acc_token1, acc_token0],
            acc_bob,
            2 ** 256 - 1,
        )
        path1_tx2_fee = acc_router.swapTokensForExactTokens(
            3333333333333333333,
            2 ** 256 - 1,
            [acc_token1, acc_token0],
            acc_bob,
            2 ** 256 - 1,
        )

    with snapshot_and_revert_fix(chain):
        acc_token1.approve(acc_router, 2 ** 256 - 1)
        path2_tx1_no_fee = acc_router.swapTokensForExactTokens_noFee(
            3333333333333333333,
            2 ** 256 - 1,
            [acc_token1, acc_token0],
            acc_bob,
            2 ** 256 - 1,
        )
        path2_tx2_fee = acc_router.swapTokensForExactTokens(
            3333333333333333333,
            2 ** 256 - 1,
            [acc_token1, acc_token0],
            acc_bob,
            2 ** 256 - 1,
        )

    print(f"path1_tx1_fee: {path1_tx1_fee.return_value}")
    print(f"path1_tx2_fee: {path1_tx2_fee.return_value}")
    print(f"path2_tx1_no_fee: {path2_tx1_no_fee.return_value}")
    print(f"path2_tx2_fee: {path2_tx2_fee.return_value}")


    # with snapshot_and_revert_fix(chain):
    #     acc_token0.approve(acc_router, 2 ** 256 - 1)
    #     tx0 = acc_router.swapExactTokensForTokens(
    #         10 * 10 ** 18,
    #         0,
    #         [acc_token0, acc_token1],
    #         acc_bob,
    #         2 ** 256 - 1,
    #     )
    #
    # with snapshot_and_revert_fix(chain):
    #     acc_token0.approve(acc_router, 2 ** 256 - 1)
    #     tx1 = acc_router.swapExactTokensForTokens(
    #         5 * 10 ** 18,
    #         0,
    #         [acc_token0, acc_token1],
    #         acc_bob,
    #         2 ** 256 - 1,
    #     )
    #     tx2 = acc_router.swapExactTokensForTokens(
    #         5 * 10 ** 18,
    #         0,
    #         [acc_token0, acc_token1],
    #         acc_bob,
    #         2 ** 256 - 1,
    #     )
    #
    # print("tx0.return_value", tx0.return_value)
    # print("tx1.return_value", tx1.return_value)
    # print("tx2.return_value", tx2.return_value)
    #
