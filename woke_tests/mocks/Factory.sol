pragma solidity 0.8.20;

import "../../src/UniswapV2Pair.sol";

contract Factory {
    address public feeTo = address(0);

    event PairCreated(
        address token0,
        address token1,
        address pair
    );
    function createPair(address token0, address token1) external {
        UniswapV2Pair pair = new UniswapV2Pair();
        pair.initialize(token0, token1);
        emit PairCreated(token0, token1, address(pair));
    }
}
