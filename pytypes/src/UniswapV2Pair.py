
from __future__ import annotations

import dataclasses
from typing import List, Dict, Optional, overload, Union, Callable, Tuple
from typing_extensions import Literal

from woke.development.core import Contract, Library, Address, Account, Chain, RequestType
from woke.development.primitive_types import *
from woke.development.transactions import TransactionAbc, TransactionRevertedError

from enum import IntEnum

from pytypes.src.UniswapV2ERC20 import UniswapV2ERC20



class UniswapV2Pair(UniswapV2ERC20):
    """
    [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#11)
    """
    _abi = {'constructor': {'inputs': [], 'stateMutability': 'nonpayable', 'type': 'constructor'}, b'6D\xe5\x15': {'inputs': [], 'name': 'DOMAIN_SEPARATOR', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'\xba\x9azV': {'inputs': [], 'name': 'MINIMUM_LIQUIDITY', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'0\xad\xf8\x1f': {'inputs': [], 'name': 'PERMIT_TYPEHASH', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, b'\xddb\xed>': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}, {'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'allowance', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\t^\xa7\xb3': {'inputs': [{'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'approve', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'p\xa0\x821': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\x89\xaf\xcbD': {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}], 'name': 'burn', 'outputs': [{'internalType': 'uint256', 'name': 'amount0', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount1', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'1<\xe5g': {'inputs': [], 'name': 'decimals', 'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}], 'stateMutability': 'view', 'type': 'function'}, b'\xc4Z\x01U': {'inputs': [], 'name': 'factory', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\t\x02\xf1\xac': {'inputs': [], 'name': 'getReserves', 'outputs': [{'internalType': 'uint112', 'name': '_reserve0', 'type': 'uint112'}, {'internalType': 'uint112', 'name': '_reserve1', 'type': 'uint112'}, {'internalType': 'uint32', 'name': '_blockTimestampLast', 'type': 'uint32'}], 'stateMutability': 'view', 'type': 'function'}, b'H\\\xc9U': {'inputs': [{'internalType': 'address', 'name': '_token0', 'type': 'address'}, {'internalType': 'address', 'name': '_token1', 'type': 'address'}], 'name': 'initialize', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'td\xfc=': {'inputs': [], 'name': 'kLast', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'jbxB': {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}], 'name': 'mint', 'outputs': [{'internalType': 'uint256', 'name': 'liquidity', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x06\xfd\xde\x03': {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'~\xce\xbe\x00': {'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'name': 'nonces', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xd5\x05\xac\xcf': {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}, {'internalType': 'address', 'name': 'spender', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'deadline', 'type': 'uint256'}, {'internalType': 'uint8', 'name': 'v', 'type': 'uint8'}, {'internalType': 'bytes32', 'name': 'r', 'type': 'bytes32'}, {'internalType': 'bytes32', 'name': 's', 'type': 'bytes32'}], 'name': 'permit', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'Y\t\xc0\xd5': {'inputs': [], 'name': 'price0CumulativeLast', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'Z=T\x93': {'inputs': [], 'name': 'price1CumulativeLast', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xbc%\xcfw': {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}], 'name': 'skim', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x02,\r\x9f': {'inputs': [{'internalType': 'uint256', 'name': 'amount0Out', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amount1Out', 'type': 'uint256'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'bytes', 'name': 'data', 'type': 'bytes'}], 'name': 'swap', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x95\xd8\x9bA': {'inputs': [], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}], 'stateMutability': 'view', 'type': 'function'}, b'\xff\xf6\xca\xe9': {'inputs': [], 'name': 'sync', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\r\xfe\x16\x81': {'inputs': [], 'name': 'token0', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\xd2\x12 \xa7': {'inputs': [], 'name': 'token1', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, b'\x18\x16\r\xdd': {'inputs': [], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'\xa9\x05\x9c\xbb': {'inputs': [{'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'transfer', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}, b'#\xb8r\xdd': {'inputs': [{'internalType': 'address', 'name': 'from', 'type': 'address'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'value', 'type': 'uint256'}], 'name': 'transferFrom', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _creation_code = "60806040526001600c55348015610014575f80fd5b50604080518082018252600a8152692ab734b9bbb0b8102b1960b11b6020918201528151808301835260018152603160f81b9082015281517f8b73c3c69bb8fe3d512ecc4cf759cc79239f7b179b0ffacaa9a75d522b39400f818301527fbfcc8ef98ffbf7b6c3fec7bf5185b566b9863e35a9d83acd49ad6824b5969738818401527fc89efdaa54c0f20c7adf612882df0950f5a951637e0307cdcb4c672f298b8bc660608201524660808201523060a0808301919091528351808303909101815260c09091019092528151910120600355600580546001600160a01b0319163317905561255f806101055f395ff3fe608060405234801561000f575f80fd5b50600436106101a1575f3560e01c80636a627842116100f3578063ba9a7a5611610093578063d21220a71161006e578063d21220a7146103fc578063d505accf1461040f578063dd62ed3e14610422578063fff6cae91461044c575f80fd5b8063ba9a7a56146103cd578063bc25cf77146103d6578063c45a0155146103e9575f80fd5b80637ecebe00116100ce5780637ecebe001461034e57806389afcb441461036d57806395d89b4114610395578063a9059cbb146103ba575f80fd5b80636a6278421461031357806370a08231146103265780637464fc3d14610345575f80fd5b806323b872dd1161015e5780633644e515116101395780633644e515146102e5578063485cc955146102ee5780635909c0d5146103015780635a3d54931461030a575f80fd5b806323b872dd1461029157806330adf81f146102a4578063313ce567146102cb575f80fd5b8063022c0d9f146101a557806306fdde03146101ba5780630902f1ac146101f9578063095ea7b31461022d5780630dfe16811461025057806318160ddd1461027b575b5f80fd5b6101b86101b3366004612081565b610454565b005b6101e36040518060400160405280600a8152602001692ab734b9bbb0b8102b1960b11b81525081565b6040516101f0919061215c565b60405180910390f35b610201610945565b604080516001600160701b03948516815293909216602084015263ffffffff16908201526060016101f0565b61024061023b36600461216e565b61096f565b60405190151581526020016101f0565b600654610263906001600160a01b031681565b6040516001600160a01b0390911681526020016101f0565b6102835f5481565b6040519081526020016101f0565b61024061029f366004612198565b610985565b6102837f6e71edae12b1b97f4d1f60370fef10105fa2faae0126114a169c64845d6126c981565b6102d3601281565b60405160ff90911681526020016101f0565b61028360035481565b6101b86102fc3660046121d6565b610a15565b61028360095481565b610283600a5481565b61028361032136600461220d565b610a94565b61028361033436600461220d565b60016020525f908152604090205481565b610283600b5481565b61028361035c36600461220d565b60046020525f908152604090205481565b61038061037b36600461220d565b610f4e565b604080519283526020830191909152016101f0565b6101e3604051806040016040528060068152602001652aa72496ab1960d11b81525081565b6102406103c836600461216e565b6112a4565b6102836103e881565b6101b86103e436600461220d565b6112b0565b600554610263906001600160a01b031681565b600754610263906001600160a01b031681565b6101b861041d366004612228565b6113c1565b6102836104303660046121d6565b600260209081525f928352604080842090915290825290205481565b6101b86115d1565b600c5460011461047f5760405162461bcd60e51b815260040161047690612299565b60405180910390fd5b5f600c558415158061049057505f84115b6104ea5760405162461bcd60e51b815260206004820152602560248201527f556e697377617056323a20494e53554646494349454e545f4f55545055545f416044820152641353d5539560da1b6064820152608401610476565b5f806104f4610945565b5091509150816001600160701b0316871080156105195750806001600160701b031686105b61056f5760405162461bcd60e51b815260206004820152602160248201527f556e697377617056323a20494e53554646494349454e545f4c495155494449546044820152605960f81b6064820152608401610476565b6006546007545f9182916001600160a01b039182169190811690891682148015906105ac5750806001600160a01b0316896001600160a01b031614155b6105f05760405162461bcd60e51b8152602060048201526015602482015274556e697377617056323a20494e56414c49445f544f60581b6044820152606401610476565b8a1561060157610601828a8d6116f0565b891561061257610612818a8c6116f0565b861561067a576040516304347a1760e21b81526001600160a01b038a16906310d1e85c9061064c9033908f908f908e908e906004016122c4565b5f604051808303815f87803b158015610663575f80fd5b505af1158015610675573d5f803e3d5ffd5b505050505b6040516370a0823160e01b81523060048201526001600160a01b038316906370a0823190602401602060405180830381865afa1580156106bc573d5f803e3d5ffd5b505050506040513d601f19601f820116820180604052508101906106e0919061230f565b6040516370a0823160e01b81523060048201529094506001600160a01b038216906370a0823190602401602060405180830381865afa158015610725573d5f803e3d5ffd5b505050506040513d601f19601f82011682018060405250810190610749919061230f565b925050505f89856001600160701b0316610763919061233a565b831161076f575f61078c565b6107828a6001600160701b03871661233a565b61078c908461233a565b90505f6107a28a6001600160701b03871661233a565b83116107ae575f6107cb565b6107c18a6001600160701b03871661233a565b6107cb908461233a565b90505f8211806107da57505f81115b6108325760405162461bcd60e51b8152602060048201526024808201527f556e697377617056323a20494e53554646494349454e545f494e5055545f414d60448201526313d5539560e21b6064820152608401610476565b5f610853610841846003611836565b61084d876103e8611836565b9061189c565b90505f610864610841846003611836565b9050610889620f42406108836001600160701b038b8116908b16611836565b90611836565b6108938383611836565b10156108d05760405162461bcd60e51b815260206004820152600c60248201526b556e697377617056323a204b60a01b6044820152606401610476565b50506108de848488886118f1565b60408051838152602081018390529081018c9052606081018b90526001600160a01b038a169033907fd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d8229060800160405180910390a350506001600c55505050505050505050565b6008546001600160701b0380821692600160701b830490911691600160e01b900463ffffffff1690565b5f61097b338484611ad8565b5060015b92915050565b6001600160a01b0383165f9081526002602090815260408083203384529091528120545f1914610a00576001600160a01b0384165f9081526002602090815260408083203384529091529020546109dc908361189c565b6001600160a01b0385165f9081526002602090815260408083203384529091529020555b610a0b848484611b39565b5060019392505050565b6005546001600160a01b03163314610a665760405162461bcd60e51b81526020600482015260146024820152732ab734b9bbb0b82b191d102327a92124a22222a760611b6044820152606401610476565b600680546001600160a01b039384166001600160a01b03199182161790915560078054929093169116179055565b5f600c54600114610ab75760405162461bcd60e51b815260040161047690612299565b5f600c81905580610ac6610945565b506006546040516370a0823160e01b81523060048201529294509092505f916001600160a01b03909116906370a0823190602401602060405180830381865afa158015610b15573d5f803e3d5ffd5b505050506040513d601f19601f82011682018060405250810190610b39919061230f565b6007546040516370a0823160e01b81523060048201529192505f916001600160a01b03909116906370a0823190602401602060405180830381865afa158015610b84573d5f803e3d5ffd5b505050506040513d601f19601f82011682018060405250810190610ba8919061230f565b90505f610bbe836001600160701b03871661189c565b90505f610bd4836001600160701b03871661189c565b90505f610be18787611bdc565b90505f80549050610c32604051806040016040528060078152602001660616d6f756e74360cc1b8152508560405180604001604052806007815260200166616d6f756e743160c81b81525086611d0e565b610c7e60405180604001604052806008815260200167062616c616e6365360c41b815250876040518060400160405280600881526020016762616c616e63653160c01b81525088611d0e565b805f03610cdb57610c9d6103e861084d610c988787611836565b611d5d565b9850610cca604051806040016040528060098152602001686c697175696469747960b81b8152508a611dcb565b610cd65f6103e8611e14565b610d4c565b610d1f6001600160701b038916610cf28684611836565b610cfc9190612361565b6001600160701b038916610d108685611836565b610d1a9190612361565b611ea0565b9850610d4c604051806040016040528060098152602001686c697175696469747960b81b8152508a611dcb565b5f8911610dac5760405162461bcd60e51b815260206004820152602860248201527f556e697377617056323a20494e53554646494349454e545f4c495155494449546044820152671657d3525395115160c21b6064820152608401610476565b610df360405180604001604052806002815260200161746f60f01b8152508b604051806040016040528060098152602001686c697175696469747960b81b8152508c611eb7565b610dfd8a8a611e14565b610e4960405180604001604052806008815260200167062616c616e6365360c41b815250876040518060400160405280600881526020016762616c616e63653160c01b81525088611d0e565b604080518082018252600880825267072657365727665360c41b6020808401919091528154845180860190955291845267726573657276653160c01b90840152610ea6926001600160701b0380831692600160701b900416611d0e565b610eb286868a8a6118f1565b8115610edc57600854610ed8906001600160701b0380821691600160701b900416611836565b600b555b610f0060405180604001604052806003815260200162115b9960ea1b815250611f00565b604080518581526020810185905233917f4c209b5fc8ad50758f13e2e1088ba56a560dff690a1c6fef26394f4c03821c4f910160405180910390a250506001600c5550949695505050505050565b5f80600c54600114610f725760405162461bcd60e51b815260040161047690612299565b5f600c81905580610f81610945565b506006546007546040516370a0823160e01b81523060048201529395509193506001600160a01b03908116929116905f9083906370a0823190602401602060405180830381865afa158015610fd8573d5f803e3d5ffd5b505050506040513d601f19601f82011682018060405250810190610ffc919061230f565b6040516370a0823160e01b81523060048201529091505f906001600160a01b038416906370a0823190602401602060405180830381865afa158015611043573d5f803e3d5ffd5b505050506040513d601f19601f82011682018060405250810190611067919061230f565b305f908152600160205260408120549192506110838888611bdc565b5f54909150806110938487611836565b61109d9190612361565b9a50806110aa8486611836565b6110b49190612361565b99505f8b1180156110c457505f8a115b6111215760405162461bcd60e51b815260206004820152602860248201527f556e697377617056323a20494e53554646494349454e545f4c495155494449546044820152671657d0955493915160c21b6064820152608401610476565b61112b3084611f46565b611136878d8d6116f0565b611141868d8c6116f0565b6040516370a0823160e01b81523060048201526001600160a01b038816906370a0823190602401602060405180830381865afa158015611183573d5f803e3d5ffd5b505050506040513d601f19601f820116820180604052508101906111a7919061230f565b6040516370a0823160e01b81523060048201529095506001600160a01b038716906370a0823190602401602060405180830381865afa1580156111ec573d5f803e3d5ffd5b505050506040513d601f19601f82011682018060405250810190611210919061230f565b935061121e85858b8b6118f1565b811561124857600854611244906001600160701b0380821691600160701b900416611836565b600b555b604080518c8152602081018c90526001600160a01b038e169133917fdccd412f0b1252819cb1fd330b93224ca42612892bb3f4f789976e6d81936496910160405180910390a35050505050505050506001600c81905550915091565b5f61097b338484611b39565b600c546001146112d25760405162461bcd60e51b815260040161047690612299565b5f600c556006546007546008546040516370a0823160e01b81523060048201526001600160a01b03938416939092169161136a9184918691611365916001600160701b039091169084906370a08231906024015b602060405180830381865afa158015611341573d5f803e3d5ffd5b505050506040513d601f19601f8201168201806040525081019061084d919061230f565b6116f0565b6008546040516370a0823160e01b81523060048201526113b7918391869161136591600160701b9091046001600160701b0316906001600160a01b038516906370a0823190602401611326565b50506001600c5550565b428410156114065760405162461bcd60e51b8152602060048201526012602482015271155b9a5cddd85c158c8e881156141254915160721b6044820152606401610476565b6003546001600160a01b0388165f90815260046020526040812080549192917f6e71edae12b1b97f4d1f60370fef10105fa2faae0126114a169c64845d6126c9918b918b918b91908761145883612374565b909155506040805160208101969096526001600160a01b0394851690860152929091166060840152608083015260a082015260c0810187905260e001604051602081830303815290604052805190602001206040516020016114d192919061190160f01b81526002810192909252602282015260420190565b60408051601f1981840301815282825280516020918201205f80855291840180845281905260ff88169284019290925260608301869052608083018590529092509060019060a0016020604051602081039080840390855afa158015611539573d5f803e3d5ffd5b5050604051601f1901519150506001600160a01b0381161580159061156f5750886001600160a01b0316816001600160a01b0316145b6115bb5760405162461bcd60e51b815260206004820152601c60248201527f556e697377617056323a20494e56414c49445f5349474e4154555245000000006044820152606401610476565b6115c6898989611ad8565b505050505050505050565b600c546001146115f35760405162461bcd60e51b815260040161047690612299565b5f600c556006546040516370a0823160e01b81523060048201526116e9916001600160a01b0316906370a0823190602401602060405180830381865afa15801561163f573d5f803e3d5ffd5b505050506040513d601f19601f82011682018060405250810190611663919061230f565b6007546040516370a0823160e01b81523060048201526001600160a01b03909116906370a0823190602401602060405180830381865afa1580156116a9573d5f803e3d5ffd5b505050506040513d601f19601f820116820180604052508101906116cd919061230f565b6008546001600160701b0380821691600160701b9004166118f1565b6001600c55565b604080518082018252601981527f7472616e7366657228616464726573732c75696e74323536290000000000000060209182015281516001600160a01b0385811660248301526044808301869052845180840390910181526064909201845291810180516001600160e01b031663a9059cbb60e01b17905291515f92839287169161177b919061238c565b5f604051808303815f865af19150503d805f81146117b4576040519150601f19603f3d011682016040523d82523d5f602084013e6117b9565b606091505b50915091508180156117e35750805115806117e35750808060200190518101906117e391906123a7565b61182f5760405162461bcd60e51b815260206004820152601a60248201527f556e697377617056323a205452414e534645525f4641494c45440000000000006044820152606401610476565b5050505050565b5f8115806118595750828261184b81836123c6565b92506118579083612361565b145b61097f5760405162461bcd60e51b815260206004820152601460248201527364732d6d6174682d6d756c2d6f766572666c6f7760601b6044820152606401610476565b5f826118a8838261233a565b915081111561097f5760405162461bcd60e51b815260206004820152601560248201527464732d6d6174682d7375622d756e646572666c6f7760581b6044820152606401610476565b6001600160701b03841180159061190f57506001600160701b038311155b6119515760405162461bcd60e51b8152602060048201526013602482015272556e697377617056323a204f564552464c4f5760681b6044820152606401610476565b5f611961640100000000426123dd565b6008549091505f9061198090600160e01b900463ffffffff16836123f0565b90505f8163ffffffff1611801561199f57506001600160701b03841615155b80156119b357506001600160701b03831615155b15611a40578063ffffffff166119db856119cc86611fcd565b6001600160e01b031690611fe5565b6001600160e01b03166119ee91906123c6565b60095f8282546119fe9190612414565b909155505063ffffffff8116611a17846119cc87611fcd565b6001600160e01b0316611a2a91906123c6565b600a5f828254611a3a9190612414565b90915550505b6008805463ffffffff8416600160e01b026001600160e01b036001600160701b03898116600160701b9081026001600160e01b03199095168c83161794909417918216831794859055604080519382169282169290921783529290930490911660208201527f1c411e9a96e071241c2f21f7726b17ae89e3cab4c78be50e062b03a9fffbbad1910160405180910390a1505050505050565b6001600160a01b038381165f8181526002602090815260408083209487168084529482529182902085905590518481527f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b92591015b60405180910390a3505050565b6001600160a01b0383165f90815260016020526040902054611b5b908261189c565b6001600160a01b038085165f908152600160205260408082209390935590841681522054611b899082611ff9565b6001600160a01b038084165f8181526001602052604090819020939093559151908516907fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef90611b2c9085815260200190565b5f8060055f9054906101000a90046001600160a01b03166001600160a01b031663017e7e586040518163ffffffff1660e01b8152600401602060405180830381865afa158015611c2e573d5f803e3d5ffd5b505050506040513d601f19601f82011682018060405250810190611c529190612427565b600b546001600160a01b038216158015945091925090611cfb578015611cf6575f611c8c610c986001600160701b03888116908816611836565b90505f611c9883611d5d565b905080821115611cf3575f611cb8611cb0848461189c565b5f5490611836565b90505f611cd083611cca866005611836565b90611ff9565b90505f611cdd8284612361565b90508015611cef57611cef8782611e14565b5050505b50505b611d06565b8015611d06575f600b555b505092915050565b611d5784848484604051602401611d289493929190612442565b60408051601f198184030181529190526020810180516001600160e01b031663c67ea9d160e01b17905261204d565b50505050565b5f6003821115611dbc5750805f611d75600283612361565b611d80906001612414565b90505b81811015611db657905080600281611d9b8186612361565b611da59190612414565b611daf9190612361565b9050611d83565b50919050565b8115611dc6575060015b919050565b611e108282604051602401611de192919061247e565b60408051601f198184030181529190526020810180516001600160e01b0316632d839cb360e21b17905261204d565b5050565b5f54611e209082611ff9565b5f9081556001600160a01b038316815260016020526040902054611e449082611ff9565b6001600160a01b0383165f818152600160205260408082209390935591519091907fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef90611e949085815260200190565b60405180910390a35050565b5f818310611eae5781611eb0565b825b9392505050565b611d5784848484604051602401611ed1949392919061249f565b60408051601f198184030181529190526020810180516001600160e01b03166348e8889760e11b17905261204d565b611f4381604051602401611f14919061215c565b60408051601f198184030181529190526020810180516001600160e01b031663104c13eb60e21b17905261204d565b50565b6001600160a01b0382165f90815260016020526040902054611f68908261189c565b6001600160a01b0383165f9081526001602052604081209190915554611f8e908261189c565b5f9081556040518281526001600160a01b038416907fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef90602001611e94565b5f61097f600160701b6001600160701b0384166124d2565b5f611eb06001600160701b03831684612504565b5f826120058382612414565b915081101561097f5760405162461bcd60e51b815260206004820152601460248201527364732d6d6174682d6164642d6f766572666c6f7760601b6044820152606401610476565b80516a636f6e736f6c652e6c6f67602083015f808483855afa5050505050565b6001600160a01b0381168114611f43575f80fd5b5f805f805f60808688031215612095575f80fd5b853594506020860135935060408601356120ae8161206d565b9250606086013567ffffffffffffffff808211156120ca575f80fd5b818801915088601f8301126120dd575f80fd5b8135818111156120eb575f80fd5b8960208285010111156120fc575f80fd5b9699959850939650602001949392505050565b5f5b83811015612129578181015183820152602001612111565b50505f910152565b5f815180845261214881602086016020860161210f565b601f01601f19169290920160200192915050565b602081525f611eb06020830184612131565b5f806040838503121561217f575f80fd5b823561218a8161206d565b946020939093013593505050565b5f805f606084860312156121aa575f80fd5b83356121b58161206d565b925060208401356121c58161206d565b929592945050506040919091013590565b5f80604083850312156121e7575f80fd5b82356121f28161206d565b915060208301356122028161206d565b809150509250929050565b5f6020828403121561221d575f80fd5b8135611eb08161206d565b5f805f805f805f60e0888a03121561223e575f80fd5b87356122498161206d565b965060208801356122598161206d565b95506040880135945060608801359350608088013560ff8116811461227c575f80fd5b9699959850939692959460a0840135945060c09093013592915050565b602080825260119082015270155b9a5cddd85c158c8e881313d0d2d151607a1b604082015260600190565b60018060a01b038616815284602082015283604082015260806060820152816080820152818360a08301375f81830160a090810191909152601f909201601f19160101949350505050565b5f6020828403121561231f575f80fd5b5051919050565b634e487b7160e01b5f52601160045260245ffd5b8181038181111561097f5761097f612326565b634e487b7160e01b5f52601260045260245ffd5b5f8261236f5761236f61234d565b500490565b5f6001820161238557612385612326565b5060010190565b5f825161239d81846020870161210f565b9190910192915050565b5f602082840312156123b7575f80fd5b81518015158114611eb0575f80fd5b808202811582820484141761097f5761097f612326565b5f826123eb576123eb61234d565b500690565b63ffffffff82811682821603908082111561240d5761240d612326565b5092915050565b8082018082111561097f5761097f612326565b5f60208284031215612437575f80fd5b8151611eb08161206d565b608081525f6124546080830187612131565b856020840152828103604084015261246c8186612131565b91505082606083015295945050505050565b604081525f6124906040830185612131565b90508260208301529392505050565b608081525f6124b16080830187612131565b6001600160a01b0386166020840152828103604084015261246c8186612131565b6001600160e01b038281168282168181028316929181158285048214176124fb576124fb612326565b50505092915050565b5f6001600160e01b038381168061251d5761251d61234d565b9216919091049291505056fea2646970667358221220cd62a387e5dc49789807b000bb4ca55bfae3869d6053520b4efac3b4d9b68e6e64736f6c63430008140033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["call"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> bytearray:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#61)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> UniswapV2Pair:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#61)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["estimate"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#61)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[False] = False, request_type: Literal["access_list"], chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#61)
        """
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: Literal[True], request_type: Literal["tx"] = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[UniswapV2Pair]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#61)
        """
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, return_tx: bool = False, request_type: RequestType = "tx", chain: Optional[Chain] = None, gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[bytearray, UniswapV2Pair, int, Tuple[Dict[Address, List[int]], int], TransactionAbc[UniswapV2Pair]]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#61)
        """
        return cls._deploy(request_type, [], return_tx, UniswapV2Pair, from_, value, gas_limit, {}, chain, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @classmethod
    def get_creation_code(cls) -> bytes:
        return cls._get_creation_code({})

    @dataclasses.dataclass
    class Mint:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#49)

        Attributes:
            sender (Address): indexed address
            amount0 (uint256): uint256
            amount1 (uint256): uint256
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount0', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount1', 'type': 'uint256'}], 'name': 'Mint', 'type': 'event'}
        original_name = 'Mint'
        selector = b'L \x9b_\xc8\xadPu\x8f\x13\xe2\xe1\x08\x8b\xa5jV\r\xffi\n\x1co\xef&9OL\x03\x82\x1cO'

        sender: Address
        amount0: uint256
        amount1: uint256


    @dataclasses.dataclass
    class Burn:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#50)

        Attributes:
            sender (Address): indexed address
            amount0 (uint256): uint256
            amount1 (uint256): uint256
            to (Address): indexed address
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount0', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount1', 'type': 'uint256'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}], 'name': 'Burn', 'type': 'event'}
        original_name = 'Burn'
        selector = b'\xdc\xcdA/\x0b\x12R\x81\x9c\xb1\xfd3\x0b\x93"L\xa4&\x12\x89+\xb3\xf4\xf7\x89\x97nm\x81\x93d\x96'

        sender: Address
        amount0: uint256
        amount1: uint256
        to: Address


    @dataclasses.dataclass
    class Swap:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#51)

        Attributes:
            sender (Address): indexed address
            amount0In (uint256): uint256
            amount1In (uint256): uint256
            amount0Out (uint256): uint256
            amount1Out (uint256): uint256
            to (Address): indexed address
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': True, 'internalType': 'address', 'name': 'sender', 'type': 'address'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount0In', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount1In', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount0Out', 'type': 'uint256'}, {'indexed': False, 'internalType': 'uint256', 'name': 'amount1Out', 'type': 'uint256'}, {'indexed': True, 'internalType': 'address', 'name': 'to', 'type': 'address'}], 'name': 'Swap', 'type': 'event'}
        original_name = 'Swap'
        selector = b'\xd7\x8a\xd9_\xa4l\x99KeQ\xd0\xda\x85\xfc\'_\xe6\x13\xce7e\x7f\xb8\xd5\xe3\xd10\x84\x01Y\xd8"'

        sender: Address
        amount0In: uint256
        amount1In: uint256
        amount0Out: uint256
        amount1Out: uint256
        to: Address


    @dataclasses.dataclass
    class Sync:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#59)

        Attributes:
            reserve0 (uint112): uint112
            reserve1 (uint112): uint112
        """
        _abi = {'anonymous': False, 'inputs': [{'indexed': False, 'internalType': 'uint112', 'name': 'reserve0', 'type': 'uint112'}, {'indexed': False, 'internalType': 'uint112', 'name': 'reserve1', 'type': 'uint112'}], 'name': 'Sync', 'type': 'event'}
        original_name = 'Sync'
        selector = b'\x1cA\x1e\x9a\x96\xe0q$\x1c/!\xf7rk\x17\xae\x89\xe3\xca\xb4\xc7\x8b\xe5\x0e\x06+\x03\xa9\xff\xfb\xba\xd1'

        reserve0: uint112
        reserve1: uint112


    @overload
    def MINIMUM_LIQUIDITY(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#15)

        Returns:
            uint256
        """
        ...

    @overload
    def MINIMUM_LIQUIDITY(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#15)

        Returns:
            uint256
        """
        ...

    @overload
    def MINIMUM_LIQUIDITY(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#15)

        Returns:
            uint256
        """
        ...

    @overload
    def MINIMUM_LIQUIDITY(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#15)

        Returns:
            uint256
        """
        ...

    def MINIMUM_LIQUIDITY(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#15)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "ba9a7a56", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def factory(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#18)

        Returns:
            address
        """
        ...

    @overload
    def factory(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#18)

        Returns:
            address
        """
        ...

    @overload
    def factory(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#18)

        Returns:
            address
        """
        ...

    @overload
    def factory(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#18)

        Returns:
            address
        """
        ...

    def factory(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#18)

        Returns:
            address
        """
        return self._execute(self.chain, request_type, "c45a0155", [], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def token0(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#19)

        Returns:
            address
        """
        ...

    @overload
    def token0(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#19)

        Returns:
            address
        """
        ...

    @overload
    def token0(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#19)

        Returns:
            address
        """
        ...

    @overload
    def token0(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#19)

        Returns:
            address
        """
        ...

    def token0(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#19)

        Returns:
            address
        """
        return self._execute(self.chain, request_type, "0dfe1681", [], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def token1(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Address:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#20)

        Returns:
            address
        """
        ...

    @overload
    def token1(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#20)

        Returns:
            address
        """
        ...

    @overload
    def token1(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#20)

        Returns:
            address
        """
        ...

    @overload
    def token1(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Address]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#20)

        Returns:
            address
        """
        ...

    def token1(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Address, TransactionAbc[Address], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#20)

        Returns:
            address
        """
        return self._execute(self.chain, request_type, "d21220a7", [], True if request_type == "tx" else False, Address, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def price0CumulativeLast(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#26)

        Returns:
            uint256
        """
        ...

    @overload
    def price0CumulativeLast(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#26)

        Returns:
            uint256
        """
        ...

    @overload
    def price0CumulativeLast(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#26)

        Returns:
            uint256
        """
        ...

    @overload
    def price0CumulativeLast(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#26)

        Returns:
            uint256
        """
        ...

    def price0CumulativeLast(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#26)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "5909c0d5", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def price1CumulativeLast(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#27)

        Returns:
            uint256
        """
        ...

    @overload
    def price1CumulativeLast(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#27)

        Returns:
            uint256
        """
        ...

    @overload
    def price1CumulativeLast(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#27)

        Returns:
            uint256
        """
        ...

    @overload
    def price1CumulativeLast(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#27)

        Returns:
            uint256
        """
        ...

    def price1CumulativeLast(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#27)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "5a3d5493", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def kLast(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#28)

        Returns:
            uint256
        """
        ...

    @overload
    def kLast(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#28)

        Returns:
            uint256
        """
        ...

    @overload
    def kLast(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#28)

        Returns:
            uint256
        """
        ...

    @overload
    def kLast(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#28)

        Returns:
            uint256
        """
        ...

    def kLast(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#28)

        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "7464fc3d", [], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def getReserves(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"] = "call", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[uint112, uint112, uint32]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#38)

        Returns:
            (uint112, uint112, uint32)
        """
        ...

    @overload
    def getReserves(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#38)

        Returns:
            (uint112, uint112, uint32)
        """
        ...

    @overload
    def getReserves(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#38)

        Returns:
            (uint112, uint112, uint32)
        """
        ...

    @overload
    def getReserves(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Tuple[uint112, uint112, uint32]]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#38)

        Returns:
            (uint112, uint112, uint32)
        """
        ...

    def getReserves(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'call', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Tuple[uint112, uint112, uint32], TransactionAbc[Tuple[uint112, uint112, uint32]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#38)

        Returns:
            (uint112, uint112, uint32)
        """
        return self._execute(self.chain, request_type, "0902f1ac", [], True if request_type == "tx" else False, Tuple[uint112, uint112, uint32], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def initialize(self, _token0: Union[Account, Address], _token1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#66)

        Args:
            _token0: address
            _token1: address
        """
        ...

    @overload
    def initialize(self, _token0: Union[Account, Address], _token1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#66)

        Args:
            _token0: address
            _token1: address
        """
        ...

    @overload
    def initialize(self, _token0: Union[Account, Address], _token1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#66)

        Args:
            _token0: address
            _token1: address
        """
        ...

    @overload
    def initialize(self, _token0: Union[Account, Address], _token1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#66)

        Args:
            _token0: address
            _token1: address
        """
        ...

    def initialize(self, _token0: Union[Account, Address], _token1: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#66)

        Args:
            _token0: address
            _token1: address
        """
        return self._execute(self.chain, request_type, "485cc955", [_token0, _token1], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def mint(self, to_: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> uint256:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#110)

        Args:
            to_: address
        Returns:
            uint256
        """
        ...

    @overload
    def mint(self, to_: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#110)

        Args:
            to_: address
        Returns:
            uint256
        """
        ...

    @overload
    def mint(self, to_: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#110)

        Args:
            to_: address
        Returns:
            uint256
        """
        ...

    @overload
    def mint(self, to_: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[uint256]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#110)

        Args:
            to_: address
        Returns:
            uint256
        """
        ...

    def mint(self, to_: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[uint256, TransactionAbc[uint256], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#110)

        Args:
            to_: address
        Returns:
            uint256
        """
        return self._execute(self.chain, request_type, "6a627842", [to_], True if request_type == "tx" else False, uint256, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def burn(self, to_: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[uint256, uint256]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#142)

        Args:
            to_: address
        Returns:
            (uint256, uint256)
        """
        ...

    @overload
    def burn(self, to_: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#142)

        Args:
            to_: address
        Returns:
            (uint256, uint256)
        """
        ...

    @overload
    def burn(self, to_: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#142)

        Args:
            to_: address
        Returns:
            (uint256, uint256)
        """
        ...

    @overload
    def burn(self, to_: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[Tuple[uint256, uint256]]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#142)

        Args:
            to_: address
        Returns:
            (uint256, uint256)
        """
        ...

    def burn(self, to_: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[Tuple[uint256, uint256], TransactionAbc[Tuple[uint256, uint256]], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#142)

        Args:
            to_: address
        Returns:
            (uint256, uint256)
        """
        return self._execute(self.chain, request_type, "89afcb44", [to_], True if request_type == "tx" else False, Tuple[uint256, uint256], from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def swap(self, amount0Out: uint256, amount1Out: uint256, to_: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#167)

        Args:
            amount0Out: uint256
            amount1Out: uint256
            to_: address
            data: bytes
        """
        ...

    @overload
    def swap(self, amount0Out: uint256, amount1Out: uint256, to_: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#167)

        Args:
            amount0Out: uint256
            amount1Out: uint256
            to_: address
            data: bytes
        """
        ...

    @overload
    def swap(self, amount0Out: uint256, amount1Out: uint256, to_: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#167)

        Args:
            amount0Out: uint256
            amount1Out: uint256
            to_: address
            data: bytes
        """
        ...

    @overload
    def swap(self, amount0Out: uint256, amount1Out: uint256, to_: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#167)

        Args:
            amount0Out: uint256
            amount1Out: uint256
            to_: address
            data: bytes
        """
        ...

    def swap(self, amount0Out: uint256, amount1Out: uint256, to_: Union[Account, Address], data: Union[bytearray, bytes], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#167)

        Args:
            amount0Out: uint256
            amount1Out: uint256
            to_: address
            data: bytes
        """
        return self._execute(self.chain, request_type, "022c0d9f", [amount0Out, amount1Out, to_, data], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def skim(self, to_: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#198)

        Args:
            to_: address
        """
        ...

    @overload
    def skim(self, to_: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#198)

        Args:
            to_: address
        """
        ...

    @overload
    def skim(self, to_: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#198)

        Args:
            to_: address
        """
        ...

    @overload
    def skim(self, to_: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#198)

        Args:
            to_: address
        """
        ...

    def skim(self, to_: Union[Account, Address], *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#198)

        Args:
            to_: address
        """
        return self._execute(self.chain, request_type, "bc25cf77", [to_], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

    @overload
    def sync(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["call"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> None:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#206)
        """
        ...

    @overload
    def sync(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["estimate"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> int:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#206)
        """
        ...

    @overload
    def sync(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["access_list"], gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Tuple[Dict[Address, List[int]], int]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#206)
        """
        ...

    @overload
    def sync(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: Literal["tx"] = "tx", gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> TransactionAbc[None]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#206)
        """
        ...

    def sync(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Union[int, str] = 0, gas_limit: Optional[Union[int, Literal["max"], Literal["auto"]]] = None, request_type: RequestType = 'tx', gas_price: Optional[Union[int, str]] = None, max_fee_per_gas: Optional[Union[int, str]] = None, max_priority_fee_per_gas: Optional[Union[int, str]] = None, access_list: Optional[Union[Dict[Union[Account, Address, str], List[int]], Literal["auto"]]] = None, type: Optional[int] = None, block: Optional[Union[int, Literal["latest"], Literal["pending"], Literal["earliest"], Literal["safe"], Literal["finalized"]]] = None, confirmations: Optional[int] = None) -> Union[None, TransactionAbc[None], int, Tuple[Dict[Address, List[int]], int]]:
        """
        [Source code](file:///Users/dteiml/p/hacker-dom/woke-uniswap-v2/src/UniswapV2Pair.sol#206)
        """
        return self._execute(self.chain, request_type, "fff6cae9", [], True if request_type == "tx" else False, NoneType, from_, to if to is not None else str(self.address), value, gas_limit, gas_price, max_fee_per_gas, max_priority_fee_per_gas, access_list, type, block, confirmations)

UniswapV2Pair.MINIMUM_LIQUIDITY.selector = b'\xba\x9azV'
UniswapV2Pair.factory.selector = b'\xc4Z\x01U'
UniswapV2Pair.token0.selector = b'\r\xfe\x16\x81'
UniswapV2Pair.token1.selector = b'\xd2\x12 \xa7'
UniswapV2Pair.price0CumulativeLast.selector = b'Y\t\xc0\xd5'
UniswapV2Pair.price1CumulativeLast.selector = b'Z=T\x93'
UniswapV2Pair.kLast.selector = b'td\xfc='
UniswapV2Pair.getReserves.selector = b'\t\x02\xf1\xac'
UniswapV2Pair.initialize.selector = b'H\\\xc9U'
UniswapV2Pair.mint.selector = b'jbxB'
UniswapV2Pair.burn.selector = b'\x89\xaf\xcbD'
UniswapV2Pair.swap.selector = b'\x02,\r\x9f'
UniswapV2Pair.skim.selector = b'\xbc%\xcfw'
UniswapV2Pair.sync.selector = b'\xff\xf6\xca\xe9'
