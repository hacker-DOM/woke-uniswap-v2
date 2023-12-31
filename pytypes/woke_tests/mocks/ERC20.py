
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
    _creation_code = "608060405234801561000f575f80fd5b50604051610be6380380610be683398101604081905261002e91610202565b604080518082018252600a8152692ab734b9bbb0b8102b1960b11b6020918201528151808301835260018152603160f81b9082015281517f8b73c3c69bb8fe3d512ecc4cf759cc79239f7b179b0ffacaa9a75d522b39400f818301527fbfcc8ef98ffbf7b6c3fec7bf5185b566b9863e35a9d83acd49ad6824b5969738818401527fc89efdaa54c0f20c7adf612882df0950f5a951637e0307cdcb4c672f298b8bc660608201524660808201523060a0808301919091528351808303909101815260c09091019092528151910120600355610109338261010f565b50610238565b5f5461011b908261019b565b5f9081556001600160a01b03831681526001602052604090205461013f908261019b565b6001600160a01b0383165f818152600160205260408082209390935591519091907fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef9061018f9085815260200190565b60405180910390a35050565b5f826101a78382610219565b91508110156101fc5760405162461bcd60e51b815260206004820152601460248201527f64732d6d6174682d6164642d6f766572666c6f77000000000000000000000000604482015260640160405180910390fd5b92915050565b5f60208284031215610212575f80fd5b5051919050565b808201808211156101fc57634e487b7160e01b5f52601160045260245ffd5b6109a1806102455f395ff3fe608060405234801561000f575f80fd5b50600436106100e5575f3560e01c806340c10f191161008857806395d89b411161006357806395d89b4114610211578063a9059cbb14610236578063d505accf14610249578063dd62ed3e1461025c575f80fd5b806340c10f19146101be57806370a08231146101d35780637ecebe00146101f2575f80fd5b806323b872dd116100c357806323b872dd1461016157806330adf81f14610174578063313ce5671461019b5780633644e515146101b5575f80fd5b806306fdde03146100e9578063095ea7b31461012857806318160ddd1461014b575b5f80fd5b6101126040518060400160405280600a8152602001692ab734b9bbb0b8102b1960b11b81525081565b60405161011f9190610794565b60405180910390f35b61013b6101363660046107fa565b610286565b604051901515815260200161011f565b6101535f5481565b60405190815260200161011f565b61013b61016f366004610822565b61029c565b6101537f6e71edae12b1b97f4d1f60370fef10105fa2faae0126114a169c64845d6126c981565b6101a3601281565b60405160ff909116815260200161011f565b61015360035481565b6101d16101cc3660046107fa565b61032c565b005b6101536101e136600461085b565b60016020525f908152604090205481565b61015361020036600461085b565b60046020525f908152604090205481565b610112604051806040016040528060068152602001652aa72496ab1960d11b81525081565b61013b6102443660046107fa565b61033a565b6101d161025736600461087b565b610346565b61015361026a3660046108e8565b600260209081525f928352604080842090915290825290205481565b5f61029233848461055b565b5060015b92915050565b6001600160a01b0383165f9081526002602090815260408083203384529091528120545f1914610317576001600160a01b0384165f9081526002602090815260408083203384529091529020546102f390836105bc565b6001600160a01b0385165f9081526002602090815260408083203384529091529020555b610322848484610611565b5060019392505050565b61033682826106b4565b5050565b5f610292338484610611565b428410156103905760405162461bcd60e51b8152602060048201526012602482015271155b9a5cddd85c158c8e881156141254915160721b60448201526064015b60405180910390fd5b6003546001600160a01b0388165f90815260046020526040812080549192917f6e71edae12b1b97f4d1f60370fef10105fa2faae0126114a169c64845d6126c9918b918b918b9190876103e28361092d565b909155506040805160208101969096526001600160a01b0394851690860152929091166060840152608083015260a082015260c0810187905260e0016040516020818303038152906040528051906020012060405160200161045b92919061190160f01b81526002810192909252602282015260420190565b60408051601f1981840301815282825280516020918201205f80855291840180845281905260ff88169284019290925260608301869052608083018590529092509060019060a0016020604051602081039080840390855afa1580156104c3573d5f803e3d5ffd5b5050604051601f1901519150506001600160a01b038116158015906104f95750886001600160a01b0316816001600160a01b0316145b6105455760405162461bcd60e51b815260206004820152601c60248201527f556e697377617056323a20494e56414c49445f5349474e4154555245000000006044820152606401610387565b61055089898961055b565b505050505050505050565b6001600160a01b038381165f8181526002602090815260408083209487168084529482529182902085905590518481527f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b92591015b60405180910390a3505050565b5f826105c88382610945565b91508111156102965760405162461bcd60e51b815260206004820152601560248201527464732d6d6174682d7375622d756e646572666c6f7760581b6044820152606401610387565b6001600160a01b0383165f9081526001602052604090205461063390826105bc565b6001600160a01b038085165f9081526001602052604080822093909355908416815220546106619082610740565b6001600160a01b038084165f8181526001602052604090819020939093559151908516907fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef906105af9085815260200190565b5f546106c09082610740565b5f9081556001600160a01b0383168152600160205260409020546106e49082610740565b6001600160a01b0383165f818152600160205260408082209390935591519091907fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef906107349085815260200190565b60405180910390a35050565b5f8261074c8382610958565b91508110156102965760405162461bcd60e51b815260206004820152601460248201527364732d6d6174682d6164642d6f766572666c6f7760601b6044820152606401610387565b5f6020808352835180828501525f5b818110156107bf578581018301518582016040015282016107a3565b505f604082860101526040601f19601f8301168501019250505092915050565b80356001600160a01b03811681146107f5575f80fd5b919050565b5f806040838503121561080b575f80fd5b610814836107df565b946020939093013593505050565b5f805f60608486031215610834575f80fd5b61083d846107df565b925061084b602085016107df565b9150604084013590509250925092565b5f6020828403121561086b575f80fd5b610874826107df565b9392505050565b5f805f805f805f60e0888a031215610891575f80fd5b61089a886107df565b96506108a8602089016107df565b95506040880135945060608801359350608088013560ff811681146108cb575f80fd5b9699959850939692959460a0840135945060c09093013592915050565b5f80604083850312156108f9575f80fd5b610902836107df565b9150610910602084016107df565b90509250929050565b634e487b7160e01b5f52601160045260245ffd5b5f6001820161093e5761093e610919565b5060010190565b8181038181111561029657610296610919565b808201808211156102965761029661091956fea2646970667358221220081dde26e111d8521cdb8559a4b1ef8e0e91c4060a9541045c493f9775ef014e64736f6c63430008140033"

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
