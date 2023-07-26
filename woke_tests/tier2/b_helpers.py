from woke_tests.common import *
from .a_init import *


class Helpers(Init):
    def random_user(s) -> Account:
        return random.choice(s.users)

    def random_pair(s) -> UniswapV2Pair:
        return random.choice(s.pairs)

    def random_token(s) -> ERC20:
        return random.choice(s.tokens)

    # 138   │     /// We have:
    # 139   │     /// Δy = (-yΔx)/(x+Δx)
    # 140   │     /// For full derivation, see the attached equation.
    # 141   │     function getDeltaY(
    # 142   │         uint x,
    # 143   │         uint y,
    # 144   │         uint deltaX
    # 145   │     ) public pure returns (uint256 deltaY) {
    # 146   │         uint num = y * deltaX;
    # 147   │         uint den = x + deltaX;
    # 148   │         deltaY = num / den;
    # 149   │     }

    @staticmethod
    def constant_product(x: int, y: int, deltaX: int) -> float:
        num = y * deltaX
        den = x + deltaX
        return num / den
