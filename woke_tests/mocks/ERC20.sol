pragma solidity 0.8.20;

import '../../src/UniswapV2ERC20.sol';

contract ERC20 is UniswapV2ERC20 {
    constructor(uint _totalSupply) public {
        _mint(msg.sender, _totalSupply);
    }
    function mint(address to, uint amount) external {
        _mint(to, amount);
    }
}
