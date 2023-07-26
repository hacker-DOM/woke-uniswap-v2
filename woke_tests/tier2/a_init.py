from woke_tests.common import *

from pytypes.src.UniswapV2Factory import UniswapV2Factory
from pytypes.src.UniswapV2Pair import UniswapV2Pair
from pytypes.woke_tests.mocks.ERC20 import ERC20

class Init(FuzzTest):
    chain: Chain
    paccs: Tuple[Account, ...]
    users: Tuple[Account, ...]
    state: State # pyright: ignore [reportUninitializedInstanceVariable]

    tokens: List[ERC20]
    factory: UniswapV2Factory
    pairs: List[UniswapV2Pair]

    def __init__(s):
        super().__init__()

        # ===== Initialize accounts =====
        s.chain = default_chain
        s.paccs = tuple(s.chain.accounts[i] for i in range(NUM_PACCS))
        s.users = tuple(s.chain.accounts[NUM_PACCS:NUM_PACCS+NUM_USERS])

        # ===== Initialize variables =====
        # s.tokens = []
        # s.pairs = []

        # ===== Add labels =====
        for idx, usr in enumerate(s.users):
            usr.label = crypto_names[idx]

