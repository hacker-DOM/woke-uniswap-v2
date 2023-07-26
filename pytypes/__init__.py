
import woke.development.core
from woke.utils import get_package_version

if get_package_version("woke") != "3.5.0":
    raise RuntimeError("Pytypes generated for a different version of woke. Please regenerate.")

woke.development.core.errors = {b'\x08\xc3y\xa0': {'': ('woke.development.transactions', ('Error',))}, b'NH{q': {'': ('woke.development.transactions', ('Panic',))}}
woke.development.core.events = {b'\x8c[\xe1\xe5\xeb\xec}[\xd1OqB}\x1e\x84\xf3\xdd\x03\x14\xc0\xf7\xb2)\x1e[ \n\xc8\xc7\xc3\xb9%': {'IERC20.sol:IERC20': ('pytypes.IERC20', ('IERC20', 'Approval')), 'src/UniswapV2ERC20.sol:UniswapV2ERC20': ('pytypes.src.UniswapV2ERC20', ('UniswapV2ERC20', 'Approval')), 'woke_tests/mocks/ERC20.sol:ERC20': ('pytypes.src.UniswapV2ERC20', ('UniswapV2ERC20', 'Approval')), 'src/UniswapV2Pair.sol:UniswapV2Pair': ('pytypes.src.UniswapV2ERC20', ('UniswapV2ERC20', 'Approval'))}, b'\xdd\xf2R\xad\x1b\xe2\xc8\x9bi\xc2\xb0h\xfc7\x8d\xaa\x95+\xa7\xf1c\xc4\xa1\x16(\xf5ZM\xf5#\xb3\xef': {'IERC20.sol:IERC20': ('pytypes.IERC20', ('IERC20', 'Transfer')), 'src/UniswapV2ERC20.sol:UniswapV2ERC20': ('pytypes.src.UniswapV2ERC20', ('UniswapV2ERC20', 'Transfer')), 'woke_tests/mocks/ERC20.sol:ERC20': ('pytypes.src.UniswapV2ERC20', ('UniswapV2ERC20', 'Transfer')), 'src/UniswapV2Pair.sol:UniswapV2Pair': ('pytypes.src.UniswapV2ERC20', ('UniswapV2ERC20', 'Transfer'))}, b'\xdc\xcdA/\x0b\x12R\x81\x9c\xb1\xfd3\x0b\x93"L\xa4&\x12\x89+\xb3\xf4\xf7\x89\x97nm\x81\x93d\x96': {'src/UniswapV2Pair.sol:UniswapV2Pair': ('pytypes.src.UniswapV2Pair', ('UniswapV2Pair', 'Burn'))}, b'L \x9b_\xc8\xadPu\x8f\x13\xe2\xe1\x08\x8b\xa5jV\r\xffi\n\x1co\xef&9OL\x03\x82\x1cO': {'src/UniswapV2Pair.sol:UniswapV2Pair': ('pytypes.src.UniswapV2Pair', ('UniswapV2Pair', 'Mint'))}, b'\xd7\x8a\xd9_\xa4l\x99KeQ\xd0\xda\x85\xfc\'_\xe6\x13\xce7e\x7f\xb8\xd5\xe3\xd10\x84\x01Y\xd8"': {'src/UniswapV2Pair.sol:UniswapV2Pair': ('pytypes.src.UniswapV2Pair', ('UniswapV2Pair', 'Swap'))}, b'\x1cA\x1e\x9a\x96\xe0q$\x1c/!\xf7rk\x17\xae\x89\xe3\xca\xb4\xc7\x8b\xe5\x0e\x06+\x03\xa9\xff\xfb\xba\xd1': {'src/UniswapV2Pair.sol:UniswapV2Pair': ('pytypes.src.UniswapV2Pair', ('UniswapV2Pair', 'Sync'))}, b"\r6H\xbd\x0fk\xa8\x014\xa3;\xa9'Z\xc5\x85\xd9\xd3\x15\xf0\xad\x83U\xcd\xde\xfd\xe3\x1a\xfa(\xd0\xe9": {'src/UniswapV2Factory.sol:UniswapV2Factory': ('pytypes.src.UniswapV2Factory', ('UniswapV2Factory', 'PairCreated'))}}
woke.development.core.contracts_by_fqn = {'IERC20.sol:IERC20': ('pytypes.IERC20', ('IERC20',)), 'IUniswapV2Callee.sol:IUniswapV2Callee': ('pytypes.IUniswapV2Callee', ('IUniswapV2Callee',)), 'libs/Math.sol:Math': ('pytypes.libs.Math', ('Math',)), 'libs/SafeMath.sol:SafeMath': ('pytypes.libs.SafeMath', ('SafeMath',)), 'libs/UQ112x112.sol:UQ112x112': ('pytypes.libs.UQ112x112', ('UQ112x112',)), 'src/UniswapV2ERC20.sol:UniswapV2ERC20': ('pytypes.src.UniswapV2ERC20', ('UniswapV2ERC20',)), 'woke/console.sol:console': ('pytypes.woke.console', ('console',)), 'woke_tests/mocks/ERC20.sol:ERC20': ('pytypes.woke_tests.mocks.ERC20', ('ERC20',)), 'src/UniswapV2Pair.sol:UniswapV2Pair': ('pytypes.src.UniswapV2Pair', ('UniswapV2Pair',)), 'src/UniswapV2Factory.sol:UniswapV2Factory': ('pytypes.src.UniswapV2Factory', ('UniswapV2Factory',))}
woke.development.core.contracts_by_metadata = {b'\xa2dipfsX"\x12 \x7f\xeeH2\xfa\xda\xa1\xb9h\x19p4f\xd28\x88\xf7M\x0cJW\x0b;&\xa76\x9f\xe3\xc7\'f\xf7dsolcC\x00\x08\x14\x003': 'libs/Math.sol:Math', b'\xa2dipfsX"\x12 u\t?\'F\x97^i\x19\x17\x01\xb5V\xae\xcb\n4I\xed\xe9T\x9b\xec\xe6\xf4X(\x0b\x9ei\x92\xf6dsolcC\x00\x08\x14\x003': 'libs/SafeMath.sol:SafeMath', b'\xa2dipfsX"\x12 \x8f\xc4\x1a\xaa\xcfz\xd1\x1c\xc1\xec\xf7\xb2\xb3\x83\xc0|\xbc\xb8E\xfb\xa8\xa9\x1aj\x18f\xc0j\xe8\xd9\x03}dsolcC\x00\x08\x14\x003': 'libs/UQ112x112.sol:UQ112x112', b'\xa2dipfsX"\x12 \x08U\x99\xbc\x1e\xfb\x96\x90\n;\xfc\xbdM\xec\xded\x93\xedU\x84\xe0\x93q\xb2\xca\xac\xeeW\x9fP\xff\xe6dsolcC\x00\x08\x14\x003': 'src/UniswapV2ERC20.sol:UniswapV2ERC20', b'\xa2dipfsX"\x12 F%r\xe9\x94\x06\xfc}\xf4\xb7\xed\r<kE7!\xa0\xdc\x80<\x8b\x96\xcd\xcf\xa5\xbc{\xbcK\x8c\xb9dsolcC\x00\x08\x14\x003': 'woke/console.sol:console', b'\xa2dipfsX"\x12 \x9c\x8czW2r\xd5\xfePh\t2)\xb0\xa6\xc7g\xf3f\xb5\x03\x10\xc6\x85{\xff?\xee=&/\x88dsolcC\x00\x08\x14\x003': 'woke_tests/mocks/ERC20.sol:ERC20', b'\xa2dipfsX"\x12 L\xc1\xdeX/H\x8b\x16<\x05i9\xc2\xc8k\x1b\x01\x97\xe0\xc3`\xa7G\x19\xa4e\xc0i\xeb\xc0\xaeydsolcC\x00\x08\x14\x003': 'src/UniswapV2Pair.sol:UniswapV2Pair', b'\xa2dipfsX"\x12 X\x93\x1b\x91\xa7r\xbd\x8a~\x97\x9e}\xf8c>\n+\x81X\xedt=\xd5\x8f\x1c\xa5\xe2\xda\xb9-@\x88dsolcC\x00\x08\x14\x003': 'src/UniswapV2Factory.sol:UniswapV2Factory'}
woke.development.core.contracts_inheritance = {'IERC20.sol:IERC20': ('IERC20.sol:IERC20',), 'IUniswapV2Callee.sol:IUniswapV2Callee': ('IUniswapV2Callee.sol:IUniswapV2Callee',), 'libs/Math.sol:Math': ('libs/Math.sol:Math',), 'libs/SafeMath.sol:SafeMath': ('libs/SafeMath.sol:SafeMath',), 'libs/UQ112x112.sol:UQ112x112': ('libs/UQ112x112.sol:UQ112x112',), 'src/UniswapV2ERC20.sol:UniswapV2ERC20': ('src/UniswapV2ERC20.sol:UniswapV2ERC20',), 'woke/console.sol:console': ('woke/console.sol:console',), 'woke_tests/mocks/ERC20.sol:ERC20': ('woke_tests/mocks/ERC20.sol:ERC20', 'src/UniswapV2ERC20.sol:UniswapV2ERC20'), 'src/UniswapV2Pair.sol:UniswapV2Pair': ('src/UniswapV2Pair.sol:UniswapV2Pair', 'src/UniswapV2ERC20.sol:UniswapV2ERC20'), 'src/UniswapV2Factory.sol:UniswapV2Factory': ('src/UniswapV2Factory.sol:UniswapV2Factory',)}
woke.development.core.contracts_revert_index = {}
woke.development.core.creation_code_index = [(((160, b'g3\xa1#N\xd1\xbc\xa25\xd7\xc0\x11\xc8d\x19\x9b]\x80Dq\x9a\x9b\x99\xdf^\x9d\x0b\x1d\xdd\xe6\x81\x8a'),), 'libs/Math.sol:Math'), (((160, b'Y\xaf.\xb3\xd8\xdb\x99\xcb7\x19\x1b\xd9\x8b\xeb\x14+fr\xde%\xd1g-N]\xcbV\xfc\x9f\xbc\x9b\xb0'),), 'libs/SafeMath.sol:SafeMath'), (((160, b'\x04\x8aI\x9aL\xe3\xc5\xa2\x1cqI**\xc3\xc8\xa4\x99;\xdfZ\xdb]\xb4Y\x9a\x04]\xddvz\xa7\xaa'),), 'libs/UQ112x112.sol:UQ112x112'), (((5271, b"\x11\xae\xde+\xaa1'\x0c\xdb\xb6\xa0\x9cw'BM\xe8)\xda+\xb0r\x1bFP\x15\xf2m\x94\xf1\xc3\xa5"),), 'src/UniswapV2ERC20.sol:UniswapV2ERC20'), (((160, b'\x1c\x1c\xfa\xdf\xc2\xc1H\x9ew\xcc\x84\x8f\xb6\xe2\xde\x04\x0f\xc1u\xcc2:\x9f\xcb\x94\xa9\xce\x15\x16\x9fV\x82'),), 'woke/console.sol:console'), (((6400, b'\xdf\xa2O\xad\xee\xa7\xc2z:\xb0\x92\xa4w\xd5\\y\xb4\xce\x88\x18*#\xb0\xb5;\xfc:\xf6\x12\xe0=#'),), 'woke_tests/mocks/ERC20.sol:ERC20'), (((18318, b'\xb6\x96\xef\xf7<\x19\xa8\x81\xb0\x11\x84\x1e\x1c\x94\xa6U\xdf6\x8c\x90\xf4\x8a\xa5Q\xde2>\xaf^4\xc4\x9f'),), 'src/UniswapV2Pair.sol:UniswapV2Pair'), (((22188, b'\xdfam"\xfa\x1c\x1d\x81\x0c\xa5\x00UDl;oi\xf0\xa8^\xef\x0c\xdak\xd4%Vw\xab\xf3\x1f\x96'),), 'src/UniswapV2Factory.sol:UniswapV2Factory')]