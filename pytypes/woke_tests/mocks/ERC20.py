
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from woke.development.core import Contract, Library, Address, Account, Chain, RequestType
from woke.development.primitive_types import *
from woke.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.src.UniswapV2ERC20 import UniswapV2ERC20



class ERC20(UniswapV2ERC20):
    """
    [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/woke_tests/mocks/ERC20.sol#5)
    """
    _abi = {'constructor': {'inputs': [{'internalType': 'uint256', 'name': '_totalSupply', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'6D\xe5\x15': {'inputs': [], 'name': 'DOMAIN_SEPARATOR', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'0\xad\xf8\x1f': {'inputs': [], 'name': 'PERMIT_TYPEHASH', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'\xddb\xed>': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'allowance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\t^\xa7\xb3': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'approve', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'p\xa0\x821': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'1<\xe5g': {'inputs': [], 'name': 'decimals', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, b'@\xc1\x0f\x19': {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'name': 'mint', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x06\xfd\xde\x03': {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'~\xce\xbe\x00': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'nonces', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xd5\x05\xac\xcf': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'deadline', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'v', 'type': 'uint8'}, {'internalType': 'bytes32', 'name': 'r', 'type': 'bytes32'}, {'internalType': 'bytes32', 'name': 's', 'type': 'bytes32'}], 'name': 'permit', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x95\xd8\x9bA': {'inputs': [], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\x18\x16\r\xdd': {'inputs': [], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa9\x05\x9c\xbb': {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'#\xb8r\xdd': {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _creation_code = "608060405234801562000010575f80fd5b5060405162001900380380620019008339818101604052810190620000369190620002d5565b5f4690507f8b73c3c69bb8fe3d512ecc4cf759cc79239f7b179b0ffacaa9a75d522b39400f6040518060400160405280600a81526020017f556e697377617020563200000000000000000000000000000000000000000000815250805190602001206040518060400160405280600181526020017f3100000000000000000000000000000000000000000000000000000000000000815250805190602001208330604051602001620000ed95949392919062000373565b60405160208183030381529060405280519060200120600381905550506200011c33826200012360201b60201c565b50620004ce565b62000139815f546200023c60201b90919060201c565b5f81905550620001908160015f8573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f20546200023c60201b90919060201c565b60015f8473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f20819055508173ffffffffffffffffffffffffffffffffffffffff165f73ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef83604051620002309190620003ce565b60405180910390a35050565b5f8282846200024c919062000416565b915081101562000293576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016200028a90620004ae565b60405180910390fd5b92915050565b5f80fd5b5f819050919050565b620002b1816200029d565b8114620002bc575f80fd5b50565b5f81519050620002cf81620002a6565b92915050565b5f60208284031215620002ed57620002ec62000299565b5b5f620002fc84828501620002bf565b91505092915050565b5f819050919050565b620003198162000305565b82525050565b6200032a816200029d565b82525050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6200035b8262000330565b9050919050565b6200036d816200034f565b82525050565b5f60a082019050620003885f8301886200030e565b6200039760208301876200030e565b620003a660408301866200030e565b620003b560608301856200031f565b620003c4608083018462000362565b9695505050505050565b5f602082019050620003e35f8301846200031f565b92915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f62000422826200029d565b91506200042f836200029d565b92508282019050808211156200044a5762000449620003e9565b5b92915050565b5f82825260208201905092915050565b7f64732d6d6174682d6164642d6f766572666c6f770000000000000000000000005f82015250565b5f6200049660148362000450565b9150620004a38262000460565b602082019050919050565b5f6020820190508181035f830152620004c78162000488565b9050919050565b61142480620004dc5f395ff3fe608060405234801561000f575f80fd5b50600436106100e8575f3560e01c806340c10f191161008a57806395d89b411161006457806395d89b411461025e578063a9059cbb1461027c578063d505accf146102ac578063dd62ed3e146102c8576100e8565b806340c10f19146101e257806370a08231146101fe5780637ecebe001461022e576100e8565b806323b872dd116100c657806323b872dd1461015857806330adf81f14610188578063313ce567146101a65780633644e515146101c4576100e8565b806306fdde03146100ec578063095ea7b31461010a57806318160ddd1461013a575b5f80fd5b6100f46102f8565b6040516101019190610cc0565b60405180910390f35b610124600480360381019061011f9190610d71565b610331565b6040516101319190610dc9565b60405180910390f35b610142610347565b60405161014f9190610df1565b60405180910390f35b610172600480360381019061016d9190610e0a565b61034c565b60405161017f9190610dc9565b60405180910390f35b61019061050a565b60405161019d9190610e72565b60405180910390f35b6101ae610530565b6040516101bb9190610ea6565b60405180910390f35b6101cc610535565b6040516101d99190610e72565b60405180910390f35b6101fc60048036038101906101f79190610d71565b61053b565b005b61021860048036038101906102139190610ebf565b610549565b6040516102259190610df1565b60405180910390f35b61024860048036038101906102439190610ebf565b61055e565b6040516102559190610df1565b60405180910390f35b610266610573565b6040516102739190610cc0565b60405180910390f35b61029660048036038101906102919190610d71565b6105ac565b6040516102a39190610dc9565b60405180910390f35b6102c660048036038101906102c19190610f3e565b6105c2565b005b6102e260048036038101906102dd9190610fdb565b6107e0565b6040516102ef9190610df1565b60405180910390f35b6040518060400160405280600a81526020017f556e69737761702056320000000000000000000000000000000000000000000081525081565b5f61033d338484610800565b6001905092915050565b5f5481565b5f7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff60025f8673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f2054146104f4576104778260025f8773ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f20546108e790919063ffffffff16565b60025f8673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f20819055505b6104ff84848461093f565b600190509392505050565b7f6e71edae12b1b97f4d1f60370fef10105fa2faae0126114a169c64845d6126c95f1b81565b601281565b60035481565b6105458282610acb565b5050565b6001602052805f5260405f205f915090505481565b6004602052805f5260405f205f915090505481565b6040518060400160405280600681526020017f554e492d5632000000000000000000000000000000000000000000000000000081525081565b5f6105b833848461093f565b6001905092915050565b42841015610605576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016105fc90611063565b60405180910390fd5b5f6003547f6e71edae12b1b97f4d1f60370fef10105fa2faae0126114a169c64845d6126c95f1b89898960045f8e73ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f81548092919061067c906110ae565b919050558a60405160200161069696959493929190611104565b604051602081830303815290604052805190602001206040516020016106bd9291906111d7565b6040516020818303038152906040528051906020012090505f6001828686866040515f81526020016040526040516106f8949392919061120d565b6020604051602081039080840390855afa158015610718573d5f803e3d5ffd5b5050506020604051035190505f73ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff161415801561078b57508873ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff16145b6107ca576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016107c19061129a565b60405180910390fd5b6107d5898989610800565b505050505050505050565b6002602052815f5260405f20602052805f5260405f205f91509150505481565b8060025f8573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f8473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f20819055508173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff167f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925836040516108da9190610df1565b60405180910390a3505050565b5f8282846108f591906112b8565b9150811115610939576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161093090611335565b60405180910390fd5b92915050565b61098f8160015f8673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f20546108e790919063ffffffff16565b60015f8573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f2081905550610a208160015f8573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f2054610bde90919063ffffffff16565b60015f8473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f20819055508173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef83604051610abe9190610df1565b60405180910390a3505050565b610adf815f54610bde90919063ffffffff16565b5f81905550610b348160015f8573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f2054610bde90919063ffffffff16565b60015f8473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f20819055508173ffffffffffffffffffffffffffffffffffffffff165f73ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef83604051610bd29190610df1565b60405180910390a35050565b5f828284610bec9190611353565b9150811015610c30576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610c27906113d0565b60405180910390fd5b92915050565b5f81519050919050565b5f82825260208201905092915050565b5f5b83811015610c6d578082015181840152602081019050610c52565b5f8484015250505050565b5f601f19601f8301169050919050565b5f610c9282610c36565b610c9c8185610c40565b9350610cac818560208601610c50565b610cb581610c78565b840191505092915050565b5f6020820190508181035f830152610cd88184610c88565b905092915050565b5f80fd5b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f610d0d82610ce4565b9050919050565b610d1d81610d03565b8114610d27575f80fd5b50565b5f81359050610d3881610d14565b92915050565b5f819050919050565b610d5081610d3e565b8114610d5a575f80fd5b50565b5f81359050610d6b81610d47565b92915050565b5f8060408385031215610d8757610d86610ce0565b5b5f610d9485828601610d2a565b9250506020610da585828601610d5d565b9150509250929050565b5f8115159050919050565b610dc381610daf565b82525050565b5f602082019050610ddc5f830184610dba565b92915050565b610deb81610d3e565b82525050565b5f602082019050610e045f830184610de2565b92915050565b5f805f60608486031215610e2157610e20610ce0565b5b5f610e2e86828701610d2a565b9350506020610e3f86828701610d2a565b9250506040610e5086828701610d5d565b9150509250925092565b5f819050919050565b610e6c81610e5a565b82525050565b5f602082019050610e855f830184610e63565b92915050565b5f60ff82169050919050565b610ea081610e8b565b82525050565b5f602082019050610eb95f830184610e97565b92915050565b5f60208284031215610ed457610ed3610ce0565b5b5f610ee184828501610d2a565b91505092915050565b610ef381610e8b565b8114610efd575f80fd5b50565b5f81359050610f0e81610eea565b92915050565b610f1d81610e5a565b8114610f27575f80fd5b50565b5f81359050610f3881610f14565b92915050565b5f805f805f805f60e0888a031215610f5957610f58610ce0565b5b5f610f668a828b01610d2a565b9750506020610f778a828b01610d2a565b9650506040610f888a828b01610d5d565b9550506060610f998a828b01610d5d565b9450506080610faa8a828b01610f00565b93505060a0610fbb8a828b01610f2a565b92505060c0610fcc8a828b01610f2a565b91505092959891949750929550565b5f8060408385031215610ff157610ff0610ce0565b5b5f610ffe85828601610d2a565b925050602061100f85828601610d2a565b9150509250929050565b7f556e697377617056323a204558504952454400000000000000000000000000005f82015250565b5f61104d601283610c40565b915061105882611019565b602082019050919050565b5f6020820190508181035f83015261107a81611041565b9050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f6110b882610d3e565b91507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82036110ea576110e9611081565b5b600182019050919050565b6110fe81610d03565b82525050565b5f60c0820190506111175f830189610e63565b61112460208301886110f5565b61113160408301876110f5565b61113e6060830186610de2565b61114b6080830185610de2565b61115860a0830184610de2565b979650505050505050565b5f81905092915050565b7f19010000000000000000000000000000000000000000000000000000000000005f82015250565b5f6111a1600283611163565b91506111ac8261116d565b600282019050919050565b5f819050919050565b6111d16111cc82610e5a565b6111b7565b82525050565b5f6111e182611195565b91506111ed82856111c0565b6020820191506111fd82846111c0565b6020820191508190509392505050565b5f6080820190506112205f830187610e63565b61122d6020830186610e97565b61123a6040830185610e63565b6112476060830184610e63565b95945050505050565b7f556e697377617056323a20494e56414c49445f5349474e4154555245000000005f82015250565b5f611284601c83610c40565b915061128f82611250565b602082019050919050565b5f6020820190508181035f8301526112b181611278565b9050919050565b5f6112c282610d3e565b91506112cd83610d3e565b92508282039050818111156112e5576112e4611081565b5b92915050565b7f64732d6d6174682d7375622d756e646572666c6f7700000000000000000000005f82015250565b5f61131f601583610c40565b915061132a826112eb565b602082019050919050565b5f6020820190508181035f83015261134c81611313565b9050919050565b5f61135d82610d3e565b915061136883610d3e565b92508282019050808211156113805761137f611081565b5b92915050565b7f64732d6d6174682d6164642d6f766572666c6f770000000000000000000000005f82015250565b5f6113ba601483610c40565b91506113c582611386565b602082019050919050565b5f6020820190508181035f8301526113e7816113ae565b905091905056fea26469706673582212209c8c7a573272d5fe5068093229b0a6c767f366b50310c6857bff3fee3d262f8864736f6c63430008140033"

    @overload
    @classmethod
    def deploy(cls, _totalSupply: uint256, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/woke_tests/mocks/ERC20.sol#6)

        Args:
            _totalSupply: uint256
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _totalSupply: uint256, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> ERC20:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/woke_tests/mocks/ERC20.sol#6)

        Args:
            _totalSupply: uint256
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _totalSupply: uint256, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/woke_tests/mocks/ERC20.sol#6)

        Args:
            _totalSupply: uint256
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _totalSupply: uint256, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/woke_tests/mocks/ERC20.sol#6)

        Args:
            _totalSupply: uint256
        """
        ...

    @overload
    @classmethod
    def deploy(cls, _totalSupply: uint256, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[ERC20]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/woke_tests/mocks/ERC20.sol#6)

        Args:
            _totalSupply: uint256
        """
        ...

    @classmethod
    def deploy(cls, _totalSupply: uint256, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, ERC20, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[ERC20]]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/woke_tests/mocks/ERC20.sol#6)

        Args:
            _totalSupply: uint256
        """
        return cls._deploy(request_type, [_totalSupply], return_tx, ERC20, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @overload
    def mint(self, to_: Union[Account, Address], amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/woke_tests/mocks/ERC20.sol#9)

        Args:
            to_: address
            amount: uint256
        """
        ...

    @overload
    def mint(self, to_: Union[Account, Address], amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/woke_tests/mocks/ERC20.sol#9)

        Args:
            to_: address
            amount: uint256
        """
        ...

    @overload
    def mint(self, to_: Union[Account, Address], amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/woke_tests/mocks/ERC20.sol#9)

        Args:
            to_: address
            amount: uint256
        """
        ...

    @overload
    def mint(self, to_: Union[Account, Address], amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/woke_tests/mocks/ERC20.sol#9)

        Args:
            to_: address
            amount: uint256
        """
        ...

    def mint(self, to_: Union[Account, Address], amount: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/woke_tests/mocks/ERC20.sol#9)

        Args:
            to_: address
            amount: uint256
        """
        return self._execute(self.chain, request_type, "40c10f19", [to_, amount], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

ERC20.mint.selector = b'@\xc1\x0f\x19'
